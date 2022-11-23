# Create summary table for top and occasional contributors INDIVIDUALLY at project-level
create.table.summary.cont.individually.at.project.level = function(aux.data.frame){
  table.contributor.at.level <-
    data.frame(
      "influencing factor" = c(
        "general",
        "general",
        "target",
        "target",
        "source",
        "source",
        "One",
        "One",
        "MoreThanOne",
        "MoreThanOne"
      ),
      "Role" = c(
        "top",
        "occasional",
        "top",
        "occasional",
        "top",
        "occasional",
        "top",
        "occasional",
        "top",
        "occasional"
      ), 
      
      "#MS" = c(
        nrow(subset(aux.data.frame, top_proj > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0)),
        nrow(subset(aux.data.frame, top_proj_target > 0)),
        nrow(subset(aux.data.frame, occ_proj_target > 0)),
        nrow(subset(aux.data.frame, top_proj_source > 0)),
        nrow(subset(aux.data.frame, occ_proj_source > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & devs == 1)),
        nrow(subset(aux.data.frame, occ_proj > 0 & devs == 1)),
        nrow(subset(aux.data.frame, top_proj > 0 & devs > 1)),
        nrow(subset(aux.data.frame, occ_proj > 0 & devs > 1))
      ),
      "#CMS" = c(
        nrow(subset(aux.data.frame, top_proj > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj_target > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj_target > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj_source > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj_source > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & devs == 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & devs == 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & devs > 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & devs > 1 & has_conflict > 0))
      ), 
      "#CMS by #MS" = c(
        (nrow(subset(aux.data.frame, top_proj > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj > 0)),
        (nrow(subset(aux.data.frame, occ_proj > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj > 0)),
        (nrow(subset(aux.data.frame, top_proj_target > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj_target > 0)),
        (nrow(subset(aux.data.frame, occ_proj_target > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj_target > 0)),
        (nrow(subset(aux.data.frame, top_proj_source > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj_source > 0)),
        (nrow(subset(aux.data.frame, occ_proj_source > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj_source > 0)),
        (nrow(subset(aux.data.frame, top_proj > 0 & devs == 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj > 0 & devs == 1)),
        (nrow(subset(aux.data.frame, occ_proj > 0 & devs == 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj > 0 & devs == 1)),
        (nrow(subset(aux.data.frame, top_proj > 0 & devs > 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj > 0 & devs > 1)),
        (nrow(subset(aux.data.frame, occ_proj > 0 & devs > 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj > 0 & devs > 1))
      )
    )
  
  return(table.contributor.at.level)
}

# Create summary table for top and occasional contributors INDIVIDUALLY at branch-level
create.table.summary.cont.individually.at.ms.level = function(aux.data.frame){
  table.contributor.at.level <-
    data.frame(
      "influencing factor" = c(
        "general",
        "general",
        "target",
        "target",
        "source",
        "source",
        "One",
        "One",
        "MoreThanOne",
        "MoreThanOne"
      ),
      "Role" = c(
        "top",
        "occasional",
        "top",
        "occasional",
        "top",
        "occasional",
        "top",
        "occasional",
        "top",
        "occasional"
      ), 
      
      "#MS" = c(
        nrow(subset(aux.data.frame, top_ms > 0)),
        nrow(subset(aux.data.frame, occ_ms > 0)),
        nrow(subset(aux.data.frame, top_ms_target > 0)),
        nrow(subset(aux.data.frame, occ_ms_target > 0)),
        nrow(subset(aux.data.frame, top_ms_source > 0)),
        nrow(subset(aux.data.frame, occ_ms_source > 0)),
        nrow(subset(aux.data.frame, top_ms > 0 & devs == 1)),
        nrow(subset(aux.data.frame, occ_ms > 0 & devs == 1)),
        nrow(subset(aux.data.frame, top_ms > 0 & devs > 1)),
        nrow(subset(aux.data.frame, occ_ms > 0 & devs > 1))
      ),
      "#CMS" = c(
        nrow(subset(aux.data.frame, top_ms > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_ms > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_ms_target > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_ms_target > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_ms_source > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_ms_source > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_ms > 0 & devs == 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_ms > 0 & devs == 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_ms > 0 & devs > 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_ms > 0 & devs > 1 & has_conflict > 0))
      ), 
      "#CMS by #MS" = c(
        (nrow(subset(aux.data.frame, top_ms > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_ms > 0)),
        (nrow(subset(aux.data.frame, occ_ms > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_ms > 0)),
        (nrow(subset(aux.data.frame, top_ms_target > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_ms_target > 0)),
        (nrow(subset(aux.data.frame, occ_ms_target > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_ms_target > 0)),
        (nrow(subset(aux.data.frame, top_ms_source > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_ms_source > 0)),
        (nrow(subset(aux.data.frame, occ_ms_source > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_ms_source > 0)),
        (nrow(subset(aux.data.frame, top_ms > 0 & devs == 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_ms > 0 & devs == 1)),
        (nrow(subset(aux.data.frame, occ_ms > 0 & devs == 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_ms > 0 & devs == 1)),
        (nrow(subset(aux.data.frame, top_ms > 0 & devs > 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_ms > 0 & devs > 1)),
        (nrow(subset(aux.data.frame, occ_ms > 0 & devs > 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_ms > 0 & devs > 1))
      )
    )
  
  return(table.contributor.at.level)
}

# Create summary table for top and occasional contributors COMBINING project-level and ms-level
create.table.summary.cont.combining.at.project.and.ms.level = function(aux.data.frame){
  table.contributor.at.level <-
    data.frame(
      "influencing factor" = c(
        "general",
        "general",
        "general",
        "general",
        "target",
        "target",
        "target",
        "target",
        "source",
        "source",
        "source",
        "source",
        "One",
        "One",
        "One",
        "One",
        "MoreThanOne",
        "MoreThanOne",
        "MoreThanOne",
        "MoreThanOne"
      ),
      "Role" = c(
        "top-top",
        "top-occ",
        "occ-top",
        "occ-occ",
        "top-top",
        "top-occ",
        "occ-top",
        "occ-occ",
        "top-top",
        "top-occ",
        "occ-top",
        "occ-occ",
        "top-top",
        "top-occ",
        "occ-top",
        "occ-occ",
        "top-top",
        "top-occ",
        "occ-top",
        "occ-occ"
      ), 
      
      "#MS" = c(
        nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0)),
        nrow(subset(aux.data.frame, top_proj_target > 0 & top_ms_target > 0)),
        nrow(subset(aux.data.frame, top_proj_target > 0 & occ_ms_target > 0)),
        nrow(subset(aux.data.frame, occ_proj_target > 0 & top_ms_target > 0)),
        nrow(subset(aux.data.frame, occ_proj_target > 0 & occ_ms_target > 0)),
        nrow(subset(aux.data.frame, top_proj_source > 0 & top_ms_source > 0)),
        nrow(subset(aux.data.frame, top_proj_source > 0 & occ_ms_source > 0)),
        nrow(subset(aux.data.frame, occ_proj_source > 0 & top_ms_source > 0)),
        nrow(subset(aux.data.frame, occ_proj_source > 0 & occ_ms_source > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & devs == 1)),
        nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & devs == 1)),
        nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & devs == 1)),
        nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & devs == 1)),
        nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & devs > 1)),
        nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & devs > 1)),
        nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & devs > 1)),
        nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & devs > 1))
      ),
      "#CMS" = c(
        nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj_target > 0 & top_ms_target > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj_target > 0 & occ_ms_target > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj_target > 0 & top_ms_target > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj_target > 0 & occ_ms_target > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj_source > 0 & top_ms_source > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj_source > 0 & occ_ms_source > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj_source > 0 & top_ms_source > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj_source > 0 & occ_ms_source > 0 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & devs == 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & devs == 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & devs == 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & devs == 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & devs > 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & devs > 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & devs > 1 & has_conflict > 0)),
        nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & devs > 1 & has_conflict > 0))
      ), 
      "#CMS by #MS" = c(
        (nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0)),
        (nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0)),
        (nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0)),
        (nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0)),
        (nrow(subset(aux.data.frame, top_proj_target > 0 & top_ms_target > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj_target > 0 & top_ms_target > 0)),
        (nrow(subset(aux.data.frame, top_proj_target > 0 & occ_ms_target > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj_target > 0 & occ_ms_target > 0)),
        (nrow(subset(aux.data.frame, occ_proj_target > 0 & top_ms_target > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj_target > 0 & top_ms_target > 0)),
        (nrow(subset(aux.data.frame, occ_proj_target > 0 & occ_ms_target > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj_target > 0 & occ_ms_target > 0)),
        (nrow(subset(aux.data.frame, top_proj_source > 0 & top_ms_source > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj_source > 0 & top_ms_source > 0)),
        (nrow(subset(aux.data.frame, top_proj_source > 0 & occ_ms_source > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj_source > 0 & occ_ms_source > 0)),
        (nrow(subset(aux.data.frame, occ_proj_source > 0 & top_ms_source > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj_source > 0 & top_ms_source > 0)),
        (nrow(subset(aux.data.frame, occ_proj_source > 0 & occ_ms_source > 0 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj_source > 0 & occ_ms_source > 0)),
        (nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & devs == 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & devs == 1)),
        (nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & devs == 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & devs == 1)),
        (nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & devs == 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & devs == 1)),
        (nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & devs == 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & devs == 1)),
        (nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & devs > 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj > 0 & top_ms > 0 & devs > 1)),
        (nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & devs > 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, top_proj > 0 & occ_ms > 0 & devs > 1)),
        (nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & devs > 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj > 0 & top_ms > 0 & devs > 1)),
        (nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & devs > 1 & has_conflict > 0)) * 100) / nrow(subset(aux.data.frame, occ_proj > 0 & occ_ms > 0 & devs > 1))
      )
    )
  
  return(table.contributor.at.level)
}

