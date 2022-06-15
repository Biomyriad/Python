from flask import Flask
from flask_app.config.flask_template_filter import * 

app = Flask(__name__)
app.secret_key = "This is a secret key that No one(1) should know!"
ini_template_filters(app)
