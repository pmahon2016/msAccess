import MySQLdb

db = MySQLdb.connect('localhost','pace', 'pace123', 'BMC')

cursor = db.cursor()

sqlfile = open('tables','r')
sqltbl = sqlfile.read()

cursor.execute(sqltbl)




