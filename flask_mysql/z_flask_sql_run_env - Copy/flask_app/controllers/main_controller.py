from flask_app import app
from flask import render_template, request, redirect, session

# imports here for testing...
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorites import Favorites

css_vars = {
}

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return redirect("/authors")

# # # # # # # # # # #
#   !! Test Routes !!
# # # # # # # # # # #   

@app.route('/test')
def route_test():

    result = Author.test(4)

    author = result[0]
    un_fav_books = result[1]
    print(un_fav_books)
    
    return render_template("authors_favorites.html", author=author, un_fav_books=un_fav_books, css_vars=css_vars)     

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