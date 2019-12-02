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
        ImageUris(
            2,
            "Amazon S3",
            "https://rso-imageportal.s3.eu-central-1.amazonaws.com/Screenshot_from_2019-11-11_02-10-07.png",
            "2019-11-22T16:15:13Z",
            False,
        ),
        ImageUris(
            3,
            "Dropbox",
            "https://www.dropbox.com/s/9fccuidhjbbqdaq/173533.jpg?dl=0",
            "2019-11-22T16:14:03Z",
            False,
        ),
        ImageUris(
            4,
            "Dropbox",
            "https://www.dropbox.com/s/fs2tdth9187a6tr/deer-artwork.jpg?dl=0",
            "2019-11-22T16:14:03Z",
            False,
        ),
        ImageUris(
            5,
            "Amazon S3",
            "https://rso-imageportal.s3.eu-central-1.amazonaws.com/adrianfelipepera_traslasierra.jpg",
            "2019-11-22T16:15:13Z",
            False,
        ),
        ImageUris(
            6,
            "Dropbox",
            "https://www.dropbox.com/s/x0m8xm91wuvps0z/gdmlock.jpg?dl=0",
            "2019-11-22T16:14:03Z",
            False,
        ),
        ImageUris(
            7,
            "Dropbox",
            "https://www.dropbox.com/s/fqpguogsr8mdct2/roa050118fea-corvette-08-1522693637.jpg?dl=0",
            "2019-11-22T16:14:03Z",
            False,
        ),
        ImageUris(
            8,
            "Amazon S3",
            "https://rso-imageportal.s3.eu-central-1.amazonaws.com/wireframed-deer.jpg",
            "2019-11-22T16:15:13Z",
            False,
        ),
        ImageUris(
            9,
            "Dropbox",
            "https://www.dropbox.com/s/u90wot3rttdcbbo/wp1828915-programmer-wallpapers.png?dl=0",
            "2019-11-22T16:14:03Z",
            False,
        ),
        ImageUris(
            10,
            "Amazon S3",
            "https://rso-imageportal.s3.eu-central-1.amazonaws.com/test.jpg",
            "2019-11-22T16:15:13Z",
            False,
        ),
    ]

    with app.app_context():
        for img_up in image_uploads:
            db.session.add(img_up)
        db.session.commit()
