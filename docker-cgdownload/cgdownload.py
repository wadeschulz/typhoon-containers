import os, sys

analysisId = sys.argv[1]

os.system('/bin/bash -c \'cgquery -o /mnt/data/temp.xml analysis_id="' + analysisId + '"\'')
os.system('/bin/bash -c \'gtdownload -vvvv -p /mnt/data/download -c /mnt/data/credentials --max-children 16 /mnt/data/' + analysisId + '.xml\'')