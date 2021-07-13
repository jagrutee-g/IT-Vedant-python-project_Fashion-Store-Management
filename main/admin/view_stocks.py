import mysql.connector
import pandas as pd

class ViewStocks:
    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def view_stocks(self):

        self.mycursor.execute("SELECT ProductName,Available FROM products")
        product_data = pd.DataFrame(self.mycursor.fetchall())
        product_data.columns = self.mycursor.column_names
        self.mycursor.close()
        self.conn.close()
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None

        print("\n\nAll stock data is as follows:")
        print(product_data)

        stock = product_data[product_data['Available']<5]

        if stock.empty:
            print("\n\nAll products are sufficiently stocked.")
        else:
            print("\n\nFollowing products are low on stock. Please refill them.\n")
            print(product_data['Available'] < 5)



        return