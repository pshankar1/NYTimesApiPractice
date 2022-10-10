import flask
from lect5demo import get_headlines
app=flask.Flask(__name__)
@app.route("/")
def index():
    headlines=get_headlines("Try Guys")
    return flask.render_template(
        "index.html",
        headlines=headlines
    )
app.run()