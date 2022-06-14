from email.policy import default
from flask import Flask

app = Flask(__name__)

@app.template_filter('formatdatetime')
def format_datetime(value, format="%d %b %Y %-I:%M %p"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    if value is None:
        return ""
    return value.strftime(format)

@app.template_filter('index')
def element_by_index(value, index):
    """Return an element at index"""
    if value is None or value == "":
        return ""
    return value[int(index)]

@app.template_filter('get_validation_message')
def get_validation_message(messages, msg_label, default_return=""):
    if messages is None or messages == "":
        return default_return
    if msg_label is None or msg_label == "":
        return default_return

    for msg in messages:
        if "label" in msg and msg['label'] == msg_label:
            return msg['message']

    return default_return

@app.template_filter('get_validation_visibility')
def get_validation_visibility(messages, msg_label):
    if messages is None or messages == "":
        return ""
    if msg_label is None or msg_label == "":
        return ""

    for msg in messages:
        if "label" in msg and msg['label'] == msg_label:
            return ""

    return "hidden"


    

def ini_template_filters(app):
    app.jinja_env.filters['formatdatetime'] = format_datetime
    app.jinja_env.filters['index'] = element_by_index
    app.jinja_env.filters['get_validation_message'] = get_validation_message
    app.jinja_env.filters['get_validation_visibility'] = get_validation_visibility