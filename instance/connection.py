from flask import Flask
from instance.config import APP_CONFIG  # load configuration file
import pymysql.cursors

app = Flask(__name__)
app.config.from_object(APP_CONFIG)
conn = ''

try:
    conn = pymysql.connect(
        host=app.config["DB_HOST"],
        user=app.config["DB_USER"],
        password=app.config["DB_PASSWORD"],
        db=app.config["DB_NAME"],
        charset=app.config['CHARSET'])
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
