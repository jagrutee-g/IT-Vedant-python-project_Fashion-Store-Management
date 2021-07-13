import mysql.connector
import pandas as pd

class ViewUser:
    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def view_user(self):

        print("\n\nAll users in database are:")
        self.mycursor.execute("SELECT * FROM login")
        user_data = pd.DataFrame(self.mycursor.fetchall())
        user_data.columns = self.mycursor.column_names
        self.mycursor.close()
        self.conn.close()
        user_data=user_data.set_index(keys='ID')
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        print(user_data)

        return