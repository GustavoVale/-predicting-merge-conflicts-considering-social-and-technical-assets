# DATABASE SEARCHES RELATED TO PROJECT METRICS

get.list.of.projects.metrics = function(mydb, project.id){
  #Query
  rs <- dbSendQuery(mydb, paste("SELECT * FROM project_metrics WHERE project_id=(", project.id, ") order by project_id"))
  #fetch query
  return(fetch(rs, n=-1))
}
