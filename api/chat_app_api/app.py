from flask import Flask, jsonify
from flask_cors import CORS

from chat_app_api.models import db
from chat_app_api.routes.room import blueprint as room
from chat_app_api.routes.message import blueprint as message
from chat_app_api.routes.user import blueprint as user

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgrespasswd@postgres:5432/chat_app'
app.url_map.strict_slashes = False

db.init_app(app)

app.register_blueprint(room)
app.register_blueprint(message)
app.register_blueprint(user)


@app.errorhandler(404)
def resource_not_found(err):
    return jsonify(error=str(err)), 404


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    return "pong", 200
