import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\BESLA\BESLA.accdb;')
#cursor = conn.cursor()

sqlDrop  = """

DROP TABLE AUTOINVENTORY

"""

sqlstatement = """

CREATE TABLE AUTOINVENTORY (
        VehicleIDNum varchar(50), 
        AutoCapacity number, 
        AutoColor varchar(50), 
        AutoCylinders number,  
        AutoListPrice currency, 
        AutoMake varchar(50), 
        AutoMilageAtDelivery number, 
        AutoModel varchar(50), 
        AutoOptions varchar(150),  
        AutoCost currency, 
        AutoStyle varchar(50), 
        AutoWeight varchar(50), 
        AutoYear varchar(50), 
        DateofDelivery varchar(50), 
        DateofManufacture varchar(50), 
        DealershipNum varchar(50), 
        NumOfDoors number, 
        OdometerReading number, 
        PlaceOfManufacture varchar(100),
        PRIMARY KEY (VehicleIDNum),
        CONSTRAINT dealership_FK FOREIGN KEY (DealershipNum) REFERENCES DEALERSHIP(DealershipNum)
    );

"""


sqlInsert = """

INSERT into AUTOINVENTORY (VehicleIDNum, AutoCapacity,AutoColor, AutoCylinders, AutoListPrice, AutoMake,AutoMilageAtDelivery,AutoModel, AutoOptions,
 AutoCost, AutoStyle, AutoWeight, AutoYear, DateofDelivery, DateofManufacture, NumOfDoors, OdometerReading, PlaceOfManufacture)
 Values('1HGC382633B504352'  ,6, 'Blue' ,6, 45000, 'Besla', 0004, 'Amp', 'TechPackage', 30000, 'Sedan', '1500', '2018','March 10 2018', 'Jan 12 2018', 4, 006, 'Detroit')
   
"""

sqlInsert1 = """
 
INSERT into AUTOINVENTORY (VehicleIDNum, AutoCapacity,AutoColor, AutoCylinders, AutoListPrice, AutoMake,AutoMilageAtDelivery,AutoModel, AutoOptions,
 AutoCost, AutoStyle, AutoWeight, AutoYear, DateofDelivery, DateofManufacture, NumOfDoors, OdometerReading, PlaceOfManufacture) Values('1JGC382633B504352'  ,6, 'Red' ,6, 45000, 'Besla', 0004, 'Amp',
  'Comfort', 65000, '28000', '1500', '2018','March 10 2018', 'Jan 12 2018', 54, 006, 'Detroit')
    
"""
 
sqlInsert2 = """
 
INSERT into AUTOINVENTORY (VehicleIDNum, AutoCapacity,AutoColor, AutoCylinders, AutoListPrice, AutoMake,AutoMilageAtDelivery,AutoModel, AutoOptions,
 AutoCost, AutoStyle, AutoWeight, AutoYear, DateofDelivery, DateofManufacture, NumOfDoors, OdometerReading, PlaceOfManufacture)
  Values('1JGC3828833B50435'  ,6, 'Red' ,6, 45000, 'Besla', 0004, 'Amp', 'Comfort', 28000, 'Sedan', '1500', '2018','March 10 2018',
   'Jan 12 2018' , 24, 006, 'Detroit')
    
"""
 
sqlInsert3 = """
 
INSERT into AUTOINVENTORY (VehicleIDNum, AutoCapacity,AutoColor, AutoCylinders, AutoListPrice, AutoMake,AutoMilageAtDelivery,AutoModel, AutoOptions,
 AutoCost, AutoStyle, AutoWeight, AutoYear, DateofDelivery, DateofManufacture, NumOfDoors, OdometerReading, PlaceOfManufacture)
Values('1JGC382633B504344'  ,6, 'Red' ,6, 45000, 'Besla', 0004, 'Amp', 'Comfort', 29000, '29000', '1500', '2018','March 10 2018',
 'Jan 12 2018', 14, 006, 'Detroit')
    
"""
 
sqlInsert4 = """
 
INSERT into AUTOINVENTORY (VehicleIDNum, AutoCapacity,AutoColor, AutoCylinders, AutoListPrice, AutoMake,AutoMilageAtDelivery,AutoModel, AutoOptions,
 AutoCost, AutoStyle, AutoWeight, AutoYear, DateofDelivery, DateofManufacture, NumOfDoors, OdometerReading, PlaceOfManufacture)
Values('1JGC382633B504333'  ,4, 'Pink' ,6, 35000, 'Besla', 0004, 'Amp', 'Economy', 34000, 'Sedan', '1500', '2018','March 10 2018', 'Jan 12 2018',
0088 ,6, 'Detroit')
    
"""


#conn.execute(sqlDrop)
#conn.execute(sqlstatement)
#===============================================================================
#===============================================================================
#conn.execute(sqlInsert )
#===============================================================================
# conn.execute(sqlInsert1)
# conn.execute(sqlInsert2)
# conn.execute(sqlInsert3)
#===============================================================================
conn.execute(sqlInsert4)

conn.commit()