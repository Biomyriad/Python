from flask_app import app
from flask import render_template, request, redirect, url_for, session, flash

from flask_app.models.user import User
from flask_app.models.recipe import Recipe

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return redirect("/login") 

@app.route('/dashboard')
def route_dashboard():

    recipes = Recipe.get_all()

    return render_template("pages/dashboard.html", recipes=recipes)  

    # RECIPES ROUTE ##################

@app.route('/recipes/new')
def route_new():

    return render_template("pages/new_recipe.html") 

@app.route('/recipes/edit/<int:recipe_id>')
def route_edit(recipe_id):

    session['edit_recipe_id'] = recipe_id

    recipe = Recipe.get_by_id(recipe_id)
    recipe.date_made = recipe.date_made.date()

    return render_template("pages/edit_recipe.html", recipe=recipe) 

@app.route('/recipes/<int:recipe_id>')
def route_view(recipe_id):

    recipe = Recipe.get_by_id(recipe_id)
    recipe.date_made = recipe.date_made.date()

    print(recipe.date_made)

    return render_template("pages/view_recipe.html", recipe=recipe) 

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #

@app.route('/submit_recipe', methods=['POST'])
def route_create_recipe():

    data = request.form.to_dict()
    data["is_under_30min"] = 1 if data["is_under_30min"] == "True" else 0
    data['posted_by'] = session['logged_in']['id']

    if not Recipe.validate_recipe(data):
        return redirect("/recipes/new") 

    if 'logged_in' in session:
        Recipe.save(data)

    return redirect("/recipes/new") 
    # return redirect("/dashboard")  

@app.route('/update_recipe', methods=['POST'])
def route_update_recipe():

    recipe = Recipe.get_by_id(session["edit_recipe_id"])
    print("get recipe ------------")
    del session["edit_recipe_id"]

    data = request.form.to_dict()
    data["is_under_30min"] = 1 if data["is_under_30min"] == "True" else 0
    data["posted_by"] = recipe.posted_by_id
    data["id"] = recipe.id

    if not Recipe.validate_recipe(data):
        return redirect(f"/recipes/edit/{recipe.id}")     

    if session['logged_in']['id'] == recipe.posted_by_id:
        Recipe.update(data)

    return redirect("/dashboard") 

@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
def route_delete_recipe(recipe_id):

    recipe = Recipe.get_by_id(recipe_id)

    if session['logged_in']['id'] == recipe.posted_by_id:
        Recipe.delete_by_id(recipe_id)

    return redirect("/dashboard")  



# # # # # # # # # # #
#   !! Test Routes !!
# # # # # # # # # # #   

# @app.route('/test/<int:id>')
# def route_test(id):
#     return render_template("index.html", css_vars=css_vars)   

@app.route('/clear')
def route_clear():
    session.clear()
    return redirect("/")      

# # # # # # # # # # #
#   Error 
# # # # # # # # # # # 

@app.errorhandler(404)
def handle_404(ex):
    return render_template("pages/error_pages/404_error.html")  

@app.errorhandler(500)
def handle_500(ex):
    return render_template("pages/error_pages/500_error.html")  