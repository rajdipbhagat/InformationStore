from distutils.log import error
from flask import Flask, render_template, request,redirect

app = Flask(__name__)


em_list=[]

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/")
def sss():
    return render_template ("login.html")


# Login and visit welcome message class define
    
@app.route("/page/")
def login_page_link():
    return render_template("login.html")

@app.route("/formlogin", methods=['GET'])
def login():
    uname = request.args.get("uname")
    password = request.args.get("pass")

    if uname =="dipakbhagat" and password=="dipak123":
        return "welcome %s" % uname
    else:
        error = "Invalid UserName Or Password !"
        return render_template('login.html', error=error)



# register data and show data class define
@app.route("/register/")
def register_page_link():
    return render_template("register.html")

@app.route("/success", methods=['POST'])
def show():
    info = request.form
    return render_template("result.html", result=info)

    

@app.route("/get/all/emp")
def emp_fetch():
    return {"all_emp":em_list}
    #em_list.append()

    





if __name__ == "__main__":
    app.run(debug=True)