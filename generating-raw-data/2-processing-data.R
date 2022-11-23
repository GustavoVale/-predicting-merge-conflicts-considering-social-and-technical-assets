library("dplyr")
library("ggpubr")

initial.data <- read.csv(file = "./CSVs/devList.csv", header = TRUE)

ms.data <- distinct(initial.data, ms_id, .keep_all = TRUE)
ms.data <- ms.data[, c(1:2)]
ms.data$has_conflict <- 0
ms.data$top_proj <- 0
ms.data$top_proj_target <- 0
ms.data$top_proj_source <- 0
ms.data$occ_proj <- 0
ms.data$occ_proj_target <- 0
ms.data$occ_proj_source <- 0
ms.data$top_ms <- 0
ms.data$top_ms_target <- 0
ms.data$top_ms_source <- 0
ms.data$occ_ms <- 0
ms.data$occ_ms_target <- 0
ms.data$occ_ms_source <- 0
ms.data$devs <- 0
ms.data$devs_target <- 0
ms.data$devs_source <- 0
ms.data$devs_both <- 0
ms.data$files <- 0
ms.data$files_target <- 0
ms.data$files_source <- 0
ms.data$files_both <- 0
ms.data$chunks <- 0
ms.data$chunks_target <- 0
ms.data$chunks_source <- 0
ms.data$loc <- 0
ms.data$loc_target <- 0
ms.data$loc_source <- 0
ms.data$commits <- 0
ms.data$commits_target <- 0
ms.data$commits_source <- 0

current.ms.data <- subset(initial.data, ms_id == ms.data$ms_id[18])

for (row in 1:nrow(ms.data)) {
  current.ms.data <- subset(initial.data, ms_id == ms.data$ms_id[row])
  
  # getting total loc and computing pareto for merge scenario level
  threshold_loc_target <- sum(current.ms.data$loc_l) * 0.8
  threshold_loc_source <- sum(current.ms.data$loc_r) * 0.8
  
  has_conflict <- if (sum(current.ms.data$has_conflict) > 0) 1 else 0
  
  #aux variables
  num_top_proj  <- 0
  num_top_proj_target <- 0
  num_top_proj_source <- 0
  num_occ_proj  <- 0
  num_occ_proj_target <- 0
  num_occ_proj_source <- 0
  num_top_ms  <- 0
  num_top_ms_target <- 0
  num_top_ms_source <- 0
  num_occ_ms  <- 0
  num_occ_ms_target <- 0
  num_occ_ms_source  <- 0
  
  devs <- current.ms.data$t_dev[1]
  devs_target <- current.ms.data$t_l_d[1]
  devs_source <- current.ms.data$t_r_d[1]
  devs_both <- current.ms.data$t_both_d[1]
  files <- current.ms.data$t_f[1]
  files_target <- current.ms.data$tlf[1]
  files_source <- current.ms.data$trf[1]
  files_both <- current.ms.data$t_bsf[1]
  chunks <- current.ms.data$t_ch[1]
  chunks_target <- current.ms.data$tlch[1]
  chunks_source <- current.ms.data$trch[1]
  loc <- current.ms.data$code_churn[1]
  loc_target <- sum(current.ms.data$loc_l)
  loc_source <- sum(current.ms.data$loc_r)
  commits <- current.ms.data$t_commits[1]
  commits_target <- current.ms.data$t_lcommits[1]
  commits_source <- current.ms.data$t_rcommits[1]
 
  for (row2 in 1:nrow(current.ms.data)) {
    
    # adding data for top and occ at project-level
    if (current.ms.data$core[row2] == 1) {
      num_top_proj <- num_top_proj + 1
      
      if (current.ms.data$ch_l[row2] > 0) {
        num_top_proj_target <- num_top_proj_target + 1
      }
      
      if (current.ms.data$ch_r[row2] > 0) {
        num_top_proj_source <- num_top_proj_source + 1
      }

    } else {
      num_occ_proj <- num_occ_proj + 1

      if (current.ms.data$ch_l[row2] > 0) {
        num_occ_proj_target <- num_occ_proj_target + 1
      }
      
      if (current.ms.data$ch_r[row2] > 0) {
        num_occ_proj_source <- num_occ_proj_source + 1
      }
    }
    
    # adding data for top and occ at merge-scenario-level
    if (current.ms.data$loc_l[row2] >= threshold_loc_target |
        current.ms.data$loc_r[row2] >= threshold_loc_source) {
      num_top_ms <- num_top_ms + 1
      
      if (current.ms.data$loc_l[row2] >= threshold_loc_target) {
        num_top_ms_target <- num_top_ms_target + 1
      }
      
      if (current.ms.data$loc_r[row2] <= threshold_loc_source) {
        num_top_ms_source <- num_top_ms_source + 1
      }
      
    } else {
      num_occ_ms <- num_occ_ms + 1
      
      if (current.ms.data$ch_l[row2] > 0) {
        num_occ_ms_target <- num_occ_ms_target + 1
      } else {
        num_occ_ms_source <- num_occ_ms_source + 1
      }
    }
  }
  
  ms.data$has_conflict[row] <- has_conflict
  ms.data$top_proj[row] <- num_top_proj
  ms.data$top_proj_target[row] <- num_top_proj_target
  ms.data$top_proj_source[row] <- num_top_proj_source
  ms.data$occ_proj[row] <- num_occ_proj
  ms.data$occ_proj_target[row] <- num_occ_proj_target
  ms.data$occ_proj_source[row] <- num_occ_proj_source
  ms.data$top_ms[row] <- num_top_ms
  ms.data$top_ms_target[row] <- num_top_ms_target
  ms.data$top_ms_source[row] <- num_top_ms_source
  ms.data$occ_ms[row] <- num_occ_ms
  ms.data$occ_ms_target[row] <- num_occ_ms_target
  ms.data$occ_ms_source[row] <- num_occ_ms_source
  ms.data$devs[row] <- devs
  ms.data$devs_target[row] <- devs_target
  ms.data$devs_source[row] <- devs_source
  ms.data$devs_both[row] <- devs_both
  ms.data$files[row] <- files
  ms.data$files_target[row] <- files_target
  ms.data$files_source[row] <- files_source
  ms.data$files_both[row] <- files_both
  ms.data$chunks[row] <- chunks
  ms.data$chunks_target[row] <- chunks_target
  ms.data$chunks_source[row] <- chunks_source
  ms.data$loc[row] <- loc
  ms.data$loc_target[row] <- loc_target
  ms.data$loc_source[row] <- loc_source
  ms.data$commits[row] <- commits
  ms.data$commits_target[row] <- commits_target
  ms.data$commits_source[row] <- commits_source
  
}

# remove aux variables

rm(
  current.ms.data,
  
  has_conflict,
  
  num_top_proj,
  num_top_proj_target,
  num_top_proj_source,
  num_occ_proj,
  num_occ_proj_target,
  num_occ_proj_source,
  num_top_ms,
  num_top_ms_target,
  num_top_ms_source,
  num_occ_ms,
  num_occ_ms_target,
  num_occ_ms_source,
  
  devs,
  devs_target,
  devs_source,
  devs_both,
  files,
  files_target,
  files_source,
  files_both,
  chunks,
  chunks_target,
  chunks_source,
  loc,
  loc_target,
  loc_source,
  commits,
  commits_target,
  commits_source,
  
  threshold_loc_source,
  threshold_loc_target,
  
  row,
  row2
)

write.csv(ms.data, file = "./CSVs/ms-data.csv")
