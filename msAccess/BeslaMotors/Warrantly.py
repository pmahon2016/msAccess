import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\BESLA\BESLA.accdb;')
#cursor = conn.cursor()

sqlDrop  = """

DROP TABLE DEALERSHIP;

"""

sqlstatement = """

    CREATE TABLE WARRANTY (
        VehicleIDNum varchar(50),
        CustID integer,
        WarrantyNum varchar(50),
        BeginDate varchar(10),
        EndDate varchar(10),
        Underwriter varchar(20),
        PRIMARY KEY (VehicleIDNum,CustID, WarrantyNum),
        CONSTRAINT Cust_FK FOREIGN KEY (CustID) REFERENCES CUSTOMER(CustID),
        CONSTRAINT VInID_FK FOREIGN KEY (VehicleIDNum) REFERENCES AUTOINVENTORY(VehicleIDNum),
        CONSTRAINT CustID_FK FOREIGN KEY (CustID) REFERENCES CUSTOMER(CustID)
        );

"""


sqlInsert = """
 
INSERT into WARRANTY (CustID,WarrantyNum ,BeginDate,EndDate,Underwriter)

Values (1, '8736252', 'March 7, 2018', 'March 7, 2021', 'Belsa Motors' )


    
"""

 

 



#conn.execute(sqlDrop)
#conn.execute(sqlstatement)
conn.execute(sqlInsert)
#conn.execute(sqlInsert1)
#===============================================================================
# conn.execute(sqlInsert2)
# conn.execute(sqlInsert3)
# conn.execute(sqlInsert4)
#===============================================================================

conn.commit()