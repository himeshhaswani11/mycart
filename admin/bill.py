from others.clear_screen import clear
from others.sql import BILL_ALL_USERS


def show_bills_all_users(conn):
        cur = conn.cursor()
        cur.execute(BILL_ALL_USERS)
        rows = cur.fetchall()

        print("---------Bill Detail for all Users----------")
        print("|  User  |  Actual  |  Discount  |  Total  |")
        print("--------------------------------------------")
        for row in rows:
                print("|{}|{}|{}|{}|".format(row[0].center(8), str(row[1]).center(10), str(row[2]).center(12), str(row[3]).center(9)))
        print("--------------------------------------------\n")
