from flask_app import app
from flask import render_template, request, redirect, url_for, session, flash

from flask_app.models.email import Email

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return redirect("/login") 

@app.route('/login', methods=['POST', 'GET'])
def route_login():

    if request.method == 'GET':
        return render_template("pages/login.html")
    else:
        pass
        # data = {
        #     'email': request.form['email'],
        # }
        # if Email.validate(request.form):
        #     # Email.save(data)
        #     return redirect("/success")

    test = {
        "hello": "yup",
        "bye": 77
    }

    flash(test,"login2",)
    flash("login","login")
    flash("reg","register")
        
    return render_template("pages/login.html")
    # return redirect(url_for('success',name = "xxxx"))
    # return redirect("/success")

@app.route('/success')
def route_show_emails():

    emails = Email.get_all()

    return render_template("success.html", emails=emails)  

@app.route('/delete_email/<int:email_id>')
def route_delete_email(email_id):

    Email.delete_by_id(email_id)

    return redirect(f"/success") 

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #



# # # # # # # # # # #
#   !! Test Routes !!
# # # # # # # # # # #   

@app.route('/test/<int:id>')
def route_test(id):

    return render_template("index.html", css_vars=css_vars)   

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