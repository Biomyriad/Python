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

    return render_template("index.html",users=users, css_vars=css_vars)  

@app.route('/users/new')
def route_new_user():

    return render_template("new_user_form.html", css_vars=css_vars)

@app.route('/users/<int:user_id>')
def route_user_info(user_id):

    user = User.get_byid(user_id)

    return render_template("user_details.html", user=user, css_vars=css_vars)

@app.route('/users/<int:user_id>/edit')
def route_user_edit(user_id):

    user = User.get_byid(user_id)

    return render_template("edit_user.html", user=user, css_vars=css_vars)

# # # # # # # # # # #
#   !! Test Routes !!
# # # # # # # # # # #   

@app.route('/test')
def route_test():
    
    return render_template("user_details.html", css_vars=css_vars)     

@app.route('/clear')
def route_clear():
    session.clear()
    return redirect("/")      

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #

@app.route('/newuser', methods=['POST'])
def route_submit():

    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }

    user_id = User.save(data)

    return redirect(f"/users/{user_id}")

@app.route('/users/<int:user_id>/destroy', methods=['POST'])
def route_delete(user_id):

    user_id = User.delete_byid(user_id)

    return redirect(f"/users")

@app.route('/update', methods=['POST'])
def route_update():

    data = {
        'id': request.form['fname'],
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    # UPDATE HERE AND MOD "updated_at" WITH NOW() IN SQL
    user_id = User.update(data)

    return redirect(f"/users/{user_id}")    

# # # # # # # # # # #
#   Error 
# # # # # # # # # # # 

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True, port=5000)

