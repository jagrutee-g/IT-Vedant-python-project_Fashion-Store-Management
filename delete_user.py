import mysql.connector

class DeleteUser:
    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def delete_user(self):

        while True:
            try:

                user_id = int(input("\n\nPlease enter the ID of the user to be deleted: "))
                break

            except ValueError:
                print("\n\nPlease enter a valid input!! Please try again.\n\n")

        sql = ("DELETE FROM `fashionstore`.`login` WHERE `ID`=%s;")
        val = (user_id,)

        self.mycursor.execute(sql,val)

        self.conn.commit()

        print("\n\nYour user was deleted successfully.")

        consent = input("\n\nDo you want to delete another user(Y/N): ")  # to add another product
        if consent == 'y' or consent == 'Y':
            self.delete_user()
        else:
            self.mycursor.close()
            self.conn.close()
            return