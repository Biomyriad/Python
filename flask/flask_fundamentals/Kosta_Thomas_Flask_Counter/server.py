from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

css_vars = {
}

@app.route('/')
def route_landing():
    if not "visit-count" in session:
        session["visit-count"] = 1
    else:
        session["visit-count"] += 1

    if not "count" in session:
        session["count"] = 1
        session["count-by"] = 1
    elif "cnt_by_2" in session:
        session.pop("cnt_by_2")
        session["count"] += 2
    else:
        session["count"] += int(session["count-by"])
    return render_template("index.html", css_vars=css_vars)

@app.route('/count', methods=['POST'])
def route_post_count():

    session["count-by"] = request.form["count-by"]

    if request.form["action"] == "count-by-two":
        session["cnt_by_2"] = ""
    elif request.form["action"] == "reset":
        session.clear()
    return redirect("/")

@app.route('/destroy_session')
def route_destroy():
    session.clear()
    return redirect("/")

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)