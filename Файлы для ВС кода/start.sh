export FLASK_DEBUG=1

docker-compose up -d

# To load env variables
export $(xargs <database.conf)
export FLASK_APP=app.py

cd app && flask run