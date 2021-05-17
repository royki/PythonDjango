from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ewawsdb.db'
db = SQLAlchemy(app)

from productlist import routes
