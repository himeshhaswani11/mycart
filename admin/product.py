from others.clear_screen import clear
from others.sql import INSERT_PRODUCT_CATEGORY, SHOW_CATEGORY, INSERT_PRODUCT
from others.msg import CATEGORY_LIST, INVALID_CHOICE, ENTER_CHOICE


def add_product_category(conn):
    try:
        category = input("Enter Product Category:")

        query = INSERT_PRODUCT_CATEGORY
        values = (category.capitalize(), )
        cur = conn.cursor()
        cur.execute(query, values)
        cur.close()
        conn.commit()

        print("Product category added\n")

    except Exception as e:
        print("Category already present\n")

def add_product(obj):
    cur = obj.conn.cursor()
    cur.execute(SHOW_CATEGORY)
    rows = cur.fetchall()
    cur.close()

    product_categories = CATEGORY_LIST

    for row in range (0, len(rows)):
        product_categories += "\n{}: {}".format(row+1, rows[row][0])
    
    category_id = None
    while category_id not in [str(i) for i in range (1,len(rows)+1)]:

        print(product_categories)
        category_id = input(ENTER_CHOICE)
        clear()
        
        if category_id not in [str(i) for i in range (0,len(rows)+1)]:
            print(INVALID_CHOICE)
            add_product(obj)

        elif category_id == '0':
            obj.show_admin_choices()

        product = input("\nEnter Product Name:")
        selling_price = input("Enter Selling Price:")
        desc = input("Enter Product Description:")

        try:
            query = INSERT_PRODUCT
            values = (product, float(selling_price), desc, category_id)
            cur = obj.conn.cursor()
            cur.execute(query, values)
            cur.close()
            obj.conn.commit()

            clear()
            print("Product added\n")
            obj.show_admin_choices()

        except Exception as e:
            clear()
            print("Product already present\n")    