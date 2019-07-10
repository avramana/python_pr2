import sqlitefile as sqlitedb


sqldb = sqlitedb.DBOperations()

sqldb.create_Table()
print("before")
print(sqldb.fetch_Data())
sqldb.insert_Data("abc",100,25.0)
sqldb.insert_Data("efg",10,12.0)
sqldb.insert_Data("klm",20,23.0)
sqldb.insert_Data("xyz",35,56.0)
print("after")
print(sqldb.fetch_Data())
