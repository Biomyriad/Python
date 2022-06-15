from flask_app import app
from flask_bcrypt import Bcrypt  
bcrypt = Bcrypt(app) 
from flask import render_template, request, redirect, url_for, session, flash

from flask_app.models.user import User

# set on valid login/register URL string
valid_login_url = "/dashboard"

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
            return redirect(valid_login_url) 
        return render_template("pages/login.html")
    else:
        
        # LOGIN
        if request.form['action'] == 'login':

            session_data = User.validate_login(request.form)
            if not session_data:
                return redirect('/login')

            session['logged_in'] = session_data
            return redirect(valid_login_url) 

        # REGISTER
        else: 

            data = {}
            data['first_name'] = request.form['first_name'].capitalize()
            data['last_name'] = request.form['last_name'].capitalize()
            data['email'] = request.form['email'].lower()

            if not User.validate_registration(request.form):
                # set a temp session variable so that page will display registration on load
                #   - session variable will be removed in page jinja onload
                session['show_registration'] = True
                flash(data, "registration_form_data")
                return redirect('/login')

            data["password_hash"] = bcrypt.generate_password_hash(request.form['password'])

            user_id = User.save(data)

            session['logged_in'] = {
                "id": user_id,
                "first_name": data['first_name'],
                "email": data['email']
            }
            return redirect(valid_login_url) 
# End of ROUTE_LOGIN  

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #
