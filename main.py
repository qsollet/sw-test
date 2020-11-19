from flask import Flask, redirect, abort
from .database import db_session
from .models import Shorturl
from datetime import datetime, timedelta
from decouple import config

app = Flask(__name__)
app.config['DEPRATED_AFTER'] = config('DEPRECATED_AFTER', default='30', cast=int)

@app.route('/c/<path:url>')
def create_shorturl(url):
    s = Shorturl(url)
    app.logger.debug(f'Creating shorturl {s.id}')
    db_session.add(s)
    db_session.commit()
    return f'Shorturl: <a href="/{s.id}">/{s.id}</a>'

@app.route('/<string:shorturl_id>')
@app.route('/r/<string:shorturl_id>')
def redirect_to_url(shorturl_id):
    try:
        s = Shorturl.query.filter(Shorturl.id == shorturl_id).first()
        s.accessed += 1
        db_session.add(s)
        db_session.commit()
        app.logger.debug(f'Redirecting user to {s.url}')
        return redirect(s.url)
    except:
        abort(404)

@app.route('/d/')
def deprecate_old_shorturl():
    # In our case we'll define a shorturl deprecated if not accessed in the last x days
    filter_before = datetime.today() - timedelta(days = app.config['DEPRATED_AFTER'])
    shorturls = Shorturl.query.filter(Shorturl.updated_at < filter_before).all()
    for s in shorturls:
        db_session.delete(s)
    db_session.commit()
    app.logger.debug(f'Deleted {len(shorturls)} shorturl')
    return f'{len(shorturls)} shorturls deprecated'

@app.route('/l/')
def list_shorturl():
    shorturls = Shorturl.query.all()
    return {'shorturls': [{
        'id': s.id,
        'url': s.url,
        'accessed': s.accessed,
        'created_at': s.created_at,
        'updated_at': s.updated_at
    } for s in shorturls]}

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__=="__main__":
    app.run(debug=True)
