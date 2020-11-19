from others.clear_screen import clear
from others.connect import create_connection
from others.sql import USER_TYPE
from others.msg import WELCOME_MSG, ENTER_CHOICE, INVALID_CHOICE, MEMBER_CHOICE, ADMIN_CHOICE, EXIT_MSG


class Main:
    
    def __init__(self, conn, user_id, user_name):
        self.conn = conn
        self.user_id = user_id
        self.user_name = user_name

    def show_member_choices(self):
        choice = None
        while choice!='3':
            print(MEMBER_CHOICE .format(username.capitalize()))
            choice = input(ENTER_CHOICE)
            clear()
            
            if choice not in ['1', '2', '3']:
                print(INVALID_CHOICE)

            elif choice == '1':
                from member.product import show_product_categories
                show_product_categories(self)

            elif choice == '2':
                from member.cart import show_product_cart
                show_product_cart(self)

            else:
                conn.close()
                exit(EXIT_MSG)

    def show_admin_choices(self):
        choice = None
        while choice!='5':
            print(ADMIN_CHOICE. format(username.capitalize()))
            choice = input("Enter your choice:")
            clear()

            if choice not in ['1', '2', '3', '4', '5']:
                print(INVALID_CHOICE)

            elif choice == '1':
                from admin.product import add_product_category
                add_product_category(self.conn)
                
            elif choice == '2':
                from admin.product import add_product
                add_product(self)

            elif choice == '3':
                from admin.cart import show_users
                show_users(self.conn)

            elif choice == '4':
                from admin.bill import show_bills_all_users
                show_bills_all_users(self.conn)

            else:
                self.conn.close()
                exit(EXIT_MSG)                

# Execution starts from this line #
print(WELCOME_MSG)
username = input("Enter Your Username:")
password = input("Enter Your Password:") 

if username and password:
    conn = create_connection('my_cart')
    cur = conn.cursor()
    values = (username, password,)
    cur.execute(USER_TYPE, values)    
    row = cur.fetchone()
    cur.close()

    if row:
        clear()
        main = Main(conn, row[0], username)
        if row[1] == 'admin':
            main.show_admin_choices()
        else:
            main.show_member_choices()

    else:
        clear()
        conn.close()
        print("\nSorry we can't log you in. You are not authorised\n")