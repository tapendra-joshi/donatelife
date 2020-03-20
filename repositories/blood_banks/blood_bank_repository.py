from models.blood_banks.blood_bank_model import BloodBankModel,BloodStock

class BloodBankRepository:

    @staticmethod
    def create_blood_bank_stock(blood_stock_data=None):
        if blood_stock_data:
            blood_stock = BloodStock(
                ab_positive = blood_stock_data.get('ab_positive',0),
                ab_negative = blood_stock_data.get('ab_negative',0),
                a_positive = blood_stock_data.get('a_positive',0),
                a_negative = blood_stock_data.get('a_negative',0),
                b_positive = blood_stock_data.get('b_positive',0),
                b_negative = blood_stock_data.get('b_negative',0),
                o_positive = blood_stock_data.get('o_negative',0),
                o_negative = blood_stock_data.get('o_negative',0)
            )
            blood_stock.save()
            return blood_stock
        return None

    @staticmethod
    def update_blood_stock(blood_stock_object,blood_stock_data=None):
        if blood_stock_data:
            blood_stock_object_attrs = list(blood_stock_object.__dict__.keys())
            for blood_stock_data_key,blood_stock_data_value in blood_stock_data.items():
                if blood_stock_data_key in blood_stock_object_attrs:
                    setattr(blood_stock_object,blood_stock_data_key,blood_stock_data_value)
            blood_stock_object.save()
            return blood_stock_object
        return None

    @staticmethod
    def create_blood_bank(blood_bank_data=None):
        if blood_bank_data:
            blood_bank = BloodBankModel(
                name = blood_bank_data.get('name'),
                email = blood_bank_data.get('email'),
                address = blood_bank_data.get('address'),
                state = blood_bank_data.get('state'),
                country = blood_bank_data.get('country'),
                blood_stock_id = BloodBankRepository.create_blood_bank_stock(blood_bank_data.get('blood_stock')).id
            )
            
            blood_bank.save()
            return blood_bank
        return None

    @staticmethod
    def get_all_blood_banks(formatted=False):
        
        all_blood_banks = BloodBankModel.query.all()
        if all_blood_banks:
            if not formatted:
                return all_blood_banks
            all_blood_bank_data = {}
            for blood_bank in all_blood_banks:
                all_blood_bank_data[blood_bank.id] = blood_bank.to_json()
            return all_blood_bank_data
        return None


