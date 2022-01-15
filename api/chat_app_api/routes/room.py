from flask import Blueprint, jsonify, request

from chat_app_api.models import Room, db

blueprint = Blueprint('room', __name__, url_prefix='/room')


@blueprint.route('/', methods=['POST'])
def create_room():

    data = request.json
    if data is None:
        return {"error": "No JSON provided"}, 400

    try:
        room = Room(**data)
    except TypeError as err:
        return jsonify(error=str(err)), 400

    db.session.add(room)
    db.session.commit()

    return jsonify(room.serialize), 201


@blueprint.route('/', methods=['GET'])
def list_rooms():

    rooms = Room.query.order_by(Room.created).all()
    return jsonify([room.serialize for room in rooms]), 200


@blueprint.route('/<room_id>', methods=['GET'])
def get_room(room_id: int):

    room = Room.query.get_or_404(room_id)
    return jsonify(room.serialize), 200


@blueprint.route('/<room_id>', methods=['DELETE'])
def delete_room(room_id: int):

    room = Room.query.get_or_404(room_id)

    db.session.delete(room)
    db.session.commit()

    return '', 204
