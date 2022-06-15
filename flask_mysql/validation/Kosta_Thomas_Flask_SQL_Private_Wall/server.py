from flask_app import app

from flask_app.controllers import main_controller
from flask_app.controllers import login_controller

if __name__=="__main__":   
    app.run(debug=True, port=5000)

