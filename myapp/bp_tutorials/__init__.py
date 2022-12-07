from flask import Blueprint

bp_tutorials = Blueprint('bp_tutorials', __name__, cli_group="db")

from . import views_tutorials

