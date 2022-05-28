from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

css_vars = {
}

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return redirect("/dojos")

@app.route('/dojos')
def route_dojos():

    all_dojos = Dojo.get_all()

    return render_template("index.html", all_dojos=all_dojos, css_vars=css_vars)  

@app.route('/ninjas')
def route_new_ninja():

    all_dojos = Dojo.get_all()

    return render_template("new_ninja.html", all_dojos=all_dojos, css_vars=css_vars)  

@app.route('/dojos/<int:dojo_id>')
def route_dojo_ninjas(dojo_id):

    dojo_name = Dojo.get_by_id(dojo_id).name
    dojo_ninjas = Ninja.get_all_by_dojo_id(dojo_id)

    return render_template("show_dojo.html", dojo_name=dojo_name, dojo_ninjas=dojo_ninjas, css_vars=css_vars)

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

@app.route('/dojos/new_dojo', methods=['POST'])
def route_new_dojo():

    data = {
        'name': request.form['name']
    }

    user_id = Dojo.save(data)

    return redirect(f"/dojos")

@app.route('/ninjas/new_ninja', methods=['POST'])
def route_update():
    print(request.form)
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    # UPDATE HERE AND MOD "updated_at" WITH NOW() IN SQL
    ninja_id = Ninja.save(data)

    return redirect(f"/dojos/{request.form['dojo_id']}")    

# # # # # # # # # # #
#   Error 
# # # # # # # # # # # 

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."