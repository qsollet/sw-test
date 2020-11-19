from flask import Flask
from .database import db_session
from .models import Shorturl

app = Flask(__name__)

@app.route('/c/<path:url>')
def create_shorturl(url):
    return f'shorturl from {url}'

@app.route('/<string:shorturl>')
@app.route('/r/<shorturl>')
def redirect_to_url(shorturl):
    return f'shorturl {shorturl}'

@app.route('/d/')
def deprecate_old_shorturl():
    return 'deprecate url'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__=="__main__":
    app.run(debug=True)
