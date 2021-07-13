import mysql.connector
import pandas as pd

class Checkout:

    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def checkout(self,sales_id):

        print("\n\nYou have purchased the following items:")

        self.mycursor.execute("SELECT * FROM sales WHERE salesid=%s;",(sales_id,))
        sales_info = pd.DataFrame(self.mycursor.fetchall())
        sales_info.columns = self.mycursor.column_names
        sales_info = sales_info.set_index(keys='SalesID')

        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        print(sales_info)

        self.mycursor.execute("SELECT SUM(salesamount) FROM sales WHERE salesid=%s;", (sales_id,))
        total_sales_amount = self.mycursor.fetchall()
        total_sales_amount=total_sales_amount[0][0]

        print("\n\nYour total sales amount for above purchased items is: {}".format(total_sales_amount))

        while True:
            payment=input("\n\nDid you pay the bill? (Y/N): ")
            if payment=='y' or payment=='Y':
                print("\n\n***Thank you for shopping at Fashion Store. Have a nice day.***")
                self.mycursor.close()
                self.conn.close()
                return
            else:
                print("\n\nPlease pay the bill.")






