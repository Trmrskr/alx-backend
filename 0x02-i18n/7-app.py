#!/usr/bin/env python3
'''
    Module for Babel i18n.
'''

from flask_babel import Babel
from pytz import timezone
from flask import Flask, render_template, request, g
from typing import Union

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    '''
        Babel configuration
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    '''
        Get user from session as per variable
    '''
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id), None)
    return None


@app.before_request
def before_request():
    '''
        Operations before request.
    '''
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    '''
        Render template for Babel usage.
    '''
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    '''
        Get user locale.
    '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.header.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    '''
        Get timezone
    '''
    try:
        if request.args.get('timezone'):
            timezone = request.args.get('timezone')
        elif g.user and g.user.get('timezone'):
            timezone = g.user.get('timezone')
        else:
            timezone = app.config['BABEL_DEFAULT_TIMEZONE']

        # check if timezone is a valid timezone using pytz
        tz = timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone


if __name__ == '__main__':
    app.run()
