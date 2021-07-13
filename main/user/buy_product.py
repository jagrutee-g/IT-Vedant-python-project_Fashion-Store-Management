import  mysql.connector
import pandas as pd
from datetime import datetime

class BuyProduct:
    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

        self.add_to_cart=0
        self.val = []


    def buy_product(self,sales_id):

        print("\n\nFollowing products are available for sale: ")
        self.mycursor.execute("SELECT * FROM products")
        product_data = pd.DataFrame(self.mycursor.fetchall())
        product_data.columns = self.mycursor.column_names
        product_data = product_data.set_index(keys='ProductID')
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        print(product_data)

        while True:

            try:
                product_id = int(input("\nPlease enter the ID product you want to buy: "))
                quantity  = int(input("\nPlease enter the quantity of the product you want to buy: "))
            except ValueError:
                print("\n\nPlease enter valid values.")
            else:
                self.mycursor.execute("SELECT productid FROM products where productid=%s",(product_id,))
                fetched_product_id = self.mycursor.fetchall()
                if not fetched_product_id:
                    print("\nPlease enter a valid product ID.")
                else:
                    self.mycursor.execute("SELECT Available FROM products where productid=%s", (product_id,))
                    fetched_availablity = self.mycursor.fetchall()
                    if fetched_availablity[0][0] < quantity:
                        print("\n\nOut of stock!!! Please enter quantity less than {} or if none available select another similar product.".format(fetched_availablity[0][0]))
                        cont = input("\nDo you want to buy another product? (Y/N): ")
                        if cont=='Y' or cont=='y':
                            continue
                        else:
                            print("\n\nOkay going back to main menu.")
                            return
                    else:
                        break

        self.mycursor.execute("SELECT ProductName FROM products where productid=%s", (product_id,))
        product_name = self.mycursor.fetchall()
        product_name=product_name[0][0]
        print("{} is added to your cart.".format(product_name))
        self.add_to_cart += 1

        self.mycursor.execute("SELECT productprice FROM products WHERE productid=%s",(product_id,))
        product_price = self.mycursor.fetchall()
        product_price=product_price[0][0]
        sales_amount = product_price*quantity

        self.mycursor.execute("SELECT discountpercentage FROM products WHERE productid=%s", (product_id,))
        discount = self.mycursor.fetchall()
        discount = discount[0][0]
        sales_amount=sales_amount*discount*0.01

        sales_date=datetime.now()
        sales_date=sales_date.strftime('%Y-%m-%d %H:%M:%S')

        #to store list of various products bought
        self.val.append((sales_id,product_id,product_name,quantity,sales_amount,sales_date))

        cont=input("\n\nDo you want to continue shopping? (Y/N): ")
        if cont=='Y' or cont=='y':
            self.buy_product(sales_id)
        else:
            sql = "INSERT INTO `fashionstore`.`sales` (`SalesID`, `ProductID`,`ProductName`, `Quantity`, `SalesAmount`, `SalesDate`)\
                                          VALUES(%s,%s,%s,%s,%s,%s)"
            self.mycursor.executemany(sql, self.val)

            stock=fetched_availablity[0][0]-quantity
            self.mycursor.execute("UPDATE products SET Available=%s WHERE productid=%s",(stock,product_id))



            check=input("\n\nDo you want to proceed to checkout? (Y/N): ")
            if check=='Y' or check=='y':
                self.conn.commit()
                self.mycursor.close()
                self.conn.close()
                return self.add_to_cart

            elif check=='N' or check=='n':
                print("\n\nYour order will be not processed and cart will be emptied.")
                print("\nGoing back to main menu.")
                self.add_to_cart=0
                self.mycursor.close()
                self.conn.close()
                return self.add_to_cart

            else:
                print("Please enter a correct choice.")

