import sys
import database
import login
from admin import admin
import user.user


if __name__=="__main__":
    #creating database
    d=database.Database()
    d.database()

    print("**************Welcome to Fashion Store******************")
    #login into system
    l=login.Login()
    login_access=0
    while login_access==0 or login_access>4:
        try:
            login_access=int(input("Please enter whether you are a: \n1. Admin \n2. Buyer\n3. Quit\n\nChoice: "))
            if login_access == 1:
                type='Admin'
                l.login(type)
            elif login_access == 2:
                type='User'
                l.login(type)
            elif login_access == 3:
                print("Thank you for visiting.")
                sys.exit()
            else:
                print("Please enter a valid choice.")
        except ValueError as err:
            print("Please enter a number.")



    if login_access==1:
        #if an admin has logged in show admin activity page
        a = admin.Admin()
        a.admin_activity()

    else:
        # if a buyer has logged in show buyer activity page
        u = user.user.User()
        u.buyer_activity()