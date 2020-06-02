from flask import Blueprint, jsonify
from repositories.blood_banks.blood_bank_repository import BloodBankRepository
from data_process.upload_blood_bank_data import upload_blood_bank_data

blueprint = Blueprint("dashboard_blueprint", __name__, url_prefix="")

@blueprint.route('/home',methods=["GET"])
def home():
    try:
        # blood_banks = BloodBankRepository.find_by_available_blood_stock("ab_positive")
        upload_blood_bank_data()
        # print(blood_banks)
        # blood_bank_data = {}
        # for blood_bank in blood_banks:
        #     blood_bank_data[blood_bank.id] = blood_bank.to_json()
        #     print(blood_bank)
        # print(blood_bank_data)
        # a=[]
        # for row in result:
        #     a.append(row)
        # print(type(result))
        # if len(a)>0:
        return {"done":True}
    except Exception as exe:
        print(exe)
        return {}
