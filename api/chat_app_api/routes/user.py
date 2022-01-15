from flask import Blueprint, jsonify, request

from chat_app_api.models import User, db

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/', methods=['POST'])
def create_user():

    data = request.json
    if data is None:
        return {"error": "No JSON provided"}, 400

    try:
        user = User(**data)
    except TypeError as err:
        return jsonify(error=str(err)), 400

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize), 201


@blueprint.route('/', methods=['GET'])
def list_users():

    users = User.query.order_by(User.created).all()
    return jsonify([user.serialize for user in users]), 200


@blueprint.route('/<user_id>', methods=['GET'])
def get_room(user_id: int):

    user = User.query.get_or_404(user_id)
    return jsonify(user.serialize), 200


@blueprint.route('/<user_id>', methods=['DELETE'])
def delete_room(user_id: int):

    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return '', 204

