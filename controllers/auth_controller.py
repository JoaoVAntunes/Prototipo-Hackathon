from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, logout_user, login_required, current_user


auth = Blueprint('auth', __name__, template_folder="views")


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
