import mysql.connector

class CancelOrder:
    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def cancel_order(self,sales_id):
        print("\n\nDo you want to cancel/return entire order or part of the order?:")
        print("1. Entire Order\n2. Part of Order")

        while True:
            try:
                choice=int(input("Please enter your choice: "))
                if choice==1:
                    confirm=input("\n\nAre you sure you want to cancel/return the entire order? (Y/N): ")
                    if confirm=='y' or confirm=='Y':
                        self.mycursor.execute("SELECT SUM(salesamount) FROM sales WHERE salesid=%s;", (sales_id,))
                        total_sales_amount = self.mycursor.fetchall()
                        total_sales_amount = total_sales_amount[0][0]

                        # self.mycursor.execute("SELECT productid FROM sales WHERE salesid=%s",(sales_id,))
                        # for product_id in self.mycursor.fetchall():
                        #     self.mycursor.execute("SELECT quantity FROM sales WHERE salesid=%s and product_id=%s", (sales_id,product_id))
                        #     quantity = self.mycursor.fetchall()
                        #     quantity=quantity[0][0]
                        #     self.mycursor.execute("UPDATE products SET quantity=%s WHERE productid=%s;",(quantity,product_id))

                        self.mycursor.execute("DELETE FROM sales WHERE salesid=%s",(sales_id,))

                        print("\n\nYour order is successfully cancelled.")
                        self.conn.commit()
                        self.mycursor.close()
                        self.conn.close()
                        return
                    else:
                        main_menu=input("Please enter choice 2 or do you want to go back to main menu. Type 'Y': ")
                        if main_menu=='Y' or main_menu=='y':
                            return
                        else:
                            self.cancel_order(sales_id)

                elif choice==2:
                    product_id=int(input("\n\nPlease enter the ID of the product you want to return: "))
                    self.mycursor.execute("DELETE FROM sales WHERE salesid=%s and productid=%s", (sales_id,product_id))

                    print("\n\nYour order is successfully cancelled.")
                    self.conn.commit()
                    self.mycursor.close()
                    self.conn.close()
                    return

                else:
                    print("Please enter correct choice.")


            except ValueError:
                print("Please enter valid values.")


