import datetime
from sqlalchemy_utils import ChoiceType
from models.database import IndexedTimestampModel,db,Column
from constants.user_constants import UserSex,BloodGroup,IndianStates,UserStatus,UserVerificationStatus,BloodRequirementStatus
from constants.hashing_constants import HashMethod
from helpers.hash_helper import get_hash_string
from flask_login import UserMixin
import json
from extentions.extentions import login_manager


class UserModel(UserMixin,IndexedTimestampModel):
    __tablename__ = "life_users"

    id = Column(db.BigInteger, primary_key=True, autoincrement=True, nullable=False)
    email = db.Column(db.String(255),unique=True, nullable=False)
    password_hash = db.Column(db.String(65),nullable=False)
    reset_password_code = db.Column(db.String(255), nullable=True, default=None, index=True)
    reset_password_expiry = db.Column(db.DateTime, nullable=True,default=(datetime.datetime.utcnow() + datetime.timedelta(hours=2)))
    blood_group = db.Column(ChoiceType(BloodGroup),nullable=False)
    first_name = db.Column(db.String(255),nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    phone_number = db.Column(db.String(15),nullable=True)
    sex = db.Column(ChoiceType(UserSex),nullable=False,default=UserSex.UNSPECIFIED)
    birth_date = db.Column(db.DateTime,nullable=False)
    profile_picture_data = db.Column(db.JSON,name = "profile_picture_data",default={})
    state = db.Column(ChoiceType(IndianStates), nullable=False,index=True)
    country = db.Column(db.String(65),nullable=False,default="India",index=True)
    verification_status = db.Column(ChoiceType(UserVerificationStatus), nullable=False, default=UserVerificationStatus.UNVERIFIED)
    verification_code = db.Column(db.String(255), nullable=True, default=None, index=True)
    status = db.Column(ChoiceType(UserStatus),nullable=False, default= UserStatus.ACTIVE)
    blood_requirement_status = db.Column(ChoiceType(BloodRequirementStatus),nullable=False,default=BloodRequirementStatus.NOT_REQUIRED)
    required_blood_group = db.Column(ChoiceType(BloodGroup),nullable=True,default=None)

    # def __init__(self,email,password,first_name,last_name,blood_group,status,verification_status,state,blood_requirement_status,required_blood_group):
    #     self.email = email
    #     self.password_hash = get_hash_string(password,HashMethod.SHA256)
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.blood_group = blood_group
    #     self.status = status
    #     self.verification_status = verification_status
    #     self.state = state
    #     self.blood_requirement_status = blood_requirement_status
    #     self.required_blood_group = required_blood_group

    def to_json(self):

        status_value = None
        if self.status:
            status_value = self.status.value
        
        verification_status_value = None
        if self.verification_status:
            verification_status_value = self.verification_status.value
        
        blood_group_value = None
        if self.blood_group:
            blood_group_value = self.blood_group.value
        
        sex_value = None
        if self.sex:
            sex_value = self.sex.value
        
        profile_picture_data_value = None
        if self.profile_picture_data:
            profile_picture_data_value = json.loads(self.profile_picture_data)

        required_blood_group_value = None
        if self.required_blood_group:
            required_blood_group_value=self.required_blood_group.value

        blood_requirement_status_value = None
        if self.blood_requirement_status:
            blood_requirement_status_value = self.blood_requirement_status.value

        return{
            "id":self.id,
            "first_name":self.first_name,
            "last_time":self.last_name,
            "blood_group":blood_group_value,
            "sex":sex_value,
            "profile_picture_data":profile_picture_data_value,
            "status":status_value,
            "verification_status":verification_status_value,
            "email":self.email,
            "blood_requirement_status":blood_requirement_status_value,
            "required_blood_group":required_blood_group_value,

            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "last_updated_at": self.last_updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }



@login_manager.user_loader
def load_user(id):
    return UserModel.query.get(int(id))