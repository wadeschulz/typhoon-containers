import os
from sys import argv

script, chr, loc = argv

tabixCmd = "../tabix-0.2.6/tabix -fh ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20100804/ALL.2of4intersection.20100804.genotypes.vcf.gz " + chr + ":" + loc + "-" + loc + " > genotypes.vcf"

os.system(tabixCmd)

vcfToolsCmd = "../vcftools-0.1.13/cpp/vcftools --vcf genotypes.vcf --freq --out allelefrequencies"
os.system(vcfToolsCmd)

os.remove("allelefrequencies.log")
os.remove("genotypes.vcf")
os.remove("ALL.2of4intersection.20100804.genotypes.vcf.gz.tbi")

lines = [line.rstrip() for line in open('allelefrequencies.frq')]
os.remove("allelefrequencies.frq")

print lines[1]