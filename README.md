# Image Catalogue Microservice

Image Catalogue Microservice is a part of Image sharing and analysis portal app.
Service is responsible for CRUD operations upon Image catalogue.
Image catalogue is keeping information about:

* image ownership
* image location
* image upload date

# Installation

## Python packages

```
pip install -r requirements.txt
```

psycopg2 package might cause some dependency issues - possible solution here:
https://stackoverflow.com/a/28938258

## Local database setup (POSTGRESQL)

Install postgres packages
```
sudo apt-get update
sudo apt install postgresql postgresql-contrib
```

Set password for default postgres user
```
sudo -u postgres psql
ALTER USER postgres WITH PASSWORD 'newPassword';
```

Create new test_user with 'password' (skip first line if already in psql)
```
sudo -u postgres psql
CREATE USER test_user WITH PASSWORD 'password1';
```


You can check if user was created successully (skip first line if already in psql)
```
sudo -u postgres psql
\du
```

Create test database for test_user (skip first line if already in psql)
```
sudo -u postgres psql
ALTER USER test_user WITH SUPERUSER;
CREATE DATABASE db_catalogue_example OWNER test_user;
GRANT ALL PRIVILEGES ON DATABASE db_catalogue_example TO test_user;
```


