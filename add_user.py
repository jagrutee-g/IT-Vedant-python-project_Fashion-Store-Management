import mysql.connector

class AddUser:

    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def add_user(self):

        print("**Please enter the details of the user to be added. \
        \nAll fields are mandatory.**")

        while True:
            try:

                first_name = input("\n\nPlease enter the first name of the new user: ")
                last_name = input("\nPlease enter the last name of new user: ")
                user_type = int(input("\nPlease enter the privileges to be granted to the new user 1.Admin or 2. User: "))
                if user_type==1:
                    user_type="Admin"
                else:
                    user_type="User"
                loginid = input("\nPlease enter the login ID of the new user: ")
                password = input("\nPlease enter the password of the new user: ")
                break

            except ValueError:
                print("Please enter a valid input!! Please try again.\n\n")

        sql = ("INSERT INTO `fashionstore`.`login` \
        (`FirstName`, `LastName`, `Type`, `LoginID`, `Password`) \
        VALUES (%s, %s, %s, %s, %s);")

        val = (first_name,last_name,user_type,loginid,password)

        self.mycursor.execute(sql, val)

        self.conn.commit()
        print("\n\nYour user was inserted successfully.")


        consent = input("\n\nDo you want to add another user(Y/N): ") #to add another product
        if consent=='y' or consent=='Y':
            self.add_product()
        else:
            self.mycursor.close()
            self.conn.close()
            return