from flask_app import app
from flask_bcrypt import Bcrypt  
bcrypt = Bcrypt(app) 
from flask import render_template, request, redirect, url_for, session, flash

from flask_app.models.user import User

# set on valid login/register URL string
valid_login_url = "/dashboard"
valid_login_template_path = "pages/dashboard.html"

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/logout')
def route_logout():

    del session["logged_in"]

    return redirect("/") 

@app.route('/login', methods=['POST', 'GET'])
def route_login():

    if request.method == 'GET':
        if "logged_in" in session:
            return render_template(valid_login_template_path)
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
            
            session['logged_in'] = {
                "id": user.id,
                "first_name": user.first_name,
                "email": user.email
            }
            return redirect(valid_login_url) 
        # REGISTER
        else: 

            data = {}
            data['first_name'] = request.form['first_name'].capitalize()
            data['last_name'] = request.form['last_name'].capitalize()
            data['email'] = request.form['email']


            is_valid = User.validate_registration(request.form)

            if request.form['password'] == "" or request.form['confirm_password'] == "":
                flash({"label": "password", "message": "Must enter a password.", "visibility": ""},"register")
                is_valid = False

            # extra password validations here

            if not request.form['password'] == request.form['confirm_password']:
                flash({"label": "confirm_password", "message": "Passwords do not match.", "visibility": ""},"register")
                is_valid = False

            if not is_valid:
                # set a temp session variable so that page will display registration on load
                #   - session variable will be removed in page jinja onload
                session['show_registration'] = True
                flash(data, "registration_form_data")
                return redirect('/login')

            data["password_hash"] = bcrypt.generate_password_hash(request.form['password'])

            User.save(data)

            session['logged_in'] = {
                "id": user.id,
                "first_name": user.first_name,
                "email": user.email
            }
            return redirect(valid_login_url) 
# End of ROUTE_LOGIN  

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #
