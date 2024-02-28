cmd_to_make_table = """CREATE TABLE FARMERS (
     EMAIL VARCHAR(255),
     FIRSTNAME VARCHAR(255),
     LASTNAME VARCHAR(255),
     PASSWORD INTEGER);"""

cmd_to_insert_values = """INSERT INTO FARMERS Values {}"""
cmd_to_insert_values_specific_columns = """INSERT INTO FARMERS (EMAIL, FIRSTNAME, LASTNAME , PASSWORD) Values {}"""

cmd_to_select = """SELECT * FROM FARMERS"""

cmd_to_change_value = """UPDATE FARMERS SET {} = {}"""

cmd_to_delete = """DELETE FROM FARMERS WHERE {} = {};"""

cmd_to_check_table = '''SELECT name FROM sqlite_master WHERE type='table' AND name ='FARMERS';'''




cmd_to_make_orders_table = """CREATE TABLE ORDERS (
     ITEM_NAME VARCHAR(255),
     PRICE INTEGER,
     BUYER VARCHAR(255),
     PAYMENT_METHOD VARCHAR(255));"""

cmd_to_insert_orders_values = """INSERT INTO ORDERS Values {}"""
cmd_to_insert_orders_values_specific_columns = """INSERT INTO ORDERS (ITEM_NAME, PRICE, BUYER, PAYMENT_METHOD) Values {}"""

cmd_to_select_orders = """SELECT * FROM ORDERS"""

cmd_to_change_orders_value = """UPDATE ORDERS SET {} = {}"""

cmd_to_delete_orders = """DELETE FROM ORDERS WHERE {} = {};"""

cmd_to_check_orders_table = '''SELECT name FROM sqlite_master WHERE type='table' AND name ='ORDERS';'''



cmd_to_make_products_of_org_table = """CREATE TABLE products_of_org (
     PRODUCT_NAME VARCHAR(255),
     PRICE INTEGER,
     DESCRIPTION VARCHAR(255),
     QUANTITY INTEGER);"""

cmd_to_insert_products_of_org_values = """INSERT INTO products_of_org Values {}"""
cmd_to_insert_products_of_org_values_specific_columns = """INSERT INTO products_of_org (ITEM_NAME, PRICE, BUYER, PAYMENT_METHOD) Values {}"""

cmd_to_select_products_of_org = """SELECT * FROM products_of_org"""

cmd_to_change_products_of_org_value = """UPDATE products_of_org SET {} = {} WHERE {} ={}"""

cmd_to_delete_products_of_org = """DELETE FROM products_of_org WHERE {} = {};"""

cmd_to_check_products_of_org_table = '''SELECT name FROM sqlite_master WHERE type='table' AND name ='products_of_org';'''



# Python3 code to validate a password
# A utility function to check
# whether a password is valid or not
def isValid(password):
    # for checking if password length
    # is between 8 and 15
    if (len(password) < 8 or len(password) > 15):
        return False

    # to check space
    if (" " in password):
        return False

    if (True):
        count = 0

        # check digits from 0 to 9
        arr = ['0', '1', '2', '3', 
        '4', '5', '6', '7', '8', '9']

        for i in password:
            if i in arr:
                count = 1
                break

        if count == 0:
            return False

    # for special characters
    if True:
        count = 0

        arr = ['@', '#','!','~','$','%','^',
                '&','*','(',',','-','+','/',
                ':','.',',','<','>','?','|']

        for i in password:
            if i in arr:
                count = 1
                break
        if count == 0:
            return False

    if True:
        count = 0

        # checking capital letters
        for i in range(65, 91):

            if chr(i) in password:
                count = 1

        if (count == 0):
            return False

    if (True):
        count = 0

        # checking small letters
        for i in range(97, 123):

            if chr(i) in password:
                count = 1

        if (count == 0):
            return False

    # if all conditions fails
    return True

    # Driver code
    password1 = "GeeksForGeeks"

    if (isValid([i for i in password1])):
        print("Valid Password")
    else:
        print("Invalid Password!!!")

    password2 = "Geek$ForGeeks7"
    if (isValid([i for i in password2])):
        print("Valid Password")
    else:
        print("Invalid Password!!!")



