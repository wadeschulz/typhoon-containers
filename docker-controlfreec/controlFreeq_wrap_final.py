#!/usr/bin/env python

###############################################################################
######### Import
###############################################################################

import os
import sys
import time
import argparse
import traceback
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


###############################################################################
######### Create file objects
###############################################################################

#create time stamp YYMMDD_HH:MM:SS  (Greenwhich mean time)
logStamp = strftime('%Y%m%d_%H:%M:%S',gmtime())

#create log file name RSOIS_YYYYMMDD.log
logFile = str('controlFreeq_wrap.log.txt')


###############################################################################
######### Test file connections
###############################################################################

newUser = "#####################################################################"

#Create connection to log file
try:
	pywrapLog = open(os.path.join(logPath, logFile), 'a')
	pywrapLog.write('\n'+newUser+'\n'+logStamp + "-- Successfully opened log file")
except:
	pywrapLog.write('\n'+logStamp + 'Invalid pathname, or invalid user permissions\n')
	raise IOError('Invalid pathname, or invalid user permissions')


###############################################################################
######### Classes and functions
###############################################################################

# Create function for UNcaught exceptions
def catchExceptions(exctype, value, tb):
	pywrapLog.write('\n'+logStamp+'-- '+'UNCAUGHT ERROR')
	exctype = str(exctype)
	pywrapLog.write('\n'+'TYPE: ' + exctype)
	pywrapLog.write('\n'+'VALUE: ' + str(value))
	tb = traceback.extract_tb(tb)
	pywrapLog.write('\n'+'TRACEBACK: '+'\n')
	for item in tb:
		pywrapLog.write(str(item))
		pywrapLog.write('> \n')


# Override excepthook; will return uncaught exceptions in catchExceptions
sys.excepthook = catchExceptions

parser = argparse.ArgumentParser('Support script for ControlFREEQ client')

# REQUIRED 
parser.add_argument('--runId', type=str, required=True)
parser.add_argument('--input', type=file, required=True)
parser.add_argument('--control', type=file, required=True)
parser.add_argument('--chrPath', type=str, required=True)
parser.add_argument('--outputPath', type=str, required=True)
parser.add_argument('--bed', type=file, required=True)

# OPTIONAL
parser.add_argument('--step', type=int, default=250, required=False)
parser.add_argument('--intercept', type=int, default=0, required=False)
parser.add_argument('--threads', type=int, default=1, required=False)
parser.add_argument('--minDepth', type=int, default=50, required=False)
parser.add_argument('--contamination', type=int, default=0, required=False)


###############################################################################
######### Main
###############################################################################


def main(*args):
	
	try:
		try:

			args = parser.parse_args()

			# check for outputPath directory; if not, then create
			if not os.path.isdir(args.outputPath):
				os.makedirs(args.outputPath)

			# check for chrPath directory; if not, then create
			if not os.path.isdir(args.chrPath):
				os.makedirs(args.chrPath)

			try: 
				config = ConfigParser.ConfigParser()

				configFile = str(args.runId + '.config')
				
				pywrapConfig = open(args.outputPath + configFile, 'wb')
				pywrapLog.write('\n'+logStamp + "-- Successfully opened config file")

				config.add_section('general')
				config.add_section('sample')
				config.add_section('control')
				config.add_section('BAF')
				config.add_section('target')


			except IOError:
				pywrapLog.write('\n'+logStamp + 'Invalid pathname, or invalid user permissions\n')
				raise IOError('Invalid pathname, or invalid user permissions')

			pywrapLog.write('\n'+logStamp + "-- Successfully passed arguments\n")
			
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
			if not args.contamination == 0:
				config.set('general', 'contamination', args.contamination)
			
			config.set('sample', 'mateFile', args.input)
			config.set('sample', 'inputFormat', 'SAM')
			config.set('sample', 'mateOrientation', '0')

			config.set('control', 'mateFile', args.control)
			config.set('control', 'inputFormat', 'SAM')
			config.set('control', 'mateOrientation', '0')

			config.set('target', 'captureRegions', args.bed)



			# write to config file
			config.write(pywrapConfig)

		except:
			raise
	except:
		raise
		return 2
	return 0



###############################################################################
######### Run
###############################################################################

if __name__ == "__main__":
	sys.exit(main())

	
