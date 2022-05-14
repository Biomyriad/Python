from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_hi(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:num_times>/<string:message>')
def say_repeat(num_times, message):
    ret_str = ""
    for i in range(1, num_times + 1):
        ret_str += f"{i}: {message} <br>"
    return ret_str

@app.errorhandler(404)
def handle_404(ex):
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)