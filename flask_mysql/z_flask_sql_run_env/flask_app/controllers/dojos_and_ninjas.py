from unittest import result
from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.author import Author
from flask_app.models.book import Book

css_vars = {
}

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return redirect("/authors")

@app.route('/authors')
def route_authors():

    authors = Author.get_all()

    return render_template("index.html", authors=authors , css_vars=css_vars)

@app.route('/authors/<int:author_id>')
def route_authors_favorites(author_id):

    data = { "id": author_id }
    result = Author.test(data)

    author = result[0]
    un_fav_books = result[1]

    return render_template("authors_favorites.html", author=author, un_fav_books=un_fav_books, css_vars=css_vars) 

@app.route('/books')
def route_books():

    books = Book.get_all()

    return render_template("new_book.html", books=books, css_vars=css_vars)  

# @app.route('/dojos/<int:dojo_id>')
# def route_dojo_ninjas(dojo_id):

#     dojo_name = Dojo.get_by_id(dojo_id).name
#     dojo_ninjas = Ninja.get_all_by_dojo_id(dojo_id)

#     return render_template("show_dojo.html", dojo_name=dojo_name, dojo_ninjas=dojo_ninjas, css_vars=css_vars)

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
#   Posts
# # # # # # # # # # #

@app.route('/authors/new_author', methods=['POST'])
def route_new_author():

    data = {
        'name': request.form['name']
    }

    author_id = Author.save(data)

    return redirect(f"/authors")

@app.route('/books/new_book', methods=['POST'])
def route_new_book():

    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }

    book_id = Book.save(data)

    return redirect(f"/books")

# @app.route('/ninjas/new_ninja', methods=['POST'])
# def route_update():
#     print(request.form)
#     data = {
#         'fname': request.form['fname'],
#         'lname': request.form['lname'],
#         'age': request.form['age'],
#         'dojo_id': request.form['dojo_id']
#     }
#     # UPDATE HERE AND MOD "updated_at" WITH NOW() IN SQL
#     ninja_id = Ninja.save(data)

#     return redirect(f"/dojos/{request.form['dojo_id']}")    

# # # # # # # # # # #
#   Error 
# # # # # # # # # # # 

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."