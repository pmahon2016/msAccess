import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\HSD\HSD.accdb;')
cursor = conn.cursor()

sql = """



"""

cursor.execute(sql)

conn.commit()