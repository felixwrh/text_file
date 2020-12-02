from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

app = Flask(__name__, template_folder="template")
app.secret_key = "THIS_IS_A_SECRET_KEY"
ip = "0.0.0.0"
port = "5000"


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get("password")

        with open('password.txt') as file:
            password_list = [line.rstrip("\n") for line in file]
        print(password_list)
        print(password)
        if password not in password_list:
            session["password"] = password
            return redirect(url_for('home_page'))
        return render_template("index.html")
    return render_template("index.html")


@app.route("/home", methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        session.pop('password', None)
        return redirect(url_for('login'))
    else:
        password = session["password"]
        return render_template("home.html", password=password)

if __name__ == '__main__':
    app.run(host=ip, port=port, debug=True)
