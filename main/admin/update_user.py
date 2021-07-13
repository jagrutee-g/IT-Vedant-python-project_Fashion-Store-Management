import mysql.connector

class UpdateUser:
    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def update_user(self):

        print(
            "**Please enter the details of the user to be updated. \
            \nAll fields are mandatory.**")

        while True:
            try:

                user_id = int(input("\n\nPlease enter the ID of the product to be updated: "))
                first_name = input("\n\nPlease enter the name of the product: ")
                last_name = input("\nPlease enter the type of product: ")
                user_type = int(input("\nPlease enter the privileges for user 1. Admin or 2. Buyer: "))
                if user_type==1:
                    user_type="Admin"
                else:
                    user_type="User"
                loginid = input("\nPlease enter the loginid of the user: ")
                password = input("\nPlease enter the password of the user: ")
                break

            except ValueError:
                print("Please enter a valid input!! Please try again.\n\n")

        sql = "UPDATE fashionstore.login SET FirstName=%s, LastName=%s, Type=%s, LoginID=%s, Password=%s WHERE ID=%s;"
        val = (first_name,last_name,user_type,loginid,password,user_id)

        self.mycursor.execute(sql,val)

        self.conn.commit()

        print("\n\nYour user was updated successfully.")

        consent = input("\n\nDo you want to update another user(Y/N): ")  # to add another product
        if consent == 'y' or consent == 'Y':
            self.update_user()
        else:
            self.mycursor.close()
            self.conn.close()
            return