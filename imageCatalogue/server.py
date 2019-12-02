from flask import Flask
from imageCatalogue.models import db
from imageCatalogue.example_data import db_load_example_data

app = Flask(__name__)
app.config.from_object("imageCatalogue.server_config.DevelopmentConfig")

if app.config["DB_INITIALIZE"] == "True":

    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["DATABASE_CONNECTION_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app_context().push()

    # ORDERING OF NEXT LINES IS IMPORTANT !!!
    db.init_app(app)
    from imageCatalogue.models import ImageUris

    db.create_all()
    db_load_example_data(app, db)

    app.config["DB_ONLINE"] = True

from imageCatalogue.server_views import *

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5001)
