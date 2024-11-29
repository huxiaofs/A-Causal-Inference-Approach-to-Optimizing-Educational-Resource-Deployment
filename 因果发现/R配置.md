## Causal Discovery

* GES algorithm (I guess there will be a lot of unfamiliar algorithm occur in the package)
* R environment needed, install in the R console by commandlines below:
````commandline
ENV_PATH <- "D:/R/R-4.3.3/library"
install.packages(c("V8"),repos="http://cran.us.r-project.org", quiet=TRUE, lib= ENV_PATH, verbose=FALSE)
install.packages(c("sfsmisc"),repos="http://cran.us.r-project.org", quiet=TRUE, lib= ENV_PATH, verbose=FALSE)
install.packages(c("clue"),repos="http://cran.us.r-project.org", quiet=TRUE, lib= ENV_PATH, verbose=FALSE)
install.packages("https://cran.r-project.org/src/contrib/Archive/randomForest/randomForest_4.6-14.tar.gz", repos=NULL, lib= ENV_PATH, type="source")
install.packages(c("lattice"),repos="http://cran.us.r-project.org", quiet=TRUE, lib= ENV_PATH, verbose=FALSE)
install.packages(c("devtools"),repos="http://cran.us.r-project.org", quiet=TRUE, lib= ENV_PATH, verbose=FALSE)
install.packages(c("MASS"),repos="http://cran.us.r-project.org", quiet=TRUE, lib= ENV_PATH, verbose=FALSE)
install.packages("BiocManager", lib= ENV_PATH)
BiocManager::install(c("igraph"), lib= ENV_PATH)
install.packages("https://cran.r-project.org/src/contrib/Archive/fastICA/fastICA_1.2-2.tar.gz", repos=NULL, lib= ENV_PATH, type="source")
BiocManager::install(c("SID", "bnlearn", "pcalg", "kpcalg", "glmnet", "mboost"), lib= ENV_PATH)
install.packages("https://cran.r-project.org/src/contrib/Archive/CAM/CAM_1.0.tar.gz", repos=NULL, lib= ENV_PATH, type="source")
install.packages("https://cran.r-project.org/src/contrib/sparsebnUtils_0.0.8.tar.gz", repos=NULL, lib= ENV_PATH, type="source")
BiocManager::install(c("ccdrAlgorithm", "discretecdAlgorithm"), lib= ENV_PATH)
install.packages("devtools", lib= ENV_PATH)
library(devtools); install_github("cran/CAM"); install_github("cran/momentchi2"); install_github("Diviyan-Kalainathan/RCIT", quiet=TRUE, lib= ENV_PATH, verbose=FALSE)
install.packages("https://cran.r-project.org/src/contrib/Archive/sparsebn/sparsebn_0.1.2.tar.gz", repos=NULL, lib= ENV_PATH, type="source")