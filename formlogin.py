from flask import Flask, render_template, request, url_for,redirect

app= Flask(__name__)

@app.route("/")
def sss():
    return render_template ("login.html")

@app.route("/formlogin", methods=['GET'])
def login():
    uname = request.args.get("uname")
    password = request.args.get("pass")

    if uname =="dipakbhagat" and password=="dipak123":
        return "welcome %s" % uname
    else:
        return redirect(url_for("sss"))
"""

@app.route("/formlogin", methods=['POST'])
def login():
    uname = request.form["uname"]
    password = request.form["pass"]

    if uname =="dipakbhagat" and password=="dipak123":
        return "welcome %s" % uname
    else:
        return "Try again"

"""




if __name__ =="__main__":
    app.run(debug=True)