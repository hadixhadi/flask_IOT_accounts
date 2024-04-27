from flask import Blueprint
from db_config import create_connection_pool
blueprint=Blueprint("accounts","__name__")

@blueprint.route('/accounts')
def index():
    return "accounts page"