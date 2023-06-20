install.packages("FactoMineR")
install.packages("factoextra")
install.packages("corrplot")

library("FactoMineR")
library("factoextra")
library("corrplot")

# Reading and cleaning data
df <- read.csv(file = "./CSVs/ms-data.csv", header = TRUE)
df_clean <- df[-c(1:3)]

var_names <- c("has_conflict", 
               "top_p", 
               "top_pt", 
               "top_ps", 
               "occ_p", 
               "occ_pt", 
               "occ_ps",
               "top_ms",
               "top_mst",
               "top_mss",
               "occ_ms",
               "occ_mst",
               "occ_mss",
               "devs",
               "devs_t",
               "devs_s",
               "devs_ts",
               "files",
               "files_t",
               "files_s",
               "files_ts",
               "chunks",
               "chunks_t",
               "chunks_s",
               "loc",
               "loc_t",
               "loc_s",
               "commits",
               "commits_t",
               "commits_s"
)
names(df_clean) <- var_names

# Computing correlation matrix
M <- cor(df_clean)
corrplot(M, type="upper", method="circle", tl.col = "black")

# Computing correlation dependent (has_conflict) versus independent variables
our.cor.test <- function(r.dat, com.measure){
  result <- cor.test(r.dat[,"has_conflict"], r.dat[,com.measure], 
                     alternative = "two.sided", method = "spearman", 
                     exact = NULL, conf.level = 0.95, continuity = FALSE)
  return(result)
}

corr_data_frame <- data.frame()
for (variable in var_names[-1]) {
  cor.test <- our.cor.test(df_clean, variable)
  estimate <- as.numeric(cor.test$estimate)
  new_row = c(variable, estimate)
  corr_data_frame = rbind(corr_data_frame,new_row)
}

names(corr_data_frame) <- c("variable", "coefficient")

# PCA analysis

fit <- princomp(df_clean)
summary(fit)

par(mfrow=c(1,1))
plot(fit, type = "lines", main = "Number of Components")

pca_analysis <- PCA(df_clean, graph = FALSE)

par(mar = c(1,1,2,0.1))
fviz_pca_var(pca_analysis, 
             col.var="cos2", 
             labelsize= 5, 
             gradient.cols = c("#C0F228", "#009999", "#000099"), 
             repel = TRUE, 
             title = "")
