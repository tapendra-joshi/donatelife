import pandas as pd
from models.blood_banks.blood_bank_model import BloodBankModel


def upload_blood_bank_data():
    df = pd.read_csv('blood-banks.csv',encoding='ISO-8859-1')
    for index,row in df.iterrows():
        blood_bank = BloodBankModel(
            name = row[' Blood Bank Name'],
            email=row[' Email'],
            state=row[' State'],
            district = row[' District'],
            city = row[' City'],
            blood_stock_id = 1,
            address = row[' Address'],
            contact_number = row[' Contact No'],
            mobile_number = row[' Mobile'],
            latitude = row[' Latitude'],
            longitude = row[' Longitude']
        )
        blood_bank.save()
    