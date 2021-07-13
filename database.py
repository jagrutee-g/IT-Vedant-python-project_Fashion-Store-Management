import mysql.connector

class Database:
    """Creating a database from scratch"""
    def __init__(self):
        #connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345"
        )
        self.mycursor = self.conn.cursor()

    # setting up database
    def database(self):
        #creating a new schema
        self.mycursor.execute("create database if not exists fashionstore;")
        self.conn.commit()
        self.conn.close()

        # creating required tables in the created database schema

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

        # login table
        self.mycursor.execute("CREATE TABLE if not exists `login` (\
        `ID` int(11) NOT NULL AUTO_INCREMENT,\
        `FirstName` varchar(45) NOT NULL,\
        `LastName` varchar(45) NOT NULL,\
        `Type` varchar(45) NOT NULL,\
        `LoginID` varchar(100) NOT NULL,\
        `Password` varchar(45) NOT NULL,\
        PRIMARY KEY (`ID`),\
        UNIQUE KEY `ID_UNIQUE` (`ID`)\
        ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;")

        # products table
        self.mycursor.execute("CREATE TABLE if not exists `products` (\
        `ProductID` int(11) NOT NULL AUTO_INCREMENT,\
        `ProductName` varchar(45) DEFAULT NULL,\
        `ProductType` varchar(45) DEFAULT NULL,\
        `ProductBrand` varchar(45) DEFAULT NULL,\
        `ProductColor` varchar(45) DEFAULT NULL,\
        `ProductPrice` float unsigned DEFAULT '0',\
        `DiscountPercentage` float unsigned DEFAULT '0',\
        `Gender` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,\
        `Available` int(10) unsigned DEFAULT '0',\
        PRIMARY KEY (`ProductID`),\
        UNIQUE KEY `ProductID_UNIQUE` (`ProductID`)\
        ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;")

        # sales tables
        self.mycursor.execute("CREATE TABLE if not exists `sales` (\
        `SalesID` int(11) NOT NULL,\
        `ProductID` int(11) NOT NULL,\
        `ProductName` VARCHAR(45) DEFAULT NULL,\
        `Quantity` INT DEFAULT NULL,\
        `SalesAmount` float unsigned DEFAULT '0',\
        `SalesDate` datetime NOT NULL,\
        PRIMARY KEY (`SalesID`,`ProductID`),\
        KEY `ProductID_idx` (`ProductID`),\
        CONSTRAINT `ProductID` FOREIGN KEY (`ProductID`) REFERENCES `products` (`ProductID`) ON DELETE NO ACTION ON UPDATE NO ACTION\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;")

        #insert admin credentials
        self.mycursor.execute("select * from login")
        if self.mycursor.fetchall()==[]:
            self.mycursor.execute("INSERT INTO login \
            (`FirstName`, `LastName`, `Type`, `LoginID`, `Password`)\
            VALUES ('Jagrutee','Gawande','Admin','admin','admin123')")

        self.conn.commit()
        self.mycursor.close()
        self.conn.close()