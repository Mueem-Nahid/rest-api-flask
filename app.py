
# working--------

import jwt
from flask import Flask, jsonify, make_response,request
import datetime
from functools import wraps
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.utils import redirect

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

@app.route('/unprotected/<id>',methods=['GET'])
def unprotected2(id):
    print(id)
    return jsonify(id)

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


if __name__ == '__main__':
    app.run(debug=True)
