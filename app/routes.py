from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from . import db
from .models import User, Radio

bp = Blueprint('main', __name__)

@bp.route('/')
@login_required
def index():
    radios = Radio.query.all()
    return render_template('index.html', radios=radios)

# Additional routes for authentication and radio management
