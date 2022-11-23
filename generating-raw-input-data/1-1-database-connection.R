#OPENING AND CLOSING DATABASE CONNECTION -------------------------------------------------------------

#db Connection
get.database.connection.server = function(){
  # all data to connect to the database should be in the cnf.file
  mycnf= "./cnf.file"
  dbConnect(default.file=mycnf, unix.socket="/var/run/mysqld/mysqld.sock") 
  
}

#db Disconnection
close.db.connection = function(mydb){
  dbDisconnect(mydb)  
}
