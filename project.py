from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")
    

@app.route("/page/")
def msg():
    return render_template("login.html")


@app.route("/formlogin", methods=['GET'])
def login():
    uname = request.args.get("uname")
    password = request.args.get("pass")

    if uname =="dipakbhagat" and password=="dipak123":
        return "welcome %s" % uname
    else:
        return "Try again"


if __name__ == "__main__":
    app.run(debug=True)