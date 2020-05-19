from repositories.users.user_repository import UserRepository
import uuid


class UserService:

    @staticmethod
    def create_user(user_data):
        
        existing_user = UserService.find_by_email(user_data.get('email'))
        if existing_user:
            return None

        user_data["verification_code"] = str(uuid.uuid4())
        user = UserRepository.create_user(user_data)
        if user:
            return user.to_json()

        return None


    @staticmethod
    def find_by_email(email=None,formatted=False):

        if not email:
            return None

        user = UserRepository.find_by_email(email)
        
        if not user:
            return None
        
        if formatted:
            return user.to_json()

        return user


    @staticmethod
    def update_user(user, user_data=None):
        """
        Updates a user
        :param user: User object
        :param user_data: dict of fields to be updated
        :return: upated user object if the update is successful; else None
        """
        return UserRepository.update_user(user, user_data)
    