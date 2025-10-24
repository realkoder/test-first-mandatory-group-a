from app.services.cpr_service import generate_cpr_name_gender_dob
from app.services.address_service import get_random_address
from app.services.phone_service import generate_phone_number

async def generate_person():
    person_data = await generate_cpr_name_gender_dob()
    address = await get_random_address()
    phone_number = await generate_phone_number()

    return {
        "cpr": person_data["cpr"],
        "first_name": person_data["first_name"],
        "last_name": person_data["last_name"],
        "gender": person_data["gender"],
        "dob": person_data["dob"],
        "address": address,
        "phone_number": phone_number
    }
