# PostGrid, the PostgreSQL Viewer
# Written by Alexander Yauchler (terminatedNULL)
# Project Span : 7/29/2024 - ##/##/####

from flask import Flask, render_template, request, redirect, flash
from flaskwebgui import FlaskUI
import psycopg2

app = Flask(__name__)
app.secret_key = "b(&A^90>>.,/ASDF(*&65#%$@~``~"


@app.route('/auth', methods=["GET"])
def auth():
    return render_template("index.html")


@app.route('/')
def index():
    return redirect("/auth")


@app.route('/auth_bridge', methods=["POST"])
def authBridge():  # Attempts to connect to the database
    data = request.form

    # Check if database is using a password
    try:
        if len(data["dbPass"]) != 0:
            conn = psycopg2.connect(
                dbname=data["dbName"],
                user=data["dbUser"],
                port=int(data["dbPort"]),
                host=data["dbHost"],
                password=data["dbPass"]
            )
        else:
            conn = psycopg2.connect(
                dbname=data["dbName"],
                user=data["dbUser"],
                port=data["dbPort"],
                host=data["dbHost"]
            )
    except psycopg2.Error as err:
        flash("Authentication Failed!")
        return redirect("/auth")

    cur = conn.cursor()

    return render_template("terminal.html")


if __name__ == '__main__':
    FlaskUI(app=app, server="flask", width=1000, height=500).run()
