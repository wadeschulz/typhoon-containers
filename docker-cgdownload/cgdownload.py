import os, sys

analysisId = sys.argv[1]

os.system('/bin/bash -c \'cgquery -o /mnt/data/cgquery/' + analysisId + '.xml analysis_id="' + analysisId + '"\'')
os.system('/bin/bash -c \'gtdownload -v -p /mnt/data/download -c /mnt/data/credentials --max-children 16 /mnt/data/cgquery/' + analysisId + '.xml\'')