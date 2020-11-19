from others.clear_screen import clear
from others.sql import SHOW_USERS, CART_BY_USER
from others.msg import USER_LIST, INVALID_CHOICE, EXIT_MSG, ENTER_CHOICE

import sys

def show_users(conn):
    cur = conn.cursor()
    cur.execute(SHOW_USERS)
    rows = cur.fetchall()
    cur.close()

    user_list = USER_LIST

    for row in range (0, len(rows)):
        user_list += "\n{}: {}".format(row+1, rows[row][1].capitalize())
    user_list += "\n{}: {}".format(len(rows)+1, "Exit")

    choice = None
    while choice!=str(len(rows)+1):
        print(user_list)        
        choice = input(ENTER_CHOICE)
        clear()

        if choice not in [str(i) for i in range (0,len(rows)+2)]:
            print(INVALID_CHOICE)

        elif choice == '0':
            break

        elif choice == str(len(rows)+1):
            conn.close()
            exit(EXIT_MSG)

        else:
            show_cart_by_user(conn, rows[int(choice)-1][0], rows[int(choice)-1][1])
        
def show_cart_by_user(conn, user_id, user):
        cur = conn.cursor()
        cur.execute(CART_BY_USER , (user_id, ))

        rows = cur.fetchall()

        if rows:
            print("-------------------Cart Detail of {}----------------". format(user.capitalize().ljust(10,'-')))
            print("|     Product     |  Quantity  |  Selling Price  |  Total  |")
            print("------------------------------------------------------------")
            for row in rows:
                    print("|{}|{}|{}|{}|".format(row[0].center(17), str(row[1]).center(12), str(row[2]).center(17), str(row[3]).center(9)))
            print("------------------------------------------------------------\n")
       
        else:
            print("{} has a empty cart\n".format(user.capitalize()))