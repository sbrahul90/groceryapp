from flask import *
import sqlite3

f1 = Flask(__name__)
f1.secret_key = "abc"

@f1.route('/')
def home():
    return render_template('welcomepage.html')

@f1.route('/alogin')
def alogin():
    return render_template('adminlogin.html')

@f1.route('/adminlog',methods=['POST','GET'])
def adminlg():
    email = request.form.get('email')
    pswrd = request.form.get('password')
    if request.method == 'POST':
        if (email == 'admin@grocewheel.com' or email == 'Admin@grocewheel.com') and (pswrd == 'grocewheel'):
            session['email'] = request.form.get('email')
            return render_template('admin_successpage.html')
        else:
            return 'Invalid credentials'

@f1.route('/success')
def suces():
    return render_template('admin_successpage.html')


@f1.route('/adminadd')
def add():
    return render_template('admin_add_product.html')

@f1.route('/add',methods=['POST','GET'])
def addpdt():
    if request.method == 'POST':
        try:
            id = request.form['id']
            pname = request.form['pname']
            brand = request.form['brand']
            price = request.form['price']
            quantity = request.form['quantity']
            category = request.form.get('languages')

            with sqlite3.connect("Product.DB") as cn:
                cur = cn.cursor()
                cur.execute('''insert into _product (id,category,pname,brand,quantity,price) values(?,?,?,?,?,?)''',(id,category,pname,brand,quantity,price))
                cn.commit()

        except:
            cn.rollback()

        finally:
            return render_template('admin_successpage.html')

@f1.route('/productview')
def prod_view():
    cn = sqlite3.connect("Product.DB")
    cn.row_factory = sqlite3.Row
    cur = cn.cursor()
    cur.execute("select * from _product")
    rows = cur.fetchall()
    return render_template("productsview.html", rows=rows)



@f1.route('/ulogin')
def log():
    return render_template('customerlogin.html')


@f1.route('/userlog',methods=['POST','GET'])
def ulog():
    if request.method == 'POST':
        session["em"] = request.form["email"]
        email = request.form['email']
        paswrd= request.form['password']

        with sqlite3.connect("customerdata.DB") as cn:
            cur = cn.cursor()
            dt = cur.execute("Select Email,password from users where Email= ? and password=?",(email,paswrd))
            data = dt.fetchone()

            if data:
                session['email'] = request.form['email']
                return render_template('user_successlogin.html')
            else:
                return "Invalid login"

@f1.route('/user_sucess')
def usucess():
    return render_template('user_successlogin.html')

@f1.route('/register',methods=['POST'])
def ureg():
    return render_template('customer_register.html')

@f1.route('/uadd',methods=['POST'])
def userreg():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['address'] = request.form['address']
        session['age'] = request.form['age']
        session['contact'] = request.form['contact']
        session['email'] = request.form['email']
        session['password'] = request.form['pass']
        session['cpass'] = request.form['cpass']
        session['gender'] = request.form.get("gender")
        return redirect(url_for('savedetails'))

@f1.route('/savedetails')
def savedetails():
    if 'name' in session:
        name=session['name']
        address=session['address']
        age=session['age']
        contact=session['contact']
        email=session['email']
        password=session['password']
        cpass=session['cpass']
        gender=session['gender']
        with sqlite3.connect("customerdata.DB") as cn:
            cur = cn.cursor()
            cur.execute("insert into users (Name,Address,Age,Contact,Email,password,cpassword,gender) values(?,?,?,?,?,?,?,?);",(name,address,age,contact,email,password,cpass,gender))
            cn.commit()
            return render_template("customerlogin.html")


@f1.route('/view',methods=['POST','GET'])
def view():
    cn = sqlite3.connect("customerdata.DB")
    cn.row_factory = sqlite3.Row
    cur = cn.cursor()
    cur.execute("select * from users")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@f1.route('/result', methods=['POST','GET'])
def result():
    Search=request.form["search"]
    if Search=="Dairy" or Search=="dairy" or Search=="DAIRY":
        return redirect(url_for("dairy"))
    elif Search=="Fruits" or Search=="fruits" or Search=="FRUITS" or Search=="Vegetables" or Search=="vegetables" or Search=="VEGETABLES":
        return redirect(url_for("fruits_vegetables"))
    elif Search=="Beverages" or Search=="beverages" or Search=="Beverages":
        return redirect(url_for("Beverages"))
    elif Search=="Bakery" or Search=="bakery" or Search=="BAKERY":
        return redirect(url_for("bakery"))
    elif Search=="Chocolates" or Search=="chocolates" or Search=="CHOCOLATES":
        return redirect(url_for("chocolate"))
    elif Search=="Snacks" or Search=="snacks" or Search=="SNACKS":
        return redirect(url_for("snacks"))
    elif Search=="Pet" or Search=="pet" or Search=="PET":
        return redirect(url_for("petfood"))
    elif Search=="spices" or Search=="Spices" or Search=="SPICES":
        return redirect(url_for("spicemasala"))
    elif Search=="home" or Search=="Home" or Search=="HOME" or Search=="personal" or Search=="Personal" or Search=="PERSONAL":
        return redirect(url_for("home_personal"))

