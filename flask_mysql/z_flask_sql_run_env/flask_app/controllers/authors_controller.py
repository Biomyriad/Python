from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.author import Author
from flask_app.models.favorites import Favorites

css_vars = {
}

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/authors')
def route_authors():

    authors = Author.get_all()

    return render_template("index.html", authors=authors , css_vars=css_vars)

@app.route('/authors/<int:author_id>')
def route_authors_favorites(author_id):

    result = Author.get_authors_fav_books(author_id)

    author = result[0]
    un_fav_books = result[1]

    return render_template("authors_favorites.html", author=author, un_fav_books=un_fav_books, css_vars=css_vars) 

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #

@app.route('/authors/new_author', methods=['POST'])
def route_new_author():

    data = {
        'name': request.form['name']
    }

    Author.save(data)

    return redirect(f"/authors")

@app.route('/authors/add_fav_book', methods=['POST'])
def route_add_fav_book():
    
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }

    Favorites.save(data)

    return redirect(f"/authors/{request.form['author_id']}")   
