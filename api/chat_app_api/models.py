from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db: SQLAlchemy = SQLAlchemy()
SQLAlchemyBaseModel = db.Model


class Room(SQLAlchemyBaseModel):

    __tablename__ = "room"

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False, default=True, server_default='t')
    created = db.Column(db.DateTime, default=datetime.now(), nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, nullable=True)
    name = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return '<Room id={!r}>'.format(self.id)

    @property
    def serialize(self):

        return {
            "id": self.id,
            "active": self.active,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat() if self.updated else self.updated,
            "name": self.name
        }


class User(SQLAlchemyBaseModel):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.now(), nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, nullable=True)
    name = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return '<User id={!r}>'.format(self.id)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat() if self.updated else self.updated,
            "name": self.name
        }


class Message(SQLAlchemyBaseModel):

    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False, default=True, server_default='t')
    created = db.Column(db.DateTime, default=datetime.now(), nullable=False, server_default=func.now())
    updated = db.Column(db.DateTime, nullable=True)
    content = db.Column(db.Text, nullable=True)

    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    room = db.relationship('Room', backref=db.backref('messages', lazy=True))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('messages', lazy=True))

    def __repr__(self) -> str:
        return '<Message id={!r}>'.format(self.id)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "active": self.active,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat() if self.updated else self.updated,
            "content": self.content,
            "room_id": self.room_id,
            "user_id": self.user_id,
        }
