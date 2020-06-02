from services.blood_bank_service import BloodBankService
from flask import Blueprint, jsonify,request
from constants.api_response_constants import BaseResponse,ResponseCode

blueprint = Blueprint("blood_bank_blueprint",__name__,url_prefix="/blood_banks")


@blueprint.route("/all",methods=["GET"])
def get_all_blood_banks():

    all_blood_bank_data = BloodBankService.get_all_blood_banks(True)
    if all_blood_bank_data:
        return jsonify(BaseResponse(1,ResponseCode.SUCCESS,None,all_blood_bank_data).to_json()),200
    return jsonify(BaseResponse(0,ResponseCode.RESOURCE_NOT_FOUND,"no blood banks data found",None).to_json()),201


@blueprint.route("/create",methods=["POST"])
def post_blood_bank():
    post_json = request.get_json()
    blood_bank = BloodBankService.create_blood_bank(post_json,formatted=True)
    if blood_bank:
        return jsonify(BaseResponse(1,ResponseCode.SUCCESS,None,blood_bank).to_json()),201
    return jsonify(BaseResponse(0,ResponseCode.INVALID_REQUEST_DATA,"correct data not sent by user",None).to_json()),400


@blueprint.route("/<blood_type>",methods=["GET"])
def get_filtered_blood_banks(blood_type):
    if blood_type:
        blood_banks = BloodBankRepository.find_by_available_blood_stock(blood_type,formatted=True)
        if blood_banks:
            return jsonify(BaseResponse(1,ResponseCode.SUCCESS,None,blood_banks).to_json()),200
        return jsonify(BaseResponse(0,ResponseCode.RESOURCE_NOT_FOUND,"no blood banks found",None).to_json()),201
