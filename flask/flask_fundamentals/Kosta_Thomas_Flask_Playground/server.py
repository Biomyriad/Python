from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def route_landing():
    return render_template("index.html", num_block=3, block_color="deepskyblue")

@app.route('/play')
def route_play():
    return render_template("index.html", num_block=3, block_color="deepskyblue")

@app.route('/play/<int:num_block>')
def route_play_num(num_block):
    return render_template("index.html", num_block=num_block, block_color="deepskyblue")

@app.route('/play/<int:num_block>/<string:block_color>')
def route_play_num_color(num_block=3, block_color="deepskyblue"):
    return render_template("index.html", num_block=num_block, block_color=block_color)

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)