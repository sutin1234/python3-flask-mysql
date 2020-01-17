from flask import Flask
from instance.config import APP_CONFIG  # load configuration file
import pymysql.cursors

app = Flask(__name__)
app.config.from_object(APP_CONFIG)

conn = pymysql.connect(
    host=app.config["DB_HOST"],
    user=app.config["DB_USER"],
    password=app.config["DB_PASSWORD"],
    db=app.config["DB_NAME"],
    charset=app.config['CHARSET'])
