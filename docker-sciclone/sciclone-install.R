#set CRAN repository address
local({r <- getOption("repos")
       r["CRAN"] <- "http://cran.r-project.org" 
       options(repos=r)})

#install IRanges from bioconductor
source("http://bioconductor.org/biocLite.R")
biocLite("IRanges")

#install devtools, bmm, and sciclone
Sys.setenv(RGL_USE_NULL = "True")
install.packages("devtools")
library(devtools)
install_github("genome/bmm")
install_github("genome/sciClone")