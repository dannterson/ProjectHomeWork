def get_mask_card_number(card_number: str) -> str:
    """Проверка длины номера карты, маскировка номера"""

    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты состоит из 16 цифр")

    hidden_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return hidden_card_number


def get_mask_account(account_number: str) -> str:
    """Проверка длины номера счёта, маскировка счёта"""
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    hidden_account_number = f"**{account_number[-4:]}"
    return hidden_account_number
