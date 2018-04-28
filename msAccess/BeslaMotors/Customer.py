import pyodbc


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\BESLA\BESLA.accdb;')
#cursor = conn.cursor()

sqlDrop  = """

DROP TABLE CUSTOMER;

"""

sqlstatement = """

    Create Table CUSTOMER (
    
        CustID autoincrement,
        CustFName varchar(20),
        CustLName varchar(20), 
        CustStreet varchar(20), 
        CustCity varchar(20), 
        CustZip    number,
        CustAnnualIncome currency, 
        CustomerEmail varchar(20), 
        CustomerEmployer varchar(20),
        CustomerFinancing varchar(20),
        CustGender varchar(20),
        CustomerInsuranceNum varchar(20),
        CustomerLeaseBuy varchar(20), 
        CustomerLicenseNum varchar(20),  
        CustomerPhone number, 
        CustomerReferOut varchar(20), 
        CustomerReturnBuyer varchar(120), 
        CustomerSocial number, 
        CustomerTradeIn varchar(20),  
        HowCustomerFoundDealership varchar(20), 
        OfferedTestDrive varchar(20), 
        CreditScore varchar(20), 
        WarrantyPurchase varchar(20),        
        PRIMARY KEY (CustID)
                
    );


"""


sqlInsert1 = """

INSERT into CUSTOMER (CustFName, CustLName, CustStreet, CustCity, CustZip, CustAnnualIncome,CustomerEmail,CustomerEmployer,
CustomerFinancing, CustGender, CustomerInsuranceNum, CustomerLeaseBuy, CustomerLicenseNum, CustomerPhone,CustomerReferOut,CustomerReturnBuyer,CustomerSocial, CustomerTradeIn,
HowCustomerFoundDealership, OfferedTestDrive, CreditScore,WarrantyPurchase)


Values( 'Sue' ,'Gibbons' ,'4 Forest drive', 'Mamoroneck', 09333, 175000, 'sue@gmail.com', 'JPM', 'Purchase', 'F', '9233442', 'Purchase', '98445',
 3489083, 'n/a', 'Yes',8321423,'Yes', 
'Google', 'yes', '870','Yes');

"""

sqlInsert2 = """

INSERT into CUSTOMER (CustFName, CustLName, CustStreet, CustCity, CustZip, CustAnnualIncome,CustomerEmail,CustomerEmployer,
CustomerFinancing, CustGender, CustomerInsuranceNum, CustomerLeaseBuy, CustomerLicenseNum, CustomerPhone,CustomerReferOut,CustomerReturnBuyer,CustomerSocial, CustomerTradeIn,
HowCustomerFoundDealership, OfferedTestDrive, CreditScore,WarrantyPurchase)


Values( 'Wesley' ,'Hammond' ,'5 Forest drive', 'Mamoroneck', 09333, 175000, 'sue@gmail.com', 'JPM', 'Purchase', 'F', '9233442', 'Purchase', '98445',
 3489083, 'n/a', 'Yes',8321423,'Yes', 
'Google', 'yes', '870','Yes');

"""
sqlInsert3 = """

INSERT into CUSTOMER (CustFName, CustLName, CustStreet, CustCity, CustZip, CustAnnualIncome,CustomerEmail,CustomerEmployer,
CustomerFinancing, CustGender, CustomerInsuranceNum, CustomerLeaseBuy, CustomerLicenseNum, CustomerPhone,CustomerReferOut,CustomerReturnBuyer,CustomerSocial, CustomerTradeIn,
HowCustomerFoundDealership, OfferedTestDrive, CreditScore,WarrantyPurchase)


Values( 'Mark' ,'Valentine' ,'2 High Oak Lane', 'Danbury', 90773, 125000, 'mvalentine@gmail.com', 'GE', 'Lease', 'M', '9822442', 'Lease', '66445',
 3489083, 'n/a', 'Yes',8321423,'Yes', 
'Friend', 'yes', '770','Yes');

"""
sqlInsert4 = """

INSERT into CUSTOMER (CustFName, CustLName, CustStreet, CustCity, CustZip, CustAnnualIncome,CustomerEmail,CustomerEmployer,
CustomerFinancing, CustGender, CustomerInsuranceNum, CustomerLeaseBuy, CustomerLicenseNum, CustomerPhone,CustomerReferOut,CustomerReturnBuyer,CustomerSocial, CustomerTradeIn,
HowCustomerFoundDealership, OfferedTestDrive, CreditScore,WarrantyPurchase)


Values( 'Jose' ,'Sanchez' ,'4 lake drive', 'Croton Falls', 04333, 175000, 'Sanchez@me.com', 'Self Employed', 'Finance', 'M', '9233332', 'Finance', '98345',
 3489083, 'n/a', 'Yes',8321423,'Yes', 
'Website', 'No', '870','No');

"""



#conn.execute(sqlDrop)
#conn.execute(sqlstatement)
#conn.execute(sqlInsert)
conn.execute(sqlInsert1)
#===============================================================================
conn.execute(sqlInsert2)
conn.execute(sqlInsert3)
conn.execute(sqlInsert4)
#===============================================================================

conn.commit()