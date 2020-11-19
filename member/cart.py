import time
from others.clear_screen import clear
from others.sql import SHOW_CART, INSERT_BILL, UPDATE_ORDERLINE, DELETE_FROM_CART
from others.msg import BOOK_DELETE_CART, EXIT_MSG, ENTER_CHOICE, INVALID_CHOICE

def create_bill(conn, id, total, rows):
    actual_amt = total
    discount = 500 if actual_amt > 10000 else 0.0
    total_amt = actual_amt - discount

    query = INSERT_BILL
    values = (id, actual_amt, discount, total_amt, )
    cur = conn.cursor()
    cur.execute(query, values)
    conn.commit()
    bill_id = cur.lastrowid
    cur.close()

    for row in rows:
        query = UPDATE_ORDERLINE
        values = (bill_id, 'billed', id)
        cur = conn.cursor()
        cur.execute(query, values)
        conn.commit()

    print("Bill Created, you will be redirected to homepage in 3 seconds.....\n")
    time.sleep(3)

def delete_from_cart(obj, rows):
    product_id = input("Enter product id to be deleted:")
    clear()
    if int(product_id) > 0 and int(product_id) <= len(rows):
        line_id = (rows[int(product_id)-1][5],)

        query = DELETE_FROM_CART
        cur = obj.conn.cursor()
        cur.execute(query, line_id)
        obj.conn.commit()
        cur.close()  

        show_product_cart(obj)
    else:
        print("Invalid Product Id...........\n")
        show_product_cart(obj)

def show_product_cart(obj):
    cur = obj.conn.cursor()
    query = SHOW_CART
    values = (int(obj.user_id),)
    cur.execute(query,values)
    rows = cur.fetchall()

    if rows:
        total = 0.0
        print("-----------------------------Cart Details-----------------------------")
        print("|  Serial  |        Name        |  Quantity  |   Price   |   Total   |")        
        print("----------------------------------------------------------------------")        
        for row in range(0, len(rows)):
            print("|{}|{}|{}|{}|{}|".format(str(row+1).center(10), rows[row][1].center(20), str(rows[row][2]).center(12), str(rows[row][3]).center(11), str(rows[row][4]).center(11)))
            total += rows[row][4]
        print("----------------------------------------------------------------------")        
        print("|{}  |{}|".format("TOTAL".rjust(54) ,str(total).center(11,)))
        print("----------------------------------------------------------------------")        

        choice = None
        while choice!=3:
            print(BOOK_DELETE_CART. format(obj.user_name.capitalize()))
            choice = input(ENTER_CHOICE)
            
            if choice not in ['0', '1', '2', '3']:
                clear()
                print(INVALID_CHOICE)
                show_product_cart(obj)

            elif choice == '0':
                clear()
                break

            elif choice == '1':
                clear()
                create_bill(obj.conn, obj.user_id, total, rows)
                break

            elif choice == '2':
                delete_from_cart(obj, rows)

            elif choice == '3':
                clear()
                obj.conn.close()
                exit(EXIT_MSG)

    else:
        print("Your cart is empty\n")
        obj.show_member_choices()

