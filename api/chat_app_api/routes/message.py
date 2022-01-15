from flask import Blueprint, jsonify, request

from chat_app_api.models import Room, Message, db

blueprint = Blueprint('message', __name__, url_prefix='/room/<room_id>/message')


@blueprint.route('/', methods=['POST'])
def create_message(room_id: int):

    room = Room.query.get_or_404(room_id)
    data = request.json

    # this should change if actual authentication is implemented
    if 'user_id' not in data:
        return {"error": "No user id provided"}, 400

    try:
        message = Message(**data, room=room)
    except TypeError as err:
        return jsonify(error=str(err)), 400

    db.session.add(message)
    db.session.commit()

    return jsonify(message.serialize), 201


@blueprint.route('/', methods=['GET'])
def list_messages(room_id: int):

    room = Room.query.get_or_404(room_id)
    return jsonify([message.serialize for message in room.messages]), 200


@blueprint.route('/<message_id>', methods=['GET'])
def get_message(room_id: int, message_id: int):

    message = Message.query.filter(Message.room_id == room_id, Message.id == message_id).first_or_404()
    return jsonify(message.serialize), 200


@blueprint.route('/<message_id>', methods=['DELETE'])
def delete_message(room_id: int, message_id: int):

    message = Message.query.filter(Message.room_id == room_id, Message.id == message_id).first_or_404()

    db.session.delete(message)
    db.session.commit()

    return '', 204
