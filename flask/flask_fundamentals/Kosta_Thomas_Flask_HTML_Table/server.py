from flask import Flask, render_template

app = Flask(__name__)

css_vars = {
}

users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

@app.route('/')
def route_landing():
    tst = len(users)
    return render_template("index.html", users=users, css_vars=css_vars, test=tst)

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)