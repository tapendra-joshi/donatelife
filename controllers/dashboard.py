from flask import Blueprint, jsonify

blueprint = Blueprint("dashboard_blueprint", __name__, url_prefix="/dashboard")

@blueprint.route('/home',methods=["GET"])
def home():
    try:
        return "Hello World!!!!!"
    except:
        return True
