# DATABASE SEARCHES RELATED TO MERGE SCENARIOS

get.number.of.merge.scenarios.by.project = function(mydb, project.id){
  #Query
  rs <- dbSendQuery(mydb, paste("SELECT count(*) FROM merge_scenarios WHERE project_id=(", project.id, ")"))
  #fetch query
  fetch(rs, n=-1)
}

get.number.of.conflicting.merge.scenarios.by.project = function(mydb, project.id){
  #Query
  rs <- dbSendQuery(mydb, paste("SELECT count(*) FROM merge_scenarios WHERE project_id=(", project.id, ") and has_conflict=1"))
  #fetch query
  fetch(rs, n=-1)
}

get.number.of.files.by.project = function(mydb, project.id){
  #Query
  rs <- dbSendQuery(mydb, paste("SELECT count(distinct(filepath)) FROM merge_scenarios inner join files on merge_scenarios.id=files.merge_scenarios_id WHERE project_id=(", project.id, ")"))
  #fetch query
  fetch(rs, n=-1)
}

get.number.of.chunks.by.project = function(mydb, project.id){
  #Query
  rs <- dbSendQuery(mydb, paste("SELECT count(*) FROM merge_scenarios inner join files on merge_scenarios.id=files.merge_scenarios_id inner join chunks on chunks.file_id=files.id WHERE project_id=(", project.id, ")"))
  #fetch query
  fetch(rs, n=-1)
}
