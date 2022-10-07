import flask
from lect5demo import get_headlines
app=flask.Flask(__name__)
#app= python decorater if you visit the app at this location this is what you get back
@app.route("/")
def index():
    headlines=get_headlines("Try Guys")
    return headlines
app.run()