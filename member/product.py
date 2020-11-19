from others.clear_screen import clear
from others.sql import SHOW_CATEGORY, SELECT_PRODUCT, INSERT_INTO_ORDERLINE
from others.msg import PRODUCT_CATEGORY_LIST, PRODUCT_LIST, PRODUCT_DESC_CART, ENTER_CHOICE, INVALID_CHOICE, EXIT_MSG

def show_product_categories(obj):  
    cur = obj.conn.cursor()
    cur.execute(SHOW_CATEGORY)
    rows = cur.fetchall()
    cur.close()

    product_categories = PRODUCT_CATEGORY_LIST. format(obj.user_name.capitalize())

    for row in range (0, len(rows)):
        product_categories += "\n{}: {}".format(row+1, rows[row][0])
    product_categories += "\n{}: {}".format(len(rows)+1, "Exit")
    
    choice = None
    while choice!=str(len(rows)+1):
        print(product_categories)
        choice = input(ENTER_CHOICE)
        clear()
                
        if choice not in [str(i) for i in range (0,len(rows)+2)]:
            print(INVALID_CHOICE)

        elif choice == '0':
            obj.show_member_choices()

        elif choice == str(len(rows)+1):
            obj.conn.close()
            exit(EXIT_MSG)

        else:
            show_product(obj, choice)

def show_product(obj, category_id):
    cur = obj.conn.cursor()
    query = SELECT_PRODUCT
    values = (category_id,)
    cur.execute(query, values)
    rows = cur.fetchall()

    product = PRODUCT_LIST. format(obj.user_name.capitalize())

    for row in range (0, len(rows)):
        product += "\n{}: {}".format(row+1, rows[row][1])
    product += "\n{}: {}".format(len(rows)+1, "Exit")
    
    choice = None
    while choice!=str(len(rows)+1):
        print(product)
        choice = input(ENTER_CHOICE)
        clear()

        if choice not in [str(i) for i in range (0,len(rows)+2)]:   
            print(INVALID_CHOICE)

        elif choice == '0':
            break

        elif choice == str(len(rows)+1):
            obj.conn.close()
            exit(EXIT_MSG)

        else:
            show_product_desc(obj, category_id, rows[int(choice)-1])

def show_product_desc(obj, category_id, row):
    product = PRODUCT_DESC_CART. format(obj.user_name.capitalize(), row[1].capitalize())

    choice = None
    while choice!='3':
        print(product)
        choice = input(ENTER_CHOICE)

        clear()        
        if choice not in ['0', '1', '2', '3']:
            print(INVALID_CHOICE)

        elif choice == '0':
            break

        elif choice == '1':
            print("=-------------------------------=")
            print("Product Name : {}".format(row[1]))
            print("Description  : {}".format(row[2]))
            print("=-------------------------------=")

        elif choice == '2':
            print("Once you enter the quantity you will be redirect to product category page .........")
            qty = input("Enter Quantity:")
            
            query = INSERT_INTO_ORDERLINE
            values = (row[0], qty, row[3], int(qty)*float(row[3]), 'cart', obj.user_id)
            cur = obj.conn.cursor()
            cur.execute(query, values)
            cur.close()
            obj.conn.commit()

            show_product_categories(obj)

        else:
            conn.close()
            exit(EXIT_MSG)