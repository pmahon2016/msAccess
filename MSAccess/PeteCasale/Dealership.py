import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\BESLA\BESLA.accdb;')
#cursor = conn.cursor()

sqlDrop  = """

DROP TABLE DEALERSHIP;

"""

sqlstatement = """

    CREATE TABLE DEALERSHIP (
        DealershipName varchar(50) PRIMARY KEY, 
        Owner varchar(50),   
        DealerFinancing varchar(50), 
        LicenseNum number,
        AutoMake varchar(50), 
        NumModels varchar(50),
        DealershipStreet varchar(50),
        DealershipCity varchar(50),
        DealershipState varchar(20),
        DealershipZip number
        
        );

"""


sqlInsert = """

INSERT into DEALERSHIP (DealershipName,Owner,DealerFinancing,LicenseNuM,AutoMake,
NumModels,DealershipStreet,DealershipCity,DealershipState,DealershipZip)

Values('Besla Motors', 'Besla Inc.', 'Besla Financing', 873455, 'Besla',4, '20 Chestnut Drive', 'Detroit','MI',10988 ); 
   
"""


 

 



conn.execute(sqlDrop)
conn.execute(sqlstatement)
#conn.execute(sqlInsert)
#conn.execute(sqlInsert1)
#===============================================================================
# conn.execute(sqlInsert2)
# conn.execute(sqlInsert3)
# conn.execute(sqlInsert4)
#===============================================================================

conn.commit()