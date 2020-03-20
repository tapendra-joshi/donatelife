from repositories.blood_banks.blood_bank_repository import BloodBankRepository
# data = {
#             'ab_positive':1,
#             'ab_negative':2,
#             'a_positive':3,
#             'a_negative':4,
#             'b_positive':5,
#             'b_negative':6,
#             'o_positive':7,
#             'o_negative':8
#         }
data=None
print(BloodBankRepository.create_blood_bank_stock(data))
# from models import database