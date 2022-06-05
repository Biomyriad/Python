from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.dojo import Dojo

css_vars = {
}

# # # # # # # # # # #
#   Routes 
# # # # # # # # # # #

@app.route('/')
def route_landing():
    return render_template("index.html", css_vars=css_vars)

@app.route('/result/<int:survey_id>')
def route_results(survey_id):
    survey = Dojo.get_by_id(survey_id)
    return render_template("result.html", survey=survey, css_vars=css_vars)

@app.route('/submit', methods=['POST'])
def route_submit():

    data = {}
    print(request.form)

    if not Dojo.validate(request.form):
        return redirect('/')

    data['name'] = request.form['name']
    data['location'] = request.form['location']
    data['language'] = request.form['language']
    data['comment'] = request.form['comment']

    survey_id = Dojo.save(data)

    # return redirect(f"/")    
    return redirect(f"/result/{survey_id}")  

# # # # # # # # # # #
#   !! Test Routes !!
# # # # # # # # # # #      

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