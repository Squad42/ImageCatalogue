import json
from flask import request, render_template
from imageCatalogue.server import app
from imageCatalogue.models import ImageUris
from imageCatalogue.manage_db import get_all, add_instance, delete_instance, edit_instance


@app.route("/", methods=["GET"])
def index():
    api_list = [
        "LIST of all image-uri entries in db >> <br/> /images/list ",
        "ADD new entry to uri database (POST - json object) >> <br/> /images/add ",
        "EDIT existing uri of enrty with id=image_uri_id ( PATCH - json new_uri ) >> <br/> /images/edit/:image_uri_id",
        "REMOVE uri entry with id=image_uri_id from database ( DELETE - json uri ) >> <br/> /images/remove/:image_uri_id",
    ]
    return render_template("index.html", api_list=api_list)


@app.route("/images/list", methods=["GET"])
def fetch():
    image_uris = get_all(ImageUris)
    all_image_uris = []
    for image_uri in image_uris:
        new_image_uri = {
            "id": image_uri.id,
            "user_id": image_uri.user_id,
            "img_uri": image_uri.img_uri,
            "service": image_uri.service,
        }

        all_image_uris.append(new_image_uri)
    return json.dumps(all_image_uris), 200


@app.route("/images/add", methods=["POST"])
def add():
    data = request.get_json()
    user_id = data["user_id"]
    img_uri = data["img_uri"]
    service = data["service"]

    add_instance(ImageUris, user_id=user_id, img_uri=img_uri, service=service)
    return json.dumps("Added"), 200


@app.route("/images/remove/<image_uri_id>", methods=["DELETE"])
def remove(image_uri_id):
    delete_instance(ImageUris, id=image_uri_id)
    return json.dumps("Deleted"), 200


@app.route("/images/edit/<image_uri_id>", methods=["PATCH"])
def edit(image_uri_id):
    data = request.get_json()
    new_img_uri = data["img_uri"]
    edit_instance(ImageUris, id=image_uri_id, img_uri=new_img_uri)
    return json.dumps("Edited"), 200
