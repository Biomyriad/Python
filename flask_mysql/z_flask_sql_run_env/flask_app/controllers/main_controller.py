from flask_app import app
from flask import render_template, request, redirect, url_for, session, flash

from flask_app.models.message import Message
from flask_app.models.user import User

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return redirect("/login") 

@app.route('/dashboard')
def route_dashboard():

    messages = Message.get_messages_by_recipient_id(session['logged_in']['id'])
    users = User.get_all()

    return render_template("pages/dashboard.html", messages=messages, users=users)  

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #

@app.route('/send_message', methods=['POST'])
def route_send_message():

    data = {
        "sender": session["logged_in"]['id'],
        "recipient": request.form['send_to'],
        "message": request.form['message']
    }

    Message.save(data)

    return redirect("/dashboard")

@app.route('/delete_message/<int:message_id>')
def route_delete_message(message_id):

    message = Message.get_by_id(message_id)
    print(f"RECIVED MESSAGE DATA FOR {message_id} - {message}")

    if not message:
        print(f"IF NOT MESSAGE - {message}")        
        return redirect("/dashboard") 

    if message.recipient != session['logged_in']['id']:
        print(f"ID != MESSAGE - {message}")
        return redirect("/WERNING") 
    
    print(f"DELETE - {message}")
    message.delete_by_id(message_id)

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