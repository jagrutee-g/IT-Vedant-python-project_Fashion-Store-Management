import sys
import admin.add_product
import admin.view_product
import admin.update_product
import admin.delete_product
import admin.add_user
import admin.update_user
import admin.delete_user
import admin.view_stocks
import admin.view_users


class Admin:
    """Performing Admin functions"""
    def __init__(self):
        self.l=0

    def admin_activity(self):

        while True:
            print("\n\nPlease enter what you want to do:")
            print("1. View all product details")
            print("2. Add a product")
            print("3. Update a product")
            print("4. Delete a product")
            print("5. View all users")
            print("6. Add a user")
            print("7. Update user details")
            print("8. Delete user")
            print("9. View stock of all items")
            print("10. Quit")

            try:
                admin_choice = int(input("Choice: "))
                if admin_choice == 1:
                    v = admin.view_product.ViewProduct()
                    v.view_product()


                elif admin_choice == 2:
                    a = admin.add_product.AddProduct()
                    a.add_product()


                elif admin_choice == 3:
                    u = admin.update_product.UpdateProduct()
                    u.update_product()


                elif admin_choice == 4:
                    d = admin.delete_product.DeleteProduct()
                    d.delete_product()


                elif admin_choice == 5:
                    vu = admin.view_users.ViewUser()
                    vu.view_user()

                elif admin_choice == 6:
                    au = admin.add_user.AddUser()
                    au.add_user()



                elif admin_choice == 7:
                    uu = admin.update_user.UpdateUser()
                    uu.update_user()

                elif admin_choice == 8:
                    du = admin.delete_user.DeleteUser()
                    du.delete_user()



                elif admin_choice == 9:
                    vs = admin.view_stocks.ViewStocks()
                    vs.view_stocks()

                elif admin_choice == 10:
                    sys.exit()

                else:
                    print("Please enter a valid choice.\n\n")

            except ValueError:
                print("Please enter a number.")