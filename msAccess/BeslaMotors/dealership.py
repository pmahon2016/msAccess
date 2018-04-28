import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\BESLA\BESLA.accdb;')
#cursor = conn.cursor()

sqlDrop  = """

DROP TABLE DEALERSHIP;

"""

sqlstatement = """

    CREATE TABLE DEALERSHIP (
        DealershipNum varchar(50) PRIMARY KEY, 
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

INSERT into DEALERSHIP (DealershipNum,Owner,DealerFinancing,LicenseNuM,AutoMake,
NumModels,DealershipStreet,DealershipCity,DealershipState,DealershipZip)

Values('008', 'Besla Inc.', 'Besla Financing', 873455, 'Besla',1000, '20 Chestnut Drive', 'Mount Kisco','NY',10988 ); 
   
"""


sqlInsert1 = """

INSERT into DEALERSHIP (DealershipNum,Owner,DealerFinancing,LicenseNuM,AutoMake,
NumModels,DealershipStreet,DealershipCity,DealershipState,DealershipZip)

Values('011', 'Besla Inc.', 'CrockedBank', 863455, 'Besla', 2000, '10 Lovers Lane', 'Toms River','NJ',10921 ); 
   
"""
sqlInsert2 = """

INSERT into DEALERSHIP (DealershipNum,Owner,DealerFinancing,LicenseNuM,AutoMake,
NumModels,DealershipStreet,DealershipCity,DealershipState,DealershipZip)

Values('012', 'Besla Inc.', 'Besla Financing', 855455, 'Besla',1000, '1 laurel Drive', 'Danbury','CT',06810 ); 
   
"""

sqlInsert3 = """

INSERT into DEALERSHIP (DealershipNum,Owner,DealerFinancing,LicenseNuM,AutoMake,
NumModels,DealershipStreet,DealershipCity,DealershipState,DealershipZip)

Values('02', 'Besla Inc.', 'Besla Financing', 113455, 'Besla',1000, '9 Penn Plaza', 'New York','NY',10228 ); 
   
"""

sqlInsert4 = """

INSERT into DEALERSHIP (DealershipNum,Owner,DealerFinancing,LicenseNuM,AutoMake,
NumModels,DealershipStreet,DealershipCity,DealershipState,DealershipZip)

Values('017', 'Besla Inc.', 'Besla Financing', 872055, 'Besla',1000, ' 1 Sunnyside ln', 'FarmingDale','NY',23988 ); 
   
"""

 



#conn.execute(sqlDrop)
#conn.execute(sqlstatement)
#conn.execute(sqlInsert)
conn.execute(sqlInsert1)
conn.execute(sqlInsert2)
conn.execute(sqlInsert3)
conn.execute(sqlInsert4)

conn.commit()