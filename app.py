'''
Created on 
Course work: 
@author: farmaan
Source:
'''
from flask import Flask, render_template, session, redirect, url_for, request, flash, json
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "2c51632ef45ce4571cfc487133a14273"
client = MongoClient('localhost',27017)
db = client['feat']


user_collection = db["users"]
employer_collection = db["employers"]
employer_req_collection = db["employer_req"]
engage_reqs_collection = db["engage_reqs"]

def get_one_emp_reqid(reqid):
    emp_req = employer_req_collection.find_one({"reqid": reqid}, {"reqid": 1})
    return emp_req

def get_all_emp_reqid():
    emp_req = employer_req_collection.find({}, {"reqid": 1})
    return emp_req

def view_one_emp_req_details(reqid):
    view_one_emp_req_details = employer_req_collection.find_one({"reqid":int(reqid)})
    return view_one_emp_req_details

def view_all_emp_req_details():
    view_emp_req_details = list(employer_req_collection.find())
    return view_emp_req_details

def get_engaged_by(reqid):
    engaged_by_list = list(engage_reqs_collection.distinct('engaged_by', {'reqid': int(reqid)}))
    return engaged_by_list

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         session["username"] = username

#         # Check if username exists in the database
#         username_found = user_collection.find_one({"username": username})
#         print(username_found)
#         new_username_found = username_found['username']
#         print(new_username_found)
#         if new_username_found == username:
#             flash("Featurepreneur Login Successful")
#             return redirect(url_for('dashboard', username = username))
#     else:
#         if "username" in session:
#              flash("Already Logged In")
#              return redirect(url_for("dashboard"))
#         return render_template('login.html')

@app.route("/emp/login", methods=["POST", "GET"])
def empLogin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        session["emp_username"] = username

        # Check if username exists in the database
        emp_username_found = employer_collection.find_one({"username": username})
        print(emp_username_found)
        new_emp_username_found = emp_username_found['username']
        print(new_emp_username_found)
        if new_emp_username_found == username:
            flash("Employer Login Successful")
            return redirect(url_for('empDashboard', username = username))
    else:
        if "emp_username" in session:
             flash("Already Logged In")
             return redirect(url_for("empDashboard"))
        return render_template('empLogin.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

@app.route('/emp/dashboard')
def empDashboard():
    username = session["emp_username"]
    return render_template('empDashboard.html', username=username)

@app.route("/emp/logout", methods=["POST", "GET"])
def empLogout():
    if "emp_username" in session:
        session.pop("emp_username", None)
        return render_template("empLogout.html")
    else:
        return render_template('index.html')

@app.route("/view")
def view_all_emp_req():
    view_emp_req=view_all_emp_req_details()
    return render_template("view.html", view=view_emp_req)

@app.route("/view/req/<reqid>")
def view_one_emp_req(reqid):
    view_one_emp_req = view_one_emp_req_details(reqid)
    return render_template("view_one_req.html", view=view_one_emp_req)

@app.route("/view/req/engaged/<reqid>")
def view_req_engaged(reqid):
    engaged_by = get_engaged_by(reqid)
    engaged_by_count = len(engaged_by)
    return render_template('engaged_by.html', engaged_by_list=engaged_by, count = engaged_by_count)

# reqid = 28003
# def insert_add_req_details(title,content):
#     add_req_dict = {'reqid': reqid,'title':title,'content':content}
#     employer_req_collection.insert_one(add_req_dict)

@app.route("/emp/add/req", methods=["POST", "GET"])
def addReq():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        print(title, content)
        insert_add_req_details(title,content)
        return render_template("empDashboard.html")
    return render_template("addReq.html")

if __name__ == "__main__":
    app.run(debug=True)