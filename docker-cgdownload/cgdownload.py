import os, sys

analysisId = sys.argv[1]

os.system('/bin/bash -c \'cgquery -o /mnt/tcga/temp.xml analysis_id="' + analysisId + '"\'')
os.system('/bin/bash -c \'gtdownload -vvvv -p /mnt/tcga/download -c /mnt/tcga/credentials --max-children 16 /mnt/tcga/temp.xml\'')