# install.packages("DBI")
# install.packages("ggplot2")
# install.packages("odbc")
# install.packages("RMariaDB")
# install.packages("RMySQL")
# install.packages("rapport")
# install.packages("UpSetR")
# install.packages("data.table")
# install.packages("networkD3")
# install.packages("dplyr")
# install.packages("ggpubr")

library("DBI")
library("RMySQL")
library("ggplot2")
library("RMariaDB")
library("dplyr")
library("ggpubr")

# database connection
source("1-1-database-connection.R")

# devs related
source("1-2-dao-devs.R")
source("1-3-dao-merge-scenario.R")
source("1-4-dao-project-metrics.R")

mydb <- get.database.connection.server() 

# PROJECTS SELECTED -> 66 projects -------------
target.projects <- c(
  2,
  5,
  6,
  7,
  8,
  9,
  10,
  11,
  12,
  13,
  14,
  15,
  16,
  17,
  18,
  19,
  21,
  23,
  24,
  25,
  28,
  29,
  30,
  31,
  32,
  33,
  36,
  40,
  42,
  43,
  44,
  45,
  46,
  48,
  50,
  52,
  54,
  55,
  57,
  59,
  63,
  66,
  68,
  70,
  71,
  72,
  76,
  77,
  78,
  79,
  80,
  81,
  84,
  85,
  87,
  88,
  89,
  90,
  94,
  95,
  96,
  99,
  101,
  102,
  103,
  105
)

# Creating data frames that we will use over the analysis --------------------------------

dev.list <- data.frame()
ms.metrics.by.project <- data.frame()

# Getting data frame of devs with full merge scenario information -------------------------------------------------------------------

for (project.id in target.projects) {
  aux.ms <- get.merge.scenarios.full.by.project(mydb, project.id)
  dev.list <- rbind(dev.list, aux.ms)
  print(project.id)
}

aux <- data.frame()

for (project.id in target.projects) {
  aux.ms <-
    get.number.of.merge.scenarios.by.project (mydb, project.id)
  aux.cms <-
    get.number.of.conflicting.merge.scenarios.by.project (mydb, project.id)
  aux.f <- get.number.of.files.by.project (mydb, project.id)
  aux.ch <- get.number.of.chunks.by.project (mydb, project.id)
  aux.data.frame <-
    data.frame(c(project.id), c(aux.ms), c(aux.cms), c(aux.f), c(aux.ch))
  colnames(aux.data.frame) <-
    c("pr.id",
      "number.ms",
      "number.cms",
      "number.files",
      "number.chunks")
  aux <- rbind(aux, aux.data.frame)
  print(project.id)
}

rm(aux.ms, aux.f, aux.ch)

#---------------------------------------------------------------------------------------------------------------------------

# Getting data frame of projectId and number of conflicting merge scenarios ------------------------------------------------

for (project.id in target.projects) {
  aux.ms <- get.list.of.projects.metrics(mydb, project.id)
  ms.metrics.by.project <- rbind(ms.metrics.by.project, aux.ms)
}

rm(aux.ms)

#---------------------------------------------------------------------------------------------------------------------------

# Getting the sum of merge scenarios and conflicting merge scenarios for all projects ---------------------------------------

sum.of.merge.scenarios <-
  as.numeric(nrow(subset(dev.list, !duplicated(ms_id))))

conflicting.merge.scenarios <- subset(dev.list, conflt > 0)
sum.of.conflicting.merge.scenarios <-
  as.numeric(nrow(subset(
    conflicting.merge.scenarios, !duplicated(ms_id)
  )))

rm(conflicting.merge.scenarios)

#---------------------------------------------------------------------------------------------------------------------------
# Saving generated dataframes ----------------------------------------------------------------------------------------------

write.csv(dev.list, file = "./CSVs/devList.csv")

write.csv(ms.metrics.by.project, file = "./CSVs/metricsByProject.csv")

print("FINISHED")

close.db.connection(mydb)