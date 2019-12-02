from imageCatalogue.models import ImageUris


def db_load_example_data(app, db):

    image_uploads = [
        ImageUris(
            1,
            "Dropbox",
            "https://www.dropbox.com/s/uwlodj52lmc0oxi/c3c.png?dl=0",
            "2019-11-22T16:14:03Z",
            False,
        ),
        ImageUris(2, "Amazon S3", "https://amazon-link", "2019-11-22T16:15:13Z", False),
    ]

    with app.app_context():
        for img_up in image_uploads:
            db.session.add(img_up)
        db.session.commit()