# Computing chi-square for pair of developer roles -----------------------------------------------------------------------
chi.test.contributor.pair = function(value1, value1.conflict, value2, value2.conflict){
  
  table.chi <- matrix(
    c(
      value1,
      value1.conflict,
      value2,
      value2.conflict
    ),
    ncol = 2,
    byrow = TRUE
  )
  
  colnames(table.chi) <- c("#MS", "#CMS")
  rownames(table.chi) <- c("top", "occ")
  
  result.general.ms <- chisq.test(table.chi, correct = T)
  print(result.general.ms)
  
  # creating chi-test summary table
  chi.test.summary <-
    data.frame(
      "x-squared" = result.general.ms$statistic,
      "parameter" = result.general.ms$parameter,
      "p.value" = result.general.ms$p.value
    )
  return(chi.test.summary)
}

# Computing chi-square for pair of developer roles -----------------------------------------------------------------------
chi.test.contributor.4 = function(value1, value1.conflict, value2, value2.conflict, value3, value3.conflict, value4, value4.conflict){
  
  table.chi <- matrix(
    c(
      value1,
      value1.conflict,
      value2,
      value2.conflict,
      value3, 
      value3.conflict,
      value4,
      value4.conflict
    ),
    ncol = 2,
    byrow = TRUE
  )
  
  colnames(table.chi) <- c("#MS", "#CMS")
  rownames(table.chi) <- c("top_proj", "occ_proj", "top_ms", "occ_ms")
  
  result.general.ms <- chisq.test(table.chi, correct = T)
  print(result.general.ms)
  # creating chi-test summary table
  chi.test.summary <-
    data.frame(
      "x-squared" = result.general.ms$statistic,
      "parameter" = result.general.ms$parameter,
      "p.value" = result.general.ms$p.value
    )
  return(chi.test.summary)
}
