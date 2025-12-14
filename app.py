from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os
import bcrypt

app = Flask(__name__)
app.secret_key = "secret_key_tau"  # đổi cũng được

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DB_NAME"),
        port=int(os.environ.get("DB_PORT"))
    )

@app.route("/")
def home():
    return redirect("/login")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode()

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and bcrypt.checkpw(password, user["password"].encode()):
            session["user"] = user["username"]
            session["role"] = user["role"]
            return redirect("/admin")

        return "❌ Sai tài khoản hoặc mật khẩu"

    return render_template("login.html")

# ---------- ADMIN ----------
@app.route("/admin")
def admin():
    if "user" not in session or session["role"] != "admin":
        return redirect("/login")

    return render_template("admin.html", user=session["user"])

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------- PING ----------
@app.route("/ping")
def ping():
    return "OK"

if __name__ == "__main__":
    app.run()
