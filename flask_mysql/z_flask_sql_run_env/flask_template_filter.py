from flask import Flask

app = Flask(__name__)

@app.template_filter('formatdatetime')
def format_datetime(value, format="%d %b %Y %I:%M %p"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    if value is None:
        return ""
    return value.strftime(format)

def ini_template_filters(app):
    app.jinja_env.filters['formatdatetime'] = format_datetime