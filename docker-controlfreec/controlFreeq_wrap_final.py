#!/usr/bin/env python

###############################################################################
######### Import
###############################################################################

#
import os
import sys
import time
import logging
import argparse
import ConfigParser

from time import strftime, gmtime


###############################################################################
######### Paths
###############################################################################

# set current working directory path
pgmPath = os.getcwd()

# set log path
logPath = pgmPath + '/log'
if not os.path.isdir(logPath):
	os.makedirs(logPath)

# set output path
outputPath = pgmPath + '/output'
if not os.path.isdir(outputPath):
	os.makedirs(outputPath)



###############################################################################
######### Log file and time stamp
###############################################################################

#create time stamp YYMMDD_HH:MM:SS  (Greenwhich mean time)
logStamp = strftime('%Y%m%d_%H:%M:%S',gmtime())

#create log file name RSOIS_YYYYMMDD.log
logFile = str('controlFreeq_wrap.log.txt')


###############################################################################
######### Test file connections
###############################################################################

newUser = "#####################################################################"

#Create conneciton to log file
try:
	pywrapLog = open(os.path.join(logPath, logFile), 'a')
	pywrapLog.write('\n'+newUser+'\n'+logStamp + "--Successfully opened log file")
except:
	pywrapLog.write('\n'+logStamp + 'Invalid pathname, or invalid user permissions\n')
	raise IOError('Invalid pathname, or invalid user permissions')


###############################################################################
######### Define Arguments
###############################################################################

parser = argparse.ArgumentParser('Support script for ControlFREEQ client')

# REQUIRED
parser.add_argument('--runId', type=str, required=True)
# check for file
parser.add_argument('--input', type=str, required=True)
parser.add_argument('--control', type=str, required=True)

# check for directory
parser.add_argument('--chrPath', type=str, required=True)
# output path create if not there
parser.add_argument('--outputPath', type=str, required=True)

# check for file
parser.add_argument('--bed', type=str, required=True)

# OPTIONAL
parser.add_argument('--step', type=int, default=250, required=False)
parser.add_argument('--intercept', type=int, default=0, required=False)
parser.add_argument('--threads', type=int, default=1, required=False)
parser.add_argument('--minDepth', type=int, default=50, required=False)


# if 0 don't include in parameters 
parser.add_argument('--contamination', type=int, default=0)


###############################################################################
######### Main
###############################################################################


def main(*args):

	# try:
	# 	try:
	print "here"
	args = parser.parse_args()
	try: 
		config = ConfigParser.ConfigParser()

		configFile = str(args.runId + '.config')
		
		pywrapConfig = open(args.outputPath + configFile, 'wb')
		pywrapLog.write('\n'+logStamp + "--Successfully opened config file")

		config.add_section('general')
		config.add_section('sample')
		config.add_section('control')
		config.add_section('BAF')
		config.add_section('target')


	except IOError:
		pywrapLog.write('\n'+logStamp + 'Invalid pathname, or invalid user permissions\n')
		raise IOError('Invalid pathname, or invalid user permissions')

	pywrapLog.write('\n'+logStamp + "--Successfully passed arguments\n")
	
	config.set('general', 'chrLenFile', '/mnt/data/hg19.len')
	config.set('general', 'window', '1000'+'\n')
	
	config.set('general', 'step', args.step)
	config.set('general', 'ploidy', '2')
	config.set('general', 'chrFiles', str(args.chrPath)+'\n')

	config.set('general', 'intercept', args.intercept)
	config.set('general', 'minMappabilityPerWindow', '0.7'+'\n')
	
	config.set('general', 'outputDir', str(args.outputPath) + '\n')
	
	config.set('general', 'breakPointType', '4')
	config.set('general', 'maxThreads', '4')
	config.set('general', 'readCountThreshold', '50' + '\n')
	
	config.set('general', 'contaminationAdjustment', 'True')
	config.set('general', 'contamination', '65')
	
	config.set('sample', 'mateFile', args.input)
	config.set('sample', 'inputFormat', 'SAM')
	config.set('sample', 'mateOrientation', '0')

	config.set('control', 'mateFile', args.control)
	config.set('control', 'inputFormat', 'SAM')
	config.set('control', 'mateOrientation', '0')

	config.set('target', 'captureRegions', args.bed)

	config.write(pywrapConfig)
	return 0

###############################################################################
######### Run
###############################################################################

if __name__ == "__main__":
	sys.exit(main())

	
