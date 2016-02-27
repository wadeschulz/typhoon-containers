__author__    = 'Tommy Durant, Wade Schulz'
__email__     = 'thomas.sakrison.durant@gmail.com, wade.schulz@gmail.com'
__version__   = '1.0'
__date__      = '11/26/2015'
__pyver__     = '2.7'

"""
#######################  SciCloneClient ########################################
 
            Python based SciClone bulk runner
 
            > SciClone python client for bulk run of VCF files
            > Input: Directory with VCF files, output directory, and number of
                      iterations to run SciClone
            > Output: Clone clusterTable and clusterPlot, summary statistics
 
################################################################################
"""

##### Import python modules
################################################################################

import os
from os import listdir
from os.path import isfile, join
import vcf
import rpy2.robjects as robjects
import csv

################################################################################
##### Classes
################################################################################

class Result(object):
    sample = ""
    variants = 0
    parameters = ""
    clone_counts = []

def CloneCount(path):
    """
    Iterates through SciClone output to find max clone count
    """

    max = 0
    with open(path, 'r') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')
    
        i = 0
        for row in tsvin:
            i += 1
            if i == 1:
                continue
            clones = row[9]
            if clones == 'NA':
                continue
            cloneCount = int(clones)
            if cloneCount > max:
                max = cloneCount
    return max

# set minimum number variants/max clusters
min_variants = 6

# Initialize R
robjects.r('sink("/dev/null")')
robjects.r('library(sciClone)')

os.system('cls' if os.name == 'nt' else 'clear')
print "R and SciClone successfully loaded."
print ""

# Enter input/output paths
base_path = raw_input('Enter data base directory: ')
iterations = int(raw_input ('Enter number of SciClone iterations: '))

input_path = join(base_path, "input")
out_base = join(base_path, "output")
tbl_path = join(out_base, "tables")
pdf_path = join(out_base, "pdf")
stat_path = join(out_base, "stats")

artifacts = []
artifact_path = join(base_path, "artifacts.txt")

# if an artifact file exists, pull in list
if os.path.exists(artifact_path):
  with open(artifact_path, 'r') as f:
    artifacts.extend(f.read().splitlines())

path_list = [tbl_path, pdf_path, stat_path]
for directory in path_list:
  if not os.path.exists(directory):
    os.makedirs(directory)

input_files = [f for f in listdir(input_path) if isfile(join(input_path, f))]
results = [] # array for results

stat_file = open(join(stat_path, 'stats.tsv'), 'w')
stat_file.write('id\tvariants\titer\tavg clones\tmin clones\tmax clones\n')

file_idx = 0
total_files = len(input_files)

os.system('cls' if os.name == 'nt' else 'clear')
for file in input_files:
  file_idx = file_idx + 1
  file_path = input_path + '/' + file
  # Create result object
  result = Result()
  del result.clone_counts[:]
  result.sample = file.split('.')[0]
  
  print "Evaluating specimen: " + result.sample + " (" + str(file_idx) + " of " + str(total_files) + ")"
  
  with open(file_path) as f:
    result.variants = sum(1 for _ in f)
  
  print "\tTotal variants: " + str(result.variants)

  if result.variants < min_variants:
    print "\tToo few variants for clonal evaulation"
    continue

  print "\tEvaluating clonality..."
  # Set counter for number of iterations to run through sciclone
  curIter = 0
  while curIter < iterations:
    table_file_path = join(tbl_path, result.sample + '-' + str(curIter) + '.tbl')
    pdf_file_path = join(pdf_path, result.sample + '-' + str(curIter) + '.pdf')

    robjects.r('inputData = read.table("' + file_path + '")')
    robjects.r('sc = sciClone(vafs=inputData, sampleName="", maximumClusters=' + str(min_variants) + ')')
    robjects.r('writeClusterTable(sc, "' + table_file_path + '")')
    robjects.r('sc.plot1d(sc, "' + pdf_file_path + '")')
    robjects.r('rm(list=ls())')
        
    cur_clone_count = CloneCount(table_file_path)
    result.clone_counts.append(cur_clone_count)
    print "\t\tIter (" + str(curIter + 1) + " of " + str(iterations) + ") clones: " + str(cur_clone_count)
    curIter = curIter + 1

  actual_iter = len(result.clone_counts)
  avg_clones = float(reduce(lambda x, y: x + y, result.clone_counts)) / float(actual_iter)
  min_clones = min(result.clone_counts)
  max_clones = max(result.clone_counts)

  stat_file.write(result.sample + '\t' + str(result.variants) + '\t' + str(actual_iter) + '\t' + str(avg_clones) + '\t' + str(min_clones) + '\t' + str(max_clones) + '\t')
  stat_file.write('\t'.join("'{0}'".format(n) for n in result.clone_counts) + '\n')

  print "\tAvg Clones: " + str(avg_clones) + ", Min: " + str(min_clones) + ", Max: " + str(max_clones)

robjects.r('sink()')