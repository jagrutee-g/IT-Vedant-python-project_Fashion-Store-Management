import sys
import mysql.connector
import user.buy_product
import admin.view_product
import user.checkout
import user.cancel_order
# import admin.delete_product
# import admin.add_user
# import admin.update_user
# import admin.delete_user
# import admin.view_stocks


class User:
    """Performing Buyer functions"""
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()
        self.add_to_cart=0
        self.sales_id=0

    def buyer_activity(self):

        self.mycursor.execute("SELECT MAX(salesid) FROM sales;")
        sales_id = self.mycursor.fetchall()
        if sales_id[0][0] is None:
            self.sales_id = 1
        else:
            self.sales_id = sales_id[0][0] + 1

        while True:
            print("\n\nPlease enter what you want to do:")
            print("1. Buy a product")
            print("2. View or Browse all product details")
            print("3. Checkout")
            print("4. Cancel or Return an order")
            print("5. Quit")

            try:
                buyer_choice = int(input("Choice: "))
                if buyer_choice == 1:
                    buy = user.buy_product.BuyProduct()
                    self.add_to_cart=buy.buy_product(self.sales_id)

                elif buyer_choice == 2:
                    v = admin.view_product.ViewProduct()
                    v.view_product()

                elif buyer_choice == 3:
                    if self.add_to_cart==0:
                        print("\n\nYou cannot proceed as you have not purchased any item.")
                    else:
                        checkout = user.checkout.Checkout()
                        checkout.checkout(self.sales_id)


                elif buyer_choice == 4:
                    co = user.cancel_order.CancelOrder()
                    salesid_tocancel=int(input("\n\nPlease enter the sales ID of the order you want to cancel or return: "))
                    co.cancel_order(salesid_tocancel)

                elif buyer_choice == 5:
                    sys.exit()

                else:
                    print("Please enter a valid choice.\n\n")

            except ValueError:
                print("Please enter a number.")