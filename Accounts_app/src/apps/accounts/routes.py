from flask import Blueprint, session, jsonify, Response
from db_config import create_connection_pool
from .models import *
blueprint = Blueprint("accounts", "__name__")
from flask import request
import random
import redis
from apps import app
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import create_access_token ,jwt_required , get_jwt_identity , JWTManager


limiter = Limiter(app=app, key_func=get_remote_address)
jwt=JWTManager(app=app)



base_url = "/api/v1/accounts/"
def connect_redis():
    return redis.Redis(host='redis', port='6379', decode_responses=True)


@blueprint.route(f'{base_url}send-otp', methods=['POST'])
@limiter.limit("2/minute")
def send_otp():
    data = request.form
    phone_number = data.get("phone_number")
    if len(phone_number) == 11:
        otp_code = random.randint(1000, 9999)
        r = connect_redis()
        r.set(phone_number, otp_code, ex=120)
        r.close()
        session['phone_number'] = phone_number
        response = jsonify({"message": "code sent to your phone number.",
                            "redirect_route": f"{base_url}confirm-otp"})
        response.status_code = 200
        return response
    else:
        return Response("phone number is not valid!", status=403)


@app.route(f"{base_url}confirm-otp", methods=['POST'])
@limiter.limit("4/minute")
def confirm_otp_code():
    user_otp = request.form.get("otp")
    user_phone_number = session['phone_number']
    r = connect_redis()
    redis_record = r.get(user_phone_number)
    r.close()
    if redis_record is not None and user_otp == redis_record:
        # check if user registered already create a JWT token
        result=is_user_exists(user_phone_number)
        if len(result)==0: # user does not exist
            return jsonify({"is_user_exists":False,"redirect_route":f"{base_url}/register"}),200
        else:
            # create a JWT token for user
            access_token=create_access_token(identity=user_phone_number)
            return jsonify(access_token=access_token),201
    return Response("otp code is wrong",status=403)
