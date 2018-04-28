import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\BESLA\BESLA.accdb;')


SqlQuery = """

select * from AUTOINVENTORY; 

"""


conn.execute(SqlQuery)

conn.commit()
