from optparse import Values
from flask import Flask, render_template, request, redirect, session

# ---
from friend import Friend

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

css_vars = {
}

@app.route('/')
def route_landing():

    friends = Friend.get_all()

    for row in friends:
        for key, value in vars(row).items():
            print(f"{key} -> {value}")

    return render_template("index.html", css_vars=css_vars)

@app.route('/submit', methods=['POST'])
def route_submit():

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