@f1.route('/Dairy',methods=['POST','GET'])
def dairy():
    with sqlite3.connect("Product.DB") as con:
        con.row_factory = sqlite3.Row
        cor = con.cursor()
        cor.execute("select * from _product where category = 'Dairy'")
        rows = cor.fetchall()
        return render_template("cartview.html",rows=rows)


@f1.route('/bakery',methods=['POST','GET'])
def bakery():
    cn = sqlite3.connect("Product.DB")
    cn.row_factory = sqlite3.Row
    cur = cn.cursor()
    cur.execute("select * from _product where category='Bakery' ")
    rows = cur.fetchall()
    return render_template("cartview.html",rows=rows)


@f1.route('/Beverages')
def Beverages():
    cn = sqlite3.connect("Product.DB")
    cn.row_factory = sqlite3.Row
    cur = cn.cursor()
    cur.execute("select * from _product where category='Beverages' ")
    rows = cur.fetchall()
    return render_template("cartview.html",rows=rows)


@f1.route('/fruits_vegetables')
def fruits_vegetables():
    cn = sqlite3.connect("Product.DB")
    cn.row_factory = sqlite3.Row
    cur = cn.cursor()
    cur.execute("select * from _product where category='Fruit_Vegetable' ")
    rows = cur.fetchall()
    return render_template("cartview.html",rows=rows)


@f1.route('/Chocolates')
def chocolate():
    with sqlite3.connect("Product.DB") as con:
        con.row_factory = sqlite3.Row
        cor = con.cursor()
        cor.execute("select * from _product where category = 'Chocolates'")
        rows = cor.fetchall()
        return render_template("cartview.html",rows=rows)


@f1.route('/Snacks')
def snacks():
    with sqlite3.connect("Product.DB") as con:
        con.row_factory = sqlite3.Row
        cor = con.cursor()
        cor.execute("select * from _product where category = 'Snacks'")
        rows = cor.fetchall()
        return render_template("cartview.html",rows=rows)


@f1.route('/spice_masala')
def spicemasala():
    with sqlite3.connect("Product.DB") as con:
        con.row_factory = sqlite3.Row
        cor = con.cursor()
        cor.execute("select * from _product where category = 'Spices & Masalas'")
        rows = cor.fetchall()
        return render_template("cartview.html",rows=rows)


@f1.route('/home_and_personal')
def home_personal():
    cn = sqlite3.connect("Product.DB")
    cn.row_factory = sqlite3.Row
    cur = cn.cursor()
    cur.execute("select * from _product where category='Home and PersonalCare' ")
    rows = cur.fetchall()
    return render_template("cartview.html",rows=rows)


@f1.route('/petfood')
def petfood():
    cn = sqlite3.connect("Product.DB")
    cn.row_factory = sqlite3.Row
    cur = cn.cursor()
    cur.execute("select * from _product where category='Pet food' ")
    rows = cur.fetchall()
    return render_template("cartview.html",rows=rows)


@f1.route('/savekart',methods=['POST'])
def usreg():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['quantity'] = request.form['quantity']
        session['price'] = request.form['price']
        return redirect(url_for('savedcart'))


@f1.route('/savecart')
def savedcart():
    if 'name' in session:
        name= session['name']
        quantity = session['quantity']
        price = session['price']
        tprice = int(quantity)*int(price)
        with sqlite3.connect("customerdata.DB") as cn:
            cur = cn.cursor()
            cur.execute("insert into addcart (pdName,price,quantity) values(?,?,?);",(name,tprice,quantity))
            cn.commit()
            return redirect(url_for('viewcart'))



@f1.route('/viewcart',methods=['POST','GET'])
def viewcart():
    cn = sqlite3.connect("customerdata.DB")
    cn.row_factory = sqlite3.Row
    cur = cn.cursor()
    cur.execute("select * from addcart")
    rows = cur.fetchall()
    return render_template("viewcart.html", rows=rows)


@f1.route('/saveorder',methods=['POST','GET'])
def saveorder():
    if 'name' in session and "email" in session:
        name = session['name']
        quantity = session['quantity']
        price = session['price']
        email = session['em']
        tprice = int(quantity) * int(price)
        with sqlite3.connect("customerdata.DB") as cn:
            cur = cn.cursor()
            cur.execute("insert into vieworder (cName,pdName,quantity, price) values(?,?,?,?)", (email, name, quantity, tprice))
            cn.commit()
            return redirect(url_for('paymentpage'))


@f1.route('/deletecart',methods=['POST','GET'])
def deletecart():
    if request.method == 'POST':
        name = request.form.get('name')
       # session['name']
        with sqlite3.connect("customerdata.DB") as cn:
            cur = cn.cursor()
            cur.execute("DELETE FROM addcart WHERE pdName=?",(name,))
            cn.commit()
    return redirect(url_for("viewcart"))


@f1.route('/payment',methods=['POST','GET'])
def paymentpage():
    return render_template("payment.html")


@f1.route('/paydone',methods=['POST','GET'])
def paydone():
    return render_template("order_review.html")

@f1.route('/vorder')
def vorder():
    cn = sqlite3.connect("customerdata.DB")
    cn.row_factory = sqlite3.Row
    cur = cn.cursor()
    cur.execute("select * from vieworder")
    rows = cur.fetchall()
    return render_template("orderview.html", rows=rows)

if __name__ == '__main__':
    f1.run(debug=True)
