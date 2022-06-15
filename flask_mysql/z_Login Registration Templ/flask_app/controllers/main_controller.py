from flask_app import app
from flask import render_template, request, redirect, url_for, session, flash

from flask_app.models.user import User

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return redirect("/login") 

@app.route('/dashboard')
def route_dashboard():

    return render_template("pages/dashboard.html")  

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #


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