# DATABASE SEARCHES RELATED TO DEVS

# Get full information about devs with some information about the ms aggregated
get.merge.scenarios.full.by.project = function(mydb,
                                               project.id) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT devs.id, merge_scenarios.project_id as pr_id, devs.merge_scenario_id as ms_id, contributor_id as cont_id, 
        number_files_left as fi_l, number_files_right as fi_r, number_chunks_left as ch_l, number_chunks_right as ch_r, 
        number_changed_lines_left as loc_l, number_changed_lines_right as loc_r, number_commits_left as commits_l, number_commits_right as commits_r,
        last_change_left as last_l, last_change_right as last_r, is_integrator as intg, contribute_conflict as conflt, 
        is_core_dev as core, is_left_branch_leader as l_lead, is_right_branch_leader as r_lead, 
        number_of_files as t_f, number_conflicted_files as t_conff, number_left_files as tlf, number_right_files as trf, number_both_side_files as t_bsf,
        number_chunks as t_ch, number_conflicted_chunks as t_cch, number_left_chunks as tlch, number_right_chunks as trch, 
        number_commits as t_commits, number_left_commits as t_lcommits, number_right_commits as t_rcommits,
        number_developers as t_dev, number_left_dev as t_l_d, number_right_dev as t_r_d, number_both_side_dev as t_both_d,
        code_churn, conflict_code_churn as conf_loc, merge_scenarios.has_conflict
        from devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id inner join ms_metrics on 
        ms_metrics.merge_scenario_id=merge_scenarios.id where project_id=(",
        project.id,
        ") AND (devs.number_chunks_left>0 OR devs.number_chunks_right>0)"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# ative core or peripheral
get.number.of.merge.scenarios.core.devs.contributed.by.project = function(mydb,
                                                                          project.id,
                                                                          is.core) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT count(distinct(merge_scenarios.id)) FROM devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND devs.is_core_dev=(",
        is.core,
        ") AND (number_chunks_left>0 OR number_chunks_right>0)"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# ative conflicting core or peripheral
get.number.of.merge.scenarios.core.and.conflicting.devs.contributed.by.project = function(mydb,
                                                                          project.id,
                                                                          is.core,
                                                                          contribute.conflict) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT count(distinct(merge_scenarios.id)) FROM devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND devs.is_core_dev=(",
        is.core,
        ") AND (number_chunks_left>0 OR number_chunks_right>0) AND contribute_conflict=(",
        contribute.conflict,
        ")"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# ative left side
get.number.of.merge.scenarios.left.leader.contributed.by.project = function(mydb,
                                                                            project.id,
                                                                            left.leader,
                                                                            contribute.conflict) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT distinct(merge_scenarios.id) FROM devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND devs.is_left_branch_leader=(",
        left.leader,
        ") AND number_chunks_left>0 AND contribute_conflict=(",
        contribute.conflict,
        ")"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# ative right side
get.number.of.merge.scenarios.right.leader.contributed.by.project = function(mydb,
                                                                            project.id,
                                                                            right.leader,
                                                                            contribute.conflict) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT distinct(merge_scenarios.id) FROM devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND devs.is_right_branch_leader=(",
        right.leader,
        ") AND number_chunks_right>0 AND contribute_conflict=(",
        contribute.conflict,
        ")"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# last dev left
get.number.of.merge.scenarios.last.dev.left.contributed.by.project = function(mydb,
                                                                             project.id,
                                                                             last.left,
                                                                             contribute.conflict) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT distinct(merge_scenarios.id) FROM devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND devs.last_change_left=(",
        last.left,
        ") AND number_chunks_left>0 AND contribute_conflict=(",
        contribute.conflict,
        ")"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# last dev right
get.number.of.merge.scenarios.last.dev.right.contributed.by.project = function(mydb,
                                                                              project.id,
                                                                              last.right,
                                                                              contribute.conflict) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT distinct(merge_scenarios.id) FROM devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND devs.last_change_right=(",
        last.right,
        ") AND number_chunks_right>0 AND contribute_conflict=(",
        contribute.conflict,
        ")"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# number of merge scenarios contributors
get.number.merge.scenarios.contributors.by.project = function(mydb,
                                                       project.id) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT count(distinct(devs.contributor_id)) FROM devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND (number_chunks_left>0 OR number_chunks_right>0)"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# number of merge scenarios contributors that conflicted
get.number.merge.scenarios.contributors.that.participate.conflict.by.project = function(mydb,
                                                       project.id) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT count(distinct(devs.contributor_id)) FROM devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND (number_chunks_left>0 OR number_chunks_right>0) AND contribute_conflict=1"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# merge scenarios contributors that conflicted
get.merge.scenarios.contributors.that.participate.conflict.by.project = function(mydb,
                                                                                 project.id) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT devs.contributor_id, project_id FROM devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND (number_chunks_left>0 OR number_chunks_right>0) AND contribute_conflict=1 order by project_id, contributor_id"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}

# Get information about devs and merge scenarios 
get.devs.and.merge.scenarios.by.project = function(mydb,
                                               project.id) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT merge_scenarios.project_id as pr_id, devs.merge_scenario_id as ms_id, contributor_id as cont_id, 
        merge_commit_date from devs inner join merge_scenarios on merge_scenarios.id=devs.merge_scenario_id where project_id=(",
        project.id,
        ") AND is_core_dev=1" 
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}


# number of merge scenarios of a specific contributor by project
get.number.merge.scenarios.of.specific.contributor.by.project = function(mydb, contributor.id,
                                                              project.id) {
  #Query
  rs <-
    dbSendQuery(
      mydb,
      paste(
        "SELECT count(*) FROM merge_scenarios inner join committers on merge_scenarios.id=committers.merge_scenario_id WHERE project_id=(",
        project.id,
        ") AND contributor_id=(",
        contributor.id,
        ")"
      )
    )
  #fetch query
  return(fetch(rs, n = -1))
}
