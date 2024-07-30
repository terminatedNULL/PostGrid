# PostGrid, the PostgreSQL Viewer
# Written by Alexander Yauchler (terminatedNULL)
# Project Span : 7/29/2024 - ##/##/####

from flask import Flask, render_template, request, redirect
from flaskwebgui import FlaskUI
import psycopg2

app = Flask(__name__)


@app.route('/auth/<state>')
def auth(state):
    return render_template("index.html", authState=state)


@app.route('/')
def index():
    return redirect("/auth/clean")


@app.route('/auth_bridge', methods=["GET"])
def authBridge():
    if request.method == "GET":
        # Attempt to connect to the database
        # Check if database is using a password
        try:
            if request.form.get("passReq") == "1":
                conn = psycopg2.connect(
                    dbname=request.form.get("dbName"),
                    user=request.form.get("dbUser"),
                    port=request.form.get("dbPort"),
                    password=request.form.get("dbPass")
                )
            else:
                conn = psycopg2.connect(
                    dbname=request.form.get("dbName"),
                    user=request.form.get("dbUser"),
                    port=request.form.get("dbPort")
                )
        except psycopg2.Error as err:
            return redirect("/auth/return")

        return render_template("terminal.html")


if __name__ == '__main__':
    FlaskUI(app=app, server="flask", width=1000, height=500).run()
