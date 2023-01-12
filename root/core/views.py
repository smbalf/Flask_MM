"""
Core views
"""
from flask import Blueprint, render_template

core = Blueprint("core", __name__)


# LANDING PAGE
@core.route("/")
def index():
    return render_template("core/index.html")