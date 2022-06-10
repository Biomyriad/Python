from flask_app import app
from flask_bcrypt import Bcrypt  
bcrypt = Bcrypt(app) 
from flask import render_template, request, redirect, url_for, session, flash

from flask_app.models.user import User

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return redirect("/login") 

@app.route('/login', methods=['POST', 'GET'])
def route_login():

    if request.method == 'GET':
        return render_template("pages/login.html")
    else:
        # LOGIN
        if request.form['action'] == 'login':
            # missing info
            missing_login_info = False
            if request.form['email'] == None or request.form['email'] == "":
                flash({"label": "email", "message": "Please enter an email.", "visibility": ""},"login")
            if request.form['password'] == None or request.form['password'] == "":
                flash({"label": "password", "message": "Please enter your password.", "visibility": ""},"login")
            if missing_login_info:
                return redirect('/login')
            
            # invalid info
            user = User.get_by_email(request.form['email'])
            if not user:
                flash({"label": "email", "message": f"No account found for {request.form['email']}", "visibility": ""},"login")
                return redirect("/login") 
            if not bcrypt.check_password_hash(user.password_hash, request.form['password']):
                flash({"label": "password", "message": "Invalid Password, please try again.", "visibility": ""},"login")
                return redirect('/login')
            
            return redirect("/dashboard") 
        # REGISTER
        else: 

            data = request.form.to_dict()

            is_valid = User.validate_registration(request.form)

            if data['password'] == "" or data['confirm_password'] == "":
                flash({"label": "password", "message": "Must enter a password.", "visibility": ""},"register")
                is_valid = False

            # extra password validations here

            if not data['password'] == data['confirm_password']:
                flash({"label": "confirm_password", "message": "Passwords do not match.", "visibility": ""},"register")
                is_valid = False

            if not is_valid:
                session['show_registration'] = True
                return redirect('/login')

            data["password_hash"] = bcrypt.generate_password_hash(data['password'])
            del data["password"]
            del data["confirm_password"]

            User.save(data)
            return redirect("/dashboard") 

    return render_template("pages/login.html")

@app.route('/dashboard')
def route_dashboard():

    return render_template("pages/dashboard.html")  

@app.route('/delete_email/<int:email_id>')
def route_delete_email(email_id):

    Email.delete_by_id(email_id)

    return redirect(f"/success") 

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #



# # # # # # # # # # #
#   !! Test Routes !!
# # # # # # # # # # #   

@app.route('/test/<int:id>')
def route_test(id):

    return render_template("index.html", css_vars=css_vars)   

@app.route('/clear')
def route_clear():
    session.clear()
    return redirect("/")      

# # # # # # # # # # #
#   Error 
# # # # # # # # # # # 

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."