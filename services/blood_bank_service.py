from repositories.blood_banks.blood_bank_repository import BloodBankRepository


class BloodBankService:

    @staticmethod
    def get_all_blood_banks(formatted=False):
        all_blood_bank_data = BloodBankRepository.get_all_blood_banks(formatted)
        if all_blood_bank_data:
            return all_blood_bank_data
        return None

    @staticmethod
    def create_blood_bank(blood_bank_data,formatted=False):
        if blood_bank_data:
            
            existing_blood_bank = BloodBankRepository.find_by_email(blood_bank_data.get("email"))
            if existing_blood_bank:
                return None

            blood_bank = BloodBankRepository.create_blood_bank(blood_bank_data)
            if blood_bank:
                if formatted:
                    blood_bank_json = blood_bank.to_json()
                    return blood_bank_json
                return blood_bank
        return None
                
