import os

os.system('cgquery -o /mnt/tcga/' + analysisId + '.xml "analysis_id=' + analysisId + '"')
os.system('gtdownload -v -p /mnt/tcga/download -c /mnt/tcga/credentials --max-children 16 /mnt/tcga/' + analysisId + '.xml')