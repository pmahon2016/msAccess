import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\BESLA\BESLA.accdb;')
#cursor = conn.cursor()

sqlDrop  = """

#DROP TABLE CUSTOMER;

"""

sqlstatement = """

CREATE TABLE CUSTOMER (

        CustID autoincrement,
        CustLName varchar(20),
        CustFName varchar(20), 
        CustStreet varchar(20), 
        CustCity varchar(20), 
        CustZip	number,
        CustAnnnualIncome currency, 
        CustomerEmail varchar(20), 
        CustomerEmployer, varchar(20),
        CustomerFinancing, varchar(20),
        CustGender varchar(20),
        CustomerInsuranceNum varchar(20),
        CustomerLeaseBuy varchar(20),, 
        CustomerLicenseNum varchar(20),,  
        CustomerPhone number, 
        CustomerReferOut varchar(20),, , 
        CustomerReturnBuyer varchar(120), 
        CustomerSocial number, 
        CustomerTrade-In varchar(20),,   
        HowCustomerFoundDealership varchar(20),, 
        OfferedTestDrive varchar(20), 
        RentOwnCustomerHome varchar(20), 
        ExtendedWarranty varchar(20),        
        CONSTRAINTS CustID_PK PRIMARY KEY (CustID),
                
    );

"""


sqlInsert = """

INSERT into CUSTOMER (CustLName, CustFName, CustStreet, CustCity, CustZip, CustAnnualIncome,CustEmail,CustomerEmployer, CustomerFinancing, CustGender, CustInsuranceNum, CustPhone,CustReferOut,CustomerReturnBuyer,CustomerSocial, CustomerTradeIn, HowCustomerFoundDealership, OfferedTestDrive, RentOwnCustomerHome,ExtendedWarranty)


Values(', 'Charlie Pride' , 6, 'Blue' ,6, 'Besla', 'Amp', 8777373, 
54000, 'Sedan' ,'2018', 'John Blogs', '2 hometown road', 'Jersey City' , 'Belsa Financing', 
'Lease', 'April 09 2018','Belsa Motors' , 4 , 67 , 1000, 'no'); 
   
"""

 



#conn.execute(sqlDrop)
conn.execute(sqlstatement)
#conn.execute(sqlInsert)
#conn.execute(sqlInsert1)
#===============================================================================
# conn.execute(sqlInsert2)
# conn.execute(sqlInsert3)
# conn.execute(sqlInsert4)
#===============================================================================

conn.commit()