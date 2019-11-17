from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ImageUris(db.Model):
    __tablename__ = "imageuris"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    service = db.Column(db.String(20))
    img_uri = db.Column(db.String(100))
