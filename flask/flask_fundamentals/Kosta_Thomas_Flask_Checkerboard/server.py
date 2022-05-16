from flask import Flask, render_template

app = Flask(__name__)

css_vars = {
    # "--color-1": "one",
}

@app.route('/')
def route_landing():
    return render_template("index.html", y_tiles=8, x_tiles=8, css_vars=css_vars)

@app.route('/<int:y_tiles>')
def route_x_tiles(y_tiles):
    return render_template("index.html", y_tiles=y_tiles, x_tiles=8, css_vars=css_vars)

@app.route('/<int:y_tiles>/<int:x_tiles>')
def route_xy_tiles(x_tiles, y_tiles):
    css_vars["--color-1"] = "red"
    css_vars["--color-2"] = "black"
    return render_template("index.html", y_tiles=y_tiles, x_tiles=x_tiles, css_vars=css_vars)

@app.route('/<int:y_tiles>/<int:x_tiles>/<string:col_1>/<string:col_2>')
def route_xy_tile_color(x_tiles, y_tiles, col_1, col_2):
    css_vars["--color-1"] = col_1
    css_vars["--color-2"] = col_2
    return render_template("index.html", y_tiles=y_tiles, x_tiles=x_tiles, css_vars=css_vars)

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)