from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

css_vars = {
}

@app.route('/')
def route_landing():
    return render_template("index.html", css_vars=css_vars)

@app.route('/result')
def route_results():
    return render_template("result.html", css_vars=css_vars)

@app.route('/submit', methods=['POST'])
def route_submit():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_lang'] = request.form['fav_lang']
    use1 = request.form['usage1'] if 'usage1' in request.form else ""
    use2 = request.form['usage2'] if 'usage2' in request.form else ""
    if use1 and use2:
        session['usage'] = f"{use1}, {use2}"
    else:
        session['usage'] = f"{use1}{use2}"
    session['level_exp'] = request.form['level_exp']
    session['comments'] = request.form['comments']
    return redirect("/result")

@app.route('/clear')
def route_clear():
    session.clear()
    return redirect("/")    

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True, port=5000)
