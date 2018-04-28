import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\BESLA\BESLA.accdb;')
#cursor = conn.cursor()

sqlDrop  = """

DROP TABLE SALESPERSON;

"""

sqlstatement = """

    CREATE TABLE SALESPERSON (
            SalesID number,
            SalesPersonFName varchar(50),
            SalesPersonLName varchar(50), 
            SalesPersonPhone number,
            SalesPersonEmailAddress varchar(50),
            SalesSpeciality varchar(50), 
            Availability varchar(50),
            SalesPersonMonthlyDraw currency,
            TaxNumber number,
            CONSTRAINT SalesID_PK PRIMARY KEY (SalesID)
            );
    
    """



sqlInsert = """

INSERT into SALESPERSON (SalesID, SalesPersonFName,SalesPersonLName, SalesPersonPhone, 
SalesPersonEmailAddress,  SalesSpeciality, Availability,SalesPersonMonthlyDraw, TaxNumber) 

Values ( 001, 'Charlie', 'Pride',9143489122, 'cpride@besla.com', 'Sports Cars' , 'TWTFSat',2000, 873366344 ); 
   
"""

sqlInsert1 = """

INSERT into SALESPERSON (SalesID, SalesPersonFName,SalesPersonLName, SalesPersonPhone, 
SalesPersonEmailAddress,  SalesSpeciality, Availability,SalesPersonMonthlyDraw, TaxNumber) 

Values ( 004, 'Miles', 'Tobin',9143489121, 'mtobin@besla.com', 'Family Cars' , 'WTFSatSun',2000, 833366344 ); 
   
"""
 
sqlInsert2 = """

INSERT into SALESPERSON (SalesID, SalesPersonFName,SalesPersonLName, SalesPersonPhone, 
SalesPersonEmailAddress,  SalesSpeciality, Availability,SalesPersonMonthlyDraw, TaxNumber) 

Values ( 0088, 'Saul', 'Greenberg',9143489122, 'sgreen@besla.com', 'Sales Manager' , 'WTFSatSun',4000, 8743366344 ); 
   
"""

sqlInsert3 = """

INSERT into SALESPERSON (SalesID, SalesPersonFName,SalesPersonLName, SalesPersonPhone, 
SalesPersonEmailAddress,  SalesSpeciality, Availability,SalesPersonMonthlyDraw, TaxNumber) 

Values ( 009, 'Ron', 'Gibbs',9143487722, 'ronny@besla.com', 'Economy Cars' , 'TWTFSat',2000, 873332344 ); 
   
"""


sqlInsert4 = """

INSERT into SALESPERSON (SalesID, SalesPersonFName,SalesPersonLName, SalesPersonPhone, 
SalesPersonEmailAddress,  SalesSpeciality, Availability,SalesPersonMonthlyDraw, TaxNumber) 

Values ( 044, 'Linda', 'Mann', 9143482322, 'lmann@besla.com', 'SuV' , 'MWTFSat',2000, 4433625244 ); 
   
"""

#conn.execute(sqlDrop)
#conn.execute(sqlstatement)
#conn.execute(sqlInsert)
#conn.execute(sqlInsert1)
#===============================================================================
conn.execute(sqlInsert2)
conn.execute(sqlInsert3)
conn.execute(sqlInsert4)
#===============================================================================

conn.commit()