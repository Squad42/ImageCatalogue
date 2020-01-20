import json
from flask import request, render_template, jsonify, session, g
from imageCatalogue.server import app
from imageCatalogue.models import ImageUris
from imageCatalogue.manage_db import get_all, add_instance, delete_instance, edit_instance
from functools import wraps
import jwt


def jwt_token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):

        if "jwt_token" not in session:
            return jsonify({"message": "Auth token is missing!"}), 403

        token = session["jwt_token"]

        if not token:
            return jsonify({"message": "Unknown token type!"}), 403

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            g.user_info = data
            app.logger.info("Logged in user: %s", g.user_info["username"])
        except:
            return jsonify({"message": "Token is invalid!"}), 403

        return func(*args, **kwargs)

    return decorated


@app.route("/", methods=["GET"])
def index():
    api_list = [
        "LIST of all image-uri entries in db >> <br/> /images/list ",
        "ADD new entry to uri database (POST - json object) >> <br/> /images/add ",
        "EDIT existing uri of enrty with id=image_uri_id ( PATCH - json new_uri ) >> <br/> /images/edit/:image_uri_id",
        "REMOVE uri entry with id=image_uri_id from database ( DELETE - json uri ) >> <br/> /images/remove/:image_uri_id",
    ]
    return render_template("index.html", api_list=api_list)


@app.route("/demo/info", methods=["GET"])
def demo_info_milestone_1():
    json_info = {
        "clani": ["mb2551", "rt0875"],
        "opis_projekta": "Najin projekt implementira portal za hranjenje, urejanje in deljenje fotografij",
        "mikrostoritve": ["http://34.77.38.10:5000/upload", "http://35.190.207.89:5001/images"],
        "github": [
            "https://github.com/Squad42/ImageUpload",
            "https://github.com/Squad42/ImageCatalogue",
        ],
        "travis": [
            "https://travis-ci.org/Squad42/ImageUpload",
            "https://travis-ci.org/Squad42/ImageCatalogue",
        ],
        "dockerhub": [
            "https://hub.docker.com/repository/docker/slosquad42/image_upload",
            "https://hub.docker.com/repository/docker/slosquad42/image_catalogue",
        ],
    }
    return json.dumps(json_info, indent=2), 200


@app.route("/images", methods=["GET"])
def fetch():

    if not app.config["DB_ONLINE"]:
        print("ERROR: Database connection is down!")
        response = jsonify(service_status="Bad gateway: check DB connection!", service_code=502)
        return response, 200

    image_uris = get_all(ImageUris)
    all_image_uris = []
    for image_uri in image_uris:
        new_image_uri = {
            "id": image_uri.id,
            "user_id": image_uri.user_id,
            "img_uri": image_uri.img_uri,
            "service": image_uri.service,
            "created-on": image_uri.created_datetime.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "private": image_uri.private,
        }

        all_image_uris.append(new_image_uri)
    return json.dumps(all_image_uris), 200


@app.route("/images/add", methods=["POST"])
def add():

    if not app.config["DB_ONLINE"]:
        print("ERROR: Database connection is down!")
        response = jsonify(service_status="Bad gateway: check DB connection!", service_code=502)
        return response, 200

    data = request.get_json()
    user_id = data["user_id"]
    img_uri = data["img_uri"]
    service = data["service"]
    created_datetime = data["created_datetime"]
    private = data["private"]

    add_instance(
        ImageUris,
        user_id=user_id,
        img_uri=img_uri,
        service=service,
        created_datetime=created_datetime,
        private=private,
    )
    return json.dumps("Added"), 200


@app.route("/images/remove/<image_uri_id>", methods=["DELETE"])
def remove(image_uri_id):

    if not app.config["DB_ONLINE"]:
        print("ERROR: Database connection is down!")
        response = jsonify(service_status="Bad gateway: check DB connection!", service_code=502)
        return response, 200

    delete_instance(ImageUris, id=image_uri_id)
    return json.dumps("Deleted"), 200


@app.route("/images/edit/<image_uri_id>", methods=["PATCH"])
def edit(image_uri_id):

    if not app.config["DB_ONLINE"]:
        print("ERROR: Database connection is down!")
        response = jsonify(service_status="Bad gateway: check DB connection!", service_code=502)
        return response, 200

    data = request.get_json()
    new_img_uri = data["img_uri"]
    edit_instance(ImageUris, id=image_uri_id, img_uri=new_img_uri)
    return json.dumps("Edited"), 200

@app.route("/health/liveness")
def liveness():
    healthStatus = None
    try:
        if "consul_server" in app.config and app.config["consul_server"] is not None:
            index = None
            index, data = app.config["consul_server"].kv.get("imageCatalogue/alive", index=index)
            if data is not None:
                healthStatus = data["Value"]
            else:
                healthStatus = "true"
        else:
            healthStatus = "true"
    except:
        healthStatus = "false"        

    if "false" in str(healthStatus).lower():
        response = jsonify(
        service_status="FAIL",
        service_code=503)
        return response, 503
    else:
        response = jsonify(
        service_status="PASS",
        service_code=200)
        return response, 200
    
@app.route("/health/readiness")
def readiness():
    healthStatus = None
    try:
        if "consul_server" in app.config and app.config["consul_server"] is not None:
            index = None
            index, data = app.config["consul_server"].kv.get("imageCatalogue/ready", index=index)
            if data is not None:
                healthStatus = data["Value"]
            else:
                healthStatus = "true"
        else:
            healthStatus = "true"
    except:
        healthStatus = "false"         

    if "false" in str(healthStatus).lower():
        response = jsonify(
        service_status="FAIL",
        service_code=503)
        return response, 503
    else:
        response = jsonify(
        service_status="PASS",
        service_code=200)
        return response, 200    