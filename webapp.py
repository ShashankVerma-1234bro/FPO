from flask import Flask, render_template, request, url_for,jsonify,flash,redirect
import sqlite3,pickle,socket
from sql_commands import *

app = Flask(__name__)
app.secret_key = "BroBroBro"

#binary file
file = open("current_user_account.bin","rb") 

#SQLITE3
#farmers database
farmers_database = sqlite3.connect("FARMERS.db",check_same_thread=False)
farmer_cursor = farmers_database.cursor()

listOfTables = farmer_cursor.execute(cmd_to_check_table).fetchall()
if listOfTables == []:
    farmer_cursor.execute(cmd_to_make_table)
    farmers_database.commit()
else:
    pass

#orders of person database
orders_database = sqlite3.connect("ORDERS.db",check_same_thread=False)
orders_cursor = orders_database.cursor()

listOfTables = orders_cursor.execute(cmd_to_check_orders_table).fetchall()
if listOfTables == []:
    orders_cursor.execute(cmd_to_make_orders_table)
    orders_database.commit()
else:
    pass

#product stock database
products_of_org_database = sqlite3.connect("PRODUCT.db",check_same_thread=False)
products_of_org_cursor = products_of_org_database.cursor()

listOfTables = products_of_org_cursor.execute(cmd_to_check_products_of_org_table).fetchall()
if listOfTables == []:
    products_of_org_cursor.execute(cmd_to_make_products_of_org_table)
    products_of_org_database.commit()
    products_of_org_cursor.execute(cmd_to_insert_products_of_org_values.format(("Tractor",1999,"Tractors are used for plowing, harrowing, and tilling fields to prepare them for planting crops.",50)))
    products_of_org_cursor.execute(cmd_to_insert_products_of_org_values.format(("Cultivator",2499,"A cultivator is a farm implement commonly used in agriculture for soil cultivation and weed control.",150)))
    products_of_org_cursor.execute(cmd_to_insert_products_of_org_values.format(("Plow",28,"Plows are used for primary tillage to turn over and break up soil, preparing it for planting crops.",50)))
    products_of_org_cursor.execute(cmd_to_insert_products_of_org_values.format(("Harvester",1899,"Harvesters are machines designed to efficiently gather mature crops from fields.",105)))
    products_of_org_cursor.execute(cmd_to_insert_products_of_org_values.format(("Urea",200,"Urea is widely used in the agricultural sector both as a fertilizer and animal feed additive. ",120)))
    products_of_org_cursor.execute(cmd_to_insert_products_of_org_values.format(("Wheelbarrow",1200,"Homeowners and gardeners often use wheelbarrows and garden carts to move materials around their property.",70)))
    products_of_org_cursor.execute(cmd_to_insert_products_of_org_values.format(("Shovel",500,"Shovel tool helps with digging and transplanting soil, making shallow trenches, and in removing dirt or debris.",100)))
    products_of_org_cursor.execute(cmd_to_insert_products_of_org_values.format(("Spade",250,"It is used for breaking ground and chopping through tree roots and other tough stuff. ",100)))
    products_of_org_database.commit()
else:
    pass

@app.route("/landing_page")
def landing_page():
    return render_template("landing.html")

@app.route("/get_started")
def get_started_page():
    return render_template("get_started.html")

@app.route("/make_organization")
def make_organization_page():
    return render_template("make_organization.html")

@app.route("/contact",methods=["GET","POST"])
def contact_page():
    if request.method == "POST":
        name = request.form.get("name")
        sender_email = request.form.get('email')
        message = request.form.get("message")
        #send_emails(sender_email,message)
        
    return render_template("contact.html")

@app.route("/add_products",methods=["GET","POST"])
def add_products_page():
    if request.method == "POST":
        product_name = request.form.get("product-name")
        product_price = request.form.get("product-price")
        product_description = request.form.get("product-description")
        product_quantity = request.form.get("product-quantity")
        data_of_products_added = (product_name,product_price,product_description,product_quantity)
        print(data_of_products_added)
        products_of_org_cursor.execute(cmd_to_insert_products_of_org_values.format(data_of_products_added))
        products_of_org_database.commit()
    return render_template("add_products.html")

@app.route("/")
@app.route("/home")
def home_page() ->'html':
    return render_template("landing.html")



@app.route("/about")
def about_page() -> 'html':
    return render_template("about.html")

@app.route("/product")
def product_page():
    return render_template("product.html")

@app.route("/schemes")
def schemes_page():
    return render_template("schemes.html")



@app.route("/market_trend_haryana")
def market_trends_haryana_page():
    return render_template("market_trends_haryana.html")

@app.route("/market_trend_delhi")
def market_trends_delhi_page():
    return render_template("market_trends_delhi.html")

@app.route("/market_trend_up")
def market_trends_up_page():
    return render_template("market_trends_up.html")




@app.route("/recommended_seller")
def recommended_seller_page():
    return render_template("recommended_seller.html")

@app.route("/inventory_management",methods=['GET', 'POST'])     #this redirects to the inventory manangemnt page
def inventory_management_page():
    products_of_org_cursor.execute(cmd_to_select_products_of_org)
    data_of_products = products_of_org_cursor.fetchall()
    return render_template("inventory_management.html", item_name_1 = data_of_products[0][0],item_price_1=data_of_products[0][1],item_description_1= data_of_products[0][2], 
                           item_name_2 = data_of_products[1][0],item_price_2=data_of_products[1][1],item_description_2= data_of_products[1][2], item_quantity_2= data_of_products[1][3],
                           item_name_3 = data_of_products[2][0],item_price_3=data_of_products[2][1],item_description_3= data_of_products[2][2], item_quantity_3= data_of_products[2][3],
                           item_name_4 = data_of_products[3][0],item_price_4=data_of_products[3][1],item_description_4= data_of_products[3][2], item_quantity_4= data_of_products[3][3],
                           item_name_5 = data_of_products[4][0],item_price_5=data_of_products[4][1],item_description_5= data_of_products[4][2], item_quantity_5= data_of_products[4][3],
                           item_name_6 = data_of_products[5][0],item_price_6=data_of_products[5][1],item_description_6= data_of_products[5][2], item_quantity_6= data_of_products[5][3],
                           item_name_7 = data_of_products[6][0],item_price_7=data_of_products[6][1],item_description_7= data_of_products[6][2], item_quantity_7= data_of_products[6][3],
                           item_name_8 = data_of_products[7][0],item_price_8=data_of_products[7][1],item_description_8= data_of_products[7][2], item_quantity_8= data_of_products[7][3]) 
@app.route("/user_product")
def user_product_page():
    #file = open("current_user_account.bin","rb")
    return render_template("product.html")

@app.route("/tractor",methods=['GET', 'POST'])
def tractor_page():
    products_of_org_cursor.execute("""UPDATE products_of_org SET QUANTITY = QUANTITY-1 WHERE PRODUCT_NAME ='Tractor';""")
    products_of_org_database.commit()
    return render_template("tractor.html")

@app.route("/plow",methods=['GET', 'POST'])
def plow_page():
    products_of_org_cursor.execute("""UPDATE products_of_org SET QUANTITY = QUANTITY - 1 WHERE PRODUCT_NAME ='Plow';""")
    products_of_org_database.commit()
    return render_template("plow.html")

@app.route("/harvester",methods=['GET', 'POST'])
def harvester_page():
    products_of_org_cursor.execute("""UPDATE products_of_org SET QUANTITY = QUANTITY-1 WHERE PRODUCT_NAME ='Harvester';""")
    products_of_org_database.commit()
    return render_template("harvester.html")

@app.route("/urea",methods=['GET', 'POST'])
def urea_page():
    products_of_org_cursor.execute("""UPDATE products_of_org SET QUANTITY = QUANTITY-1 WHERE PRODUCT_NAME ='Urea';""")
    products_of_org_database.commit()
    return render_template("urea.html")

@app.route("/cultivator",methods=['GET', 'POST'])
def cultivator_page():
    products_of_org_cursor.execute("""UPDATE products_of_org SET QUANTITY = QUANTITY-1 WHERE PRODUCT_NAME ='Cultivator';""")
    products_of_org_database.commit()
    return render_template("cultivator.html")

@app.route("/wheelbarrow",methods=['GET', 'POST'])
def wheelbarrow_page():
    products_of_org_cursor.execute("""UPDATE products_of_org SET QUANTITY = QUANTITY-1 WHERE PRODUCT_NAME ='Wheelbarrow';""")
    products_of_org_database.commit()
    return render_template("wheelbarrow.html")

@app.route("/shovel",methods=['GET', 'POST'])
def shovel_page():
    products_of_org_cursor.execute("""UPDATE products_of_org SET QUANTITY = QUANTITY-1 WHERE PRODUCT_NAME ='Shovel';""")
    products_of_org_database.commit()
    return render_template("shovel.html")

@app.route("/thankyou")
def thank_you_page():
    return render_template("thankyou.html")

@app.route("/orders",methods=['GET', 'POST'])
def orders_page():
    orders_cursor.execute(cmd_to_select_orders)
    data_of_orders = orders_cursor.fetchall()
    return render_template("orders.html", item_name_1 = data_of_orders[1][0],
                           price_1 = data_of_orders[1][1],
                           email_id_1 = data_of_orders[1][2],
                           payment_mode_1 = data_of_orders[1][3],
                           
                           item_name_2 = data_of_orders[2][0],
                           price_2 = data_of_orders[2][1],
                           email_id_2 = data_of_orders[2][2],
                           payment_mode_2 = data_of_orders[2][3],
                           
                           item_name_3 = data_of_orders[2][0],
                           price_3 = data_of_orders[2][1],
                           email_id_3 = data_of_orders[2][2],
                           payment_mode_3 = data_of_orders[2][3],
                           
                           item_name_4 = data_of_orders[3][0],
                           price_4 = data_of_orders[3][1],
                           email_id_4 = data_of_orders[3][2],
                           payment_mode_4 = data_of_orders[3][3],
                           
                           item_name_5 = data_of_orders[4][0],
                           price_5 = data_of_orders[4][1],
                           email_id_5 = data_of_orders[4][2],
                           payment_mode_5 = data_of_orders[4][3])

@app.route("/faqs") 
def faqs_page()->'html':
    return render_template("FAQs.html")

@app.route("/fpo")
def fpo_page():
    return render_template("fpo.html")

@app.route("/item_details_payment",methods=['GET', 'POST'])
def item_details_payment_page():
    if request.method == "POST":
        item_name = request.form.get("item_name")
        price = request.form.get('price')
        email_id = request.form.get('email_id')
        payment_mode = request.form.get('Payment_Mode')
        data_of_orders = (item_name,price,email_id,payment_mode)
        print(data_of_orders)
        orders_cursor.execute(cmd_to_insert_orders_values_specific_columns.format(data_of_orders))
        product_database.commit()
    return render_template("payment.html")

@app.route("/login",methods=['GET', 'POST'])
def login_page():
    if check_existence():
        file = open("current_user_account.bin","rb")
        return render_template("dashboard.html",user_name = pickle.load(file))
    else:
        return render_template("login.html")

@app.route("/weather")
def weather_page():
    return render_template("weather.html")

@app.route("/route")
def report_page():
    return render_template("report.html")

def check_existence():
    farmer_cursor.execute(cmd_to_select)
    list_of_users = farmer_cursor.fetchall()
    email_id = request.form.get('emailid')
    password = request.form.get('password')
    for i in list_of_users:
        if (email_id == i[0]) and (password == i[3]):
            file = open("current_user_account.bin","wb")
            pickle.dump(i[1],file)
            print(email_id,"exists")
            return True
        else:
            return False
    
@app.route("/register",methods=['GET', 'POST'])
def register_page():
    if request.method == "POST":
        first_name = request.form.get("firstname")
        last_name = request.form.get('lastname')
        email_id = request.form.get('emailid')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmpassword')
        if isValid(password) == True:
            if confirm_password == password:
                data_of_new_user = (email_id,first_name,last_name,password)
                farmer_cursor.execute(cmd_to_insert_values_specific_columns.format(data_of_new_user))
                farmers_database.commit()
                return render_template("home.html")
            else:
                return redirect(url_for("register_page"))
        else:
            return redirect(url_for("register_page"))
    return render_template("register.html")

@app.route("/logged_account")
def logged_in_page():
    return render_template("logged_account.html",user_name = pickle.load(file))
app.run()
