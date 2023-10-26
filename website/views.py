from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required #Đảm bảo ko vào trang chủ khi chưa login
def home():
    # return "<h1>Test</h1>"
    return render_template("home.html", user=current_user)