from flask import Blueprint, render_template
router_users = Blueprint('user_template', __name__)

topic_text = 'สอนเขียนเว็บด้วย Python3 Flask | User'


@router_users.route('/')
def get_user():
    return render_template('users/show.html', topic=topic_text)
