import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\BESLA\BESLA.accdb;')
#cursor = conn.cursor()

sqlDrop  = """

DROP TABLE BILLOFSALE;

"""

sqlstatement = """

CREATE TABLE BILLOFSALE (
        BOSNum autoincrement,
        VehicleIDNum varchar(50), 
        SalesID number,
        AutoCapacity number, 
        AutoColor varchar(50), 
        AutoCylinders number, 
        AutoMake varchar(50), 
        AutoModel varchar(50), 
        AutoRegistrationNumber number, 
        AutoSalePrice currency, 
        AutoStyle varchar(50), 
        AutoYear varchar(50), 
        CustID integer,
        CustomerAddress varchar(100), 
        CustomerCity varchar(50), 
        CustomerFinancing varchar(50), 
        DateOfSale varchar(50), 
        Dealer varchar(50) , 
        NumOfDoors number, 
        OdometerReading number, 
        ExtendedWarranty varchar(50),
        CONSTRAINT BOSNum_PK PRIMARY KEY(BOSNum),
        CONSTRAINT VehicleID_FK FOREIGN KEY (VehicleIDNum) REFERENCES AUTOINVENTORY(VehicleIDNum),
        CONSTRAINT Sales_FK  FOREIGN KEY (SalesID) REFERENCES SALESPERSON(SalesID),
        CONSTRAINT CustID_FK FOREIGN KEY (CustID) REFERENCES CUSTOMER(CustID),
        CONSTRAINT Dealer_FK FOREIGN KEY (Dealer) REFERENCES Dealership(DealershipName)
       
    );

"""


sqlInsert = """

        INSERT into BILLOFSALE (VehicleIDNum, SalesID, AutoCapacity, Autocolor, AutoCylinders, 
        AutoMake, AutoModel,AutoRegistrationNumber, AutoSalesPrice, AutoStyle, AutoYear, CustID, CustomerAddress,CustomerCity,CustomerFinancing, DateOfSale,Dealer,
        NumOfDoors, OdometerReading, ExtendedWarranty)


        Values('1HGC382633B504352', '1' , 6, 'Blue' ,6, 'Besla', 'Amp', 8777373, 
        54000, 'Sedan' ,'2018', 'John Blogs', '2 hometown road', 'Jersey City' , 'Belsa Financing',
        'Lease', 'April 09 2018','Belsa Motors' , 4 , 67 , 1000, 'no'); 
           
"""

sqlInsert1 = """
 
INSERT into BILLOFSALE Values('1JGC382633B504333', 'Slick Wilson' , 6, 'Pink' ,6, 'Besla',
'Amp', 8777373, 54000, 'Sedan' ,'2018', 'John Blogs', '2 hometown road', 'Jersey City' ,
'Belsa Financing', 'Lease', 'April 09 2018','Belsa Motors' , 4 , 67 , 1000, 'no'); 
    
"""
 

 



conn.execute(sqlDrop)
conn.execute(sqlstatement)
#===============================================================================
# conn.execute(sqlInsert)
# conn.execute(sqlInsert1)
#===============================================================================
#===============================================================================
# conn.execute(sqlInsert2)
# conn.execute(sqlInsert3)
# conn.execute(sqlInsert4)
#===============================================================================

conn.commit()