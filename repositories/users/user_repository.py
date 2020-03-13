from models.users.user_model import UserModel
from constants.user_constants import UserSex,BloodGroup,UserStatus,UserVerificationStatus

class UserRepository:

    @staticmethod
    def create_user(user_data=None):
        if user_data:
            user = UserModel(
                email = user_data.get('email'),
                password = user_data.get('password'),
                first_name = user_data.get('first_name'),
                last_name = user_data.get('last_name'),
                sex = user_data.get('sex'),
                blood_group = user_data.get('blood_group')
                state = user_data.get('state'),
                country = user_data.get('country'),
                birth_date = user_data.get('birth_date')
            )
            user.verification_code = user_data.get('verification_code',None)
            user.save()
            return user
        return None


