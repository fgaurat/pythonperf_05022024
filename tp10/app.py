from flask import Flask,render_template
from UserDAO import UserDAO

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/moche")
def users_moche():
    html = ""
    with UserDAO('users_db.db') as dao:
        for user in dao.findAll():
            html+=f"<li>{user.first_name} {user.last_name}</li>"
    
    return f"<ul>{html}</ul>"

# from flask import Flask,render_template
@app.route("/")
def users():
    with UserDAO('users_db.db') as dao:
        data_users = list(dao.findAll())
    
    return render_template(
        "user_list.html",
        users=data_users
        )


