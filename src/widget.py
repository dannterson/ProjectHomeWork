from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(user_data: str) -> str:
    user_data_list = user_data.split()
    if "Maestro" in user_data or "MasterCard" in user_data:
        return f"{user_data_list[0]} {get_mask_card_number(user_data[1])}"
    elif "Visa" in user_data:
        visa_name_list = []
        visa_number_list = []
        for i in user_data_list:
            if i.isalpha():
                visa_name_list.append(i)
            elif i.isdigit():
                visa_number_list.append(i)
        visa_data = "".join(visa_number_list)
        return f"{visa_name_list[0]} {visa_name_list[1]} {get_mask_card_number(visa_data)}"
    elif "Счёт" or "Счет" in user_data:
        return f"Счёт {get_mask_account(user_data_list[1])}"
    else:
        return "Неверный формат"


def get_date(date: str) -> str:
    pass

