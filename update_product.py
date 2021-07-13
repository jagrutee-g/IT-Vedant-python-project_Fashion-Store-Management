import mysql.connector

class UpdateProduct:
    '''To update a product in database'''
    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def update_product(self):

        print(
            "**Please enter the details of the product to be updated. \
            \nAll fields are mandatory.**")

        while True:
            try:

                #get details of the product to be updated
                product_id = int(input("\n\nPlease enter the ID of the product to be updated: "))
                product_name = input("\n\nPlease enter the name of the product: ")
                product_type = input("\nPlease enter the type of product: ")
                product_brand = input("\nPlease enter the product brand: ")
                product_color = input("\nPlease enter the color of the product: ")
                product_price = float(input("\nPlease enter the price of the product: "))
                product_discount = float(input("\nPlease enter the discount percentage, if not available enter 0: "))
                product_gender = int(input("\nPlease enter the whether product is to be worn by a 1.Male or 2.Female (Enter 1 or 2): "))
                if product_gender==1:
                    product_gender="Male"
                else:
                    product_gender="Female"
                product_stock = int(input("\nPlease enter the stock availability of the product: "))
                break

            except ValueError:
                print("Please enter a valid input!! Please try again.\n\n")

        #SQL query to update the product
        sql = "UPDATE fashionstore.products SET ProductName=%s, ProductType=%s,ProductBrand=%s, ProductColor=%s, ProductPrice=%s, DiscountPercentage=%s, Gender=%s, Available=%s WHERE ProductID=%s;"
        val = (product_name,product_type,product_brand,product_color,product_price,product_discount,product_gender,product_stock,product_id,)

        self.mycursor.execute(sql,val)

        self.conn.commit()

        print("\n\nYour product was updated successfully.")

        consent = input("\n\nDo you want to update another product(Y/N): ")  # to add another product
        if consent == 'y' or consent == 'Y':
            self.update_product()
        else:
            self.mycursor.close()
            self.conn.close()
            return