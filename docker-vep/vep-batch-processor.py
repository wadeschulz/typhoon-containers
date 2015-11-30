__author__    = 'Wade Schulz'
__email__     = 'wade.schulz@gmail.com'
__version__   = '1.0'
__date__      = '11/30/2015'
__pyver__     = '2.7'

"""
####################### Ensembl VEP Batch Script ###############################

            Python script to bulk process specimens with VEP

            > Input: Directory with VEP input files
            > Output: VEP annotation files

################################################################################
"""

##### Import python modules
################################################################################

import os
from os import listdir
from os.path import isfile, join

################################################################################
##### Classes
################################################################################

os.system('cls' if os.name == 'nt' else 'clear')
script_base = '/home/bio/ensembl-tools-release-82/scripts/variant_effect_predictor/'

# Enter input/output paths
base_path = raw_input('Enter data base directory: ')

input_path = join(base_path, "input")
out_base = join(base_path, "output")

path_list = [out_base]
for directory in path_list:
  if not os.path.exists(directory):
    os.makedirs(directory)

input_files = [f for f in listdir(input_path) if isfile(join(input_path, f))]
script_path = join(script_base, "variant_effect_predictor.pl")

for file in input_files:
  name = file.split('.')[0]
  print "Evaluating specimen: " + name + " (" + file + ")"
  full_input = join(input_path, file)
  out_path = join(out_base, name + '.out')
  #port 3337 for GRCh37
  os.system('perl ' + script_path + ' -i ' + full_input + ' -o ' + out_path + ' --database --fork 5 --hgvs --symbol --assembly GRCh37 --port 3337 --species homo_sapiens --canonical')