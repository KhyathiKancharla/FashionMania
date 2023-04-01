import pymongo
from flask import *
from pymongo import MongoClient
app = Flask(__name__)
@app.route('/')
def index():
    name = 'SUPPLY CHAIN MANAGEMENT SYSTEM'
    return render_template('base.html',data = name)

@app.route('/newuser')
def newuser():
    return render_template('newuserregister.html')

@app.route("/registeruser",methods=['POST','GET'])
def my_register_user():


    client = MongoClient("mongodb://localhost:27017")



    db=client['SCM']
    info=db.SCM
    register=db.Registered
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    entered_password = entered_password.lower()
    entered_email = request.form.get("email")
    entered_mobileno = request.form.get("mobileno")

    user={"Username":entered_username,"Password":entered_password,"email":entered_email,}
    result = register.insert_one(user)
    print(entered_username,entered_password,entered_email,entered_mobileno)

    if result != None:
        return render_template('Registered_Successfully.html')
    else:
        return "Try again"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/loginuser",methods=['POST','GET'])
def my_login_user():

    client = MongoClient("mongodb://localhost:27017")



    db = client['SCM']
    info=db.SCM
    login=db.Registered
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")

    find = {"Username":entered_username,"Password":entered_password}

    result = login.find_one(find)
    if result is None:
        return "Invaid User Credentials....... Try again"
    else:
        return render_template('sucess.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/planning')
def Planning():
    return render_template('planning.html')

@app.route('/materials')
def materials():
    return render_template('materials.html')

@app.route('/making')
def making():
    return render_template('making.html')

@app.route('/Delivery')
def Delivery():
    return render_template('Delivery.html')

@app.route('/Return')
def Returns():
    return render_template('Return.html')

@app.route('/order')
def order():
    return render_template('place_order.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/bom')
def bom():
    return render_template('bom.html')

@app.route('/vendor_list')
def vendor_list():
    return render_template('vendor_list.html')

@app.route('/warehouse')
def warehouse():
    return render_template('warehouse.html')

if __name__=='__main__':
    app.run(debug=True)