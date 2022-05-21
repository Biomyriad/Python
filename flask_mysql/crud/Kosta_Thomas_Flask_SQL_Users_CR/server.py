from optparse import Values
from flask import Flask, render_template, request, redirect, session
from flask_template_filter import * 

# ---
from users import User

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
ini_template_filters(app)

css_vars = {
}

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return redirect("/users")

@app.route('/users')
def route_users():

    users = User.get_all()

    for row in users:
        for key, value in vars(row).items():
            print(f"{key} -> {value}")

    return render_template("index.html",users=users, css_vars=css_vars)  

@app.route('/users/new')
def route_new_user():

    return render_template("new_user_form.html", css_vars=css_vars)

@app.route('/clear')
def route_clear():
    session.clear()
    return redirect("/")      

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #

@app.route('/submit', methods=['POST'])
def route_submit():

    print(request.form)

    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }

    User.save(data)

    return redirect("/users")

# # # # # # # # # # #
#   Error 
# # # # # # # # # # # 

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True, port=5000)

