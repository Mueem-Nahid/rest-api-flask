
# working--------

import jwt
from flask import Flask, jsonify, make_response,request
import datetime
from functools import wraps
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.utils import redirect
from connect_db import search

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms='HS256')
        except:
            return jsonify({'message': 'Token is invalid'}), 403

        return f(*args, **kwargs)
    return decorated

# @app.route('/unprotected')
# def unprotected():
#     return jsonify({'message': 'Anyone can view this'})

# @app.route('/hotel/<title>',methods=['GET'])
# @app.route('/hotel/<title>/<bedroom>', methods=['GET'])
# @app.route('/hotel/<title>/<bedroom>/<bathroom>', methods=['GET'])
# @app.route('/hotel/<title>/<bedroom>/<bathroom>/<sleep>', methods=['GET'])
# @app.route('/hotel/<title>/<bedroom>/<bathroom>/<sleep>/<price>', methods=['GET'])

@app.route('/hotel', methods=['GET'])
def hotel():
    title = request.args.get('title')
    bedroom = request.args.get('bedroom')
    bathroom = request.args.get('bathroom')
    sleep = request.args.get('sleep')
    price = request.args.get('price')
    location = request.args.get('location')
    data=search(title, bedroom, bathroom, sleep, price, location)
    return data

@app.route('/protected')
@token_required
def protected():
    ### swagger specific ###
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Seans-Python-Flask-REST-Boilerplate"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    ### end swagger specific ###

    return redirect("http://127.0.0.1:5000/swagger",code=302)


@app.route("/")
def home():
    return redirect("http://127.0.0.1:5000/login")

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == '1234':
        token =jwt.encode({'user':auth.username,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=20)},app.config['SECRET_KEY'])

        return jsonify({'token':token})
    return make_response('could not varify!', 401, {'WWW-Authenticate': 'Basic realm=Login Required'})


if __name__ == '__main__':
    app.run(debug=False)














### swagger specific ###
# SWAGGER_URL = '/swagger'
# API_URL = '/static/swagger.json'
# SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': "Seans-Python-Flask-REST-Boilerplate"
#     }
# )
# app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###