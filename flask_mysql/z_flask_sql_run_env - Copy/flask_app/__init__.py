from flask import Flask
from flask_app.config.flask_template_filter import * 

app = Flask(__name__)
app.secret_key = "shhhhhh"
ini_template_filters(app)
