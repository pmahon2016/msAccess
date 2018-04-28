import MySQLdb


db = MySQLdb.connect('localhost','pace', 'pace123', 'BMC')

cursor = db.cursor()

sqlfile = open('sqlinserts','r')
sqlmyinserts = sqlfile.read()

cursor.execute(sqlmyinserts)  