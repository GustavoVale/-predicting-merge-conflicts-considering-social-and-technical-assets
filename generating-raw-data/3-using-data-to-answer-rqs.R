source("3-1-classifying-devs-functions.R")

aux.data.frame <- read.csv(file = "./CSVs/ms-data.csv", header = TRUE)

rq1.1.table <- create.table.summary.cont.individually.at.project.level(aux.data.frame)
write.csv(rq1.1.table, file = "./CSVs/RQ1-1-results.csv")

project.chi.test <-
  chi.test.contributor.pair(nrow(subset(aux.data.frame, top_proj > 0)), 
                            nrow(subset(aux.data.frame, top_proj > 0 & has_conflict > 0)),
                            nrow(subset(aux.data.frame, occ_proj > 0)),
                            nrow(subset(aux.data.frame, occ_proj > 0 & has_conflict > 0))
                           )

project.chi.test_target <-
  chi.test.contributor.pair(nrow(subset(aux.data.frame, top_proj_target > 0)), 
                            nrow(subset(aux.data.frame, top_proj_target > 0 & has_conflict > 0)),
                            nrow(subset(aux.data.frame, occ_proj_target > 0)),
                            nrow(subset(aux.data.frame, occ_proj_target > 0 & has_conflict > 0))
  )

project.chi.test_source <-
  chi.test.contributor.pair(nrow(subset(aux.data.frame, top_proj_source > 0)), 
                            nrow(subset(aux.data.frame, top_proj_source > 0 & has_conflict > 0)),
                            nrow(subset(aux.data.frame, occ_proj_source > 0)),
                            nrow(subset(aux.data.frame, occ_proj_source > 0 & has_conflict > 0))
  )

project.chi.test <- rbind(project.chi.test, project.chi.test_target)
project.chi.test <- rbind(project.chi.test, project.chi.test_source)
write.csv(project.chi.test, file = "./CSVs/RQ1-1-chi-results.csv")

rq1.2.table <- create.table.summary.cont.individually.at.ms.level(aux.data.frame)
write.csv(rq1.2.table, file = "./CSVs/RQ1-2-results.csv")

ms.chi.test <-
  chi.test.contributor.pair(nrow(subset(aux.data.frame, top_ms > 0)), 
                            nrow(subset(aux.data.frame, top_ms > 0 & has_conflict > 0)),
                            nrow(subset(aux.data.frame, occ_ms > 0)),
                            nrow(subset(aux.data.frame, occ_ms > 0 & has_conflict > 0))
                           )

ms.chi.test_target <-
  chi.test.contributor.pair(nrow(subset(aux.data.frame, top_ms_target > 0)), 
                            nrow(subset(aux.data.frame, top_ms_target > 0 & has_conflict > 0)),
                            nrow(subset(aux.data.frame, occ_ms_target > 0)),
                            nrow(subset(aux.data.frame, occ_ms_target > 0 & has_conflict > 0))
  )

ms.chi.test_source <-
  chi.test.contributor.pair(nrow(subset(aux.data.frame, top_ms_source > 0)), 
                            nrow(subset(aux.data.frame, top_ms_source > 0 & has_conflict > 0)),
                            nrow(subset(aux.data.frame, occ_ms_source > 0)),
                            nrow(subset(aux.data.frame, occ_ms_source > 0 & has_conflict > 0))
  )

ms.chi.test <- rbind(ms.chi.test, ms.chi.test_target)
ms.chi.test <- rbind(ms.chi.test, ms.chi.test_source)
write.csv(ms.chi.test, file = "./CSVs/RQ1-2-chi-results.csv")


rq1.chi.test <-
  chi.test.contributor.4(nrow(subset(aux.data.frame, top_proj > 0)), 
                            nrow(subset(aux.data.frame, top_proj > 0 & has_conflict > 0)),
                            nrow(subset(aux.data.frame, occ_proj > 0)),
                            nrow(subset(aux.data.frame, occ_proj > 0 & has_conflict > 0)),
                            nrow(subset(aux.data.frame, top_ms > 0)), 
                            nrow(subset(aux.data.frame, top_ms > 0 & has_conflict > 0)),
                            nrow(subset(aux.data.frame, occ_ms > 0)),
                            nrow(subset(aux.data.frame, occ_ms > 0 & has_conflict > 0))
                         )
write.csv(rq1.chi.test, file = "./CSVs/RQ1-chi-results.csv")

rq2.table <- create.table.summary.cont.combining.at.project.and.ms.level(aux.data.frame)

write.csv(rq2.table, file = "./CSVs/RQ2-results.csv")

rq2.chi.test <-
  chi.test.contributor.4(nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0)), 
                         nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & has_conflict > 0)),
                         nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0)),
                         nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & has_conflict > 0)),
                         nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0)), 
                         nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & has_conflict > 0)),
                         nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0)),
                         nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & has_conflict > 0))
  )

rq2.chi.test_target <-
  chi.test.contributor.4(nrow(subset(aux.data.frame, top_proj_target > 0 & top_ms_target > 0)), 
                         nrow(subset(aux.data.frame, top_proj_target > 0 & top_ms_target > 0 & has_conflict > 0)),
                         nrow(subset(aux.data.frame, top_proj_target > 0 & occ_ms_target > 0)),
                         nrow(subset(aux.data.frame, top_proj_target > 0 & occ_ms_target > 0 & has_conflict > 0)),
                         nrow(subset(aux.data.frame, occ_proj_target > 0 & top_ms_target > 0)), 
                         nrow(subset(aux.data.frame, occ_proj_target > 0 & top_ms_target > 0 & has_conflict > 0)),
                         nrow(subset(aux.data.frame, occ_proj_target > 0 & occ_ms_target > 0)),
                         nrow(subset(aux.data.frame, occ_proj_target > 0 & occ_ms_target > 0 & has_conflict > 0))
  )

rq2.chi.test_source <-
  chi.test.contributor.4(nrow(subset(aux.data.frame, top_proj_source > 0 & top_ms_source > 0)), 
                         nrow(subset(aux.data.frame, top_proj_source > 0 & top_ms_source > 0 & has_conflict > 0)),
                         nrow(subset(aux.data.frame, top_proj_source > 0 & occ_ms_source > 0)),
                         nrow(subset(aux.data.frame, top_proj_source > 0 & occ_ms_source > 0 & has_conflict > 0)),
                         nrow(subset(aux.data.frame, occ_proj_source > 0 & top_ms_source > 0)), 
                         nrow(subset(aux.data.frame, occ_proj_source > 0 & top_ms_source > 0 & has_conflict > 0)),
                         nrow(subset(aux.data.frame, occ_proj_source > 0 & occ_ms_source > 0)),
                         nrow(subset(aux.data.frame, occ_proj_source > 0 & occ_ms_source > 0 & has_conflict > 0))
  )

rq2.chi.test <- rbind(rq2.chi.test, rq2.chi.test_target)
rq2.chi.test <- rbind(rq2.chi.test, rq2.chi.test_source)

write.csv(rq2.chi.test, file = "./CSVs/RQ2-chi-results.csv")

# source("3-2-running-machine-learning-techiniques.R")
