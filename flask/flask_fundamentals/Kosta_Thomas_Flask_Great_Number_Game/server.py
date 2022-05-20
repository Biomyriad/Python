from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

css_vars = {
}

highscores = [
]

game_state = {
    "rand_number": 0,
    "num_guesses": 0,
    "guess_ishigh": False,
    "game_ended": False,
    "game_won": False
}

@app.route('/')
def route_landing():
    guess_msg = ""
    css_vars.clear()

    if not 'highscores' in session:
        session['highscores'] = highscores.copy()

    if not 'gamestate' in session:
        session['gamestate'] = game_state.copy()
        session['gamestate']['rand_number'] = random.randint(1, 100)
        print(session['gamestate']['rand_number'])
    else:
        if not session['gamestate']['num_guesses'] == 0:
            if session['gamestate']['game_ended']:
                css_vars['--end_game_box'] = "visible"
                if session['gamestate']['game_won']:
                    # guess_msg = "You Win!"
                    pass
                else:
                    css_vars['--color-1'] = "red"
                    #guess_msg = "You Lose!"
            else:
                css_vars['--guess_box'] = "visible"
                if session['gamestate']['guess_ishigh']:
                    guess_msg = "Too High!"
                else:
                    guess_msg = "Too Low!"

    return render_template("index.html", guess_msg=guess_msg, css_vars=css_vars)

@app.route('/submitguess', methods=['POST'])
def route_submit_guess():
    if request.form['num-guess'].isdigit():
        num_guessed = int(request.form["num-guess"])

        gamestate = session['gamestate']
        gamestate['num_guesses'] = int(gamestate['num_guesses']) + 1

        if num_guessed > int(gamestate['rand_number']):
            gamestate['guess_ishigh'] = True
        elif num_guessed < int(gamestate['rand_number']):
            gamestate['guess_ishigh'] = False
        else:
            gamestate['guess_ishigh'] = False
            gamestate['game_won'] = True
            gamestate['game_ended'] = True

        if gamestate['num_guesses'] == 5:
            gamestate['game_ended'] = True

    session['gamestate'] = gamestate
    return redirect("/")

@app.route('/play', methods=['POST'])
def route_play():
    session.pop('gamestate')
    return redirect("/")

@app.route('/submitscore', methods=['POST'])
def route_submit_score():
    if session['gamestate']['game_won']:
        scores = session['highscores']
        scores[:0] = [{ "name": request.form['name'], "score": session['gamestate']['num_guesses']}]
        session['highscores'] = scores

    session.pop('gamestate')
    return redirect("/")

@app.route('/clear')
def route_clear():
    session.clear()
    return redirect("/")    

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True, port=5000)