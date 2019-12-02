from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class ImageUris(db.Model):
    __tablename__ = "imageuris"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    service = db.Column(db.String(20))
    img_uri = db.Column(db.String(100))
    created_datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    private = db.Column(db.Boolean)

    def __init__(self, user_id, service, img_uri, created_datetime, private):
        self.user_id = user_id
        self.service = service
        self.img_uri = img_uri
        self.created_datetime = datetime.datetime.strptime(created_datetime, "%Y-%m-%dT%H:%M:%SZ")
        self.private = private
