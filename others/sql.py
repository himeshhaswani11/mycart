USER_TYPE = """
    SELECT
        user_id, user_type
    FROM
        users
    WHERE 
        user_name=? and password=?
"""

INSERT_PRODUCT_CATEGORY = """
    INSERT 
        INTO product_category(category_name) 
    VALUES
        (?)
"""

SHOW_CATEGORY = """
    SELECT 
        category_name
    FROM 
        product_category
"""

INSERT_PRODUCT = """
    INSERT 
        INTO products(product_name, product_selling_price, product_desc, category_id) 
    VALUES
        (?,?,?,?)
"""

SHOW_USERS = """
    SELECT 
        user_id, user_name 
    FROM 
        USERS 
    WHERE
        user_type='member'
"""

CART_BY_USER = """
    SELECT  
        product_name, line_qty, line_selling_price, line_total
    FROM 
        orderline, products
    WHERE 
        orderline.product_id = products.product_id and user_id = ? and line_type='cart'
"""

BILL_ALL_USERS = """
    SELECT  
        user_name, bill_actual_amt, bill_discount_amt, bill_total
    FROM 
        bill, users
    WHERE 
        bill.bill_user = users.user_id
    ORDER
        BY user_name
"""

SELECT_PRODUCT = """
    SELECT 
        product_id, product_name, product_desc, product_selling_price 
    FROM 
        products 
    WHERE 
        category_id=?
"""

SHOW_CART = """
    SELECT 
        orderline.product_id, product_name, line_qty, line_selling_price, line_total, line_id
    FROM
        products, orderline 
    WHERE 
        orderline.product_id=products.product_id and orderline.user_id=? and line_type='cart'
"""

INSERT_INTO_ORDERLINE = """
    INSERT 
        INTO orderline(product_id, line_qty, line_selling_price, line_total, line_type, user_id)
    VALUES
        (?,?,?,?,?,?)
"""

INSERT_BILL = """
    INSERT 
        INTO bill(bill_user, bill_actual_amt, bill_discount_amt, bill_total)
    VALUES
        (?,?,?,?)
"""

UPDATE_ORDERLINE = """
    UPDATE 
        orderline 
    SET 
        bill_id = ?, line_type = ? 
    WHERE
        user_id= ?
"""

DELETE_FROM_CART = """
    DELETE 
        FROM orderline
    WHERE
        line_id = ?
"""