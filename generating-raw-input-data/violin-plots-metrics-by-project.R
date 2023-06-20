install.packages("ggplot2")

library(ggplot2)

df <- read.csv(file = "./CSVs/metricsByProject.csv", header = TRUE)

# testing
boxplot(df$ms_computed, col = "white", names = "scenarios")
median(df$ms_computed)
sd(df$ms_computed)


# Code to generate 6 box-plots together
par(mfrow=c(1,6))
boxplot(df$ms_computed, col = "white")
boxplot(df$ms_conflicted, col = "white")
boxplot(df$number_of_files, col = "white")
boxplot(df$number_of_chunks, col = "white")
boxplot(df$number_of_commits, col = "white")
boxplot(df$number_of_developers, col = "white")

