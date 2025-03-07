from datetime import datetime

def get_days_from_today(date_string: str) -> int:
    try:
        date_conv = datetime.strptime(date_string, "%Y-%m-%d").date() # Перетворення рядка у об'єкт datetime
        today = datetime.today().date() # Отримання поточної дати без часу
        day_delta = today - date_conv # Обчислення різниці у днях
        return day_delta.days
    except ValueError:
        return f"Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."


print(get_days_from_today("2024-09-20"))