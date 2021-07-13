import mysql.connector
#import getpass,stdiomask

class Login:
    """Validating login credentials"""
    def __init__(self):
        #connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

        self.loginid=0
        self.password=0

    def login(self,type):
        #login using credentials and only 3 tries are allowed
        n = 3
        print("\n\nYou have {} attempts left.".format(n))
        while n>0:
            self.loginid = input("Please enter your login ID: ")
            self.password = input("Please enter your password: ")

            self.mycursor.execute("SELECT loginid FROM login WHERE type=%s and loginid=%s", (type,self.loginid))
            self.myresult1 = self.mycursor.fetchall()

            self.mycursor.execute("SELECT password FROM login WHERE  type=%s and password=%s", (type,self.password))
            self.myresult2 = self.mycursor.fetchall()



            if self.myresult1 == [] or self.myresult2==[]:
                print("Please enter a valid login id/password.")
                n-=1
                print("You have {} attempts left.".format(n))

            else:

                self.mycursor.execute("SELECT FirstName, LastName FROM login WHERE type=%s and loginid=%s", (type,self.loginid))
                self.name = self.mycursor.fetchall()
                print("\n\nHi "+self.name[0][0]+" "+self.name[0][1])
                return

        self.conn.commit()
        self.conn.close()
        print("\n\nYou have expired your tries. Bye")
        return