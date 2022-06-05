from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.email import Email

css_vars = {
}

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():

    return render_template("index.html", css_vars=css_vars)

@app.route('/success')
def route_show_emails():

    emails = Email.get_all()

    return render_template("success.html", emails=emails, css_vars=css_vars)  

@app.route('/delete_email/<int:email_id>')
def route_delete_email(email_id):

    Email.delete_by_id(email_id)

    return redirect(f"/success") 

# # # # # # # # # # #
#   Posts
# # # # # # # # # # #

@app.route('/submit_email', methods=['POST'])
def route_submit_email():

    data = {
        'email': request.form['email'],
    }

    if not Email.validate(request.form):
        return redirect('/')

    Email.save(data)

    return redirect(f"/success") 

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