from flask import Flask, redirect, abort
from .database import db_session
from .models import Shorturl

app = Flask(__name__)

@app.route('/c/<path:url>')
def create_shorturl(url):
    s = Shorturl(url)
    db_session.add(s)
    db_session.commit()
    return f'Shorturl: <a href="/{s.id}">/{s.id}</a>'

@app.route('/<string:shorturl_id>')
@app.route('/r/<string:shorturl_id>')
def redirect_to_url(shorturl_id):
    try:
        s = Shorturl.query.filter(Shorturl.id == shorturl_id).first()
        return redirect(s.url)
    except:
        abort(404)

@app.route('/d/')
def deprecate_old_shorturl():
    return 'deprecate url'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__=="__main__":
    app.run(debug=True)
