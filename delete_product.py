import mysql.connector

class DeleteProduct:
    def __init__(self):
        # connect using root login credentials
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12345",
            database="fashionstore"
        )
        self.mycursor = self.conn.cursor()

    def delete_product(self):

        while True:
            try:

                product_id = int(input("\n\nPlease enter the ID of the product to be deleted: "))
                break

            except ValueError:
                print("\n\nPlease enter a valid input!! Please try again.\n\n")

        sql = ("DELETE FROM `fashionstore`.`products` WHERE `ProductID`=%s;")
        val = (product_id,)

        self.mycursor.execute(sql,val)

        self.conn.commit()

        print("\n\nYour product was deleted successfully.")

        consent = input("\n\nDo you want to delete another product(Y/N): ")  # to add another product
        if consent == 'y' or consent == 'Y':
            self.delete_product()
        else:
            self.mycursor.close()
            self.conn.close()
            return