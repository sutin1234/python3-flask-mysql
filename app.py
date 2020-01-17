from flask import Flask, render_template
from flask_cors import CORS
from instance.config import APP_CONFIG
from routes import router_student, router_users  # import all routes

# initialize app
app = Flask(__name__)
app.config.from_object(APP_CONFIG)
CORS(app)

# register router
app.register_blueprint(router_student, url_prefix="/students")
app.register_blueprint(router_users, url_prefix="/users")

# initailze global variable
topic_text = 'สอนเขียนเว็บด้วย Python3 Flask'


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html', topic=topic_text)


# main app
if __name__ == '__main__':
    app.run()


# FLASK_APP=app.py FLASK_DEBUG=1 flask run
