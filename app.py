import os
from website import create_app, db
from flask import Flask, render_template, request, url_for, redirect

basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
