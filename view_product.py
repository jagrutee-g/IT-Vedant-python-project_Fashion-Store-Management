import mysql.connector
import pandas as pd

class ViewProduct:
    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def view_product(self):

        print("\n\nAll products available in our store today are:")
        self.mycursor.execute("SELECT * FROM products")
        product_data = pd.DataFrame(self.mycursor.fetchall())
        product_data.columns = self.mycursor.column_names
        self.mycursor.close()
        self.conn.close()
        product_data=product_data.set_index(keys='ProductID')
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        print(product_data)

        return