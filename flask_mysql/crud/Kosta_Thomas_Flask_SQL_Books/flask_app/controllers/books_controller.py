from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.book import Book
from flask_app.models.favorites import Favorites

css_vars = {
}

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/books')
def route_books():

    books = Book.get_all()

    return render_template("new_book.html", books=books, css_vars=css_vars)  

@app.route('/books/<int:books_id>')
def route_books_favorites(books_id):

    result = Book.get_books_fav_by_author(books_id)

    book = result[0]
    authors_not_fav_book = result[1]

    return render_template("books_favorites.html", book=book, authors_not_fav_book=authors_not_fav_book, css_vars=css_vars)    

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #

@app.route('/books/new_book', methods=['POST'])
def route_new_book():

    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }

    Book.save(data)

    return redirect(f"/books")  

@app.route('/books/add_author_to_book', methods=['POST'])
def route_add_author_to_book():
    
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }

    Favorites.save(data)

    return redirect(f"/books/{request.form['book_id']}")  
