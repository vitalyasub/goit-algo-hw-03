import re

def normalize_phone(phone_number: str) -> str:
    # Видаляємо всі символи, крім цифр та знаку '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number) 
    
    # Якщо номер вже починається з '+380' або '+', залишаємо його без змін
    if cleaned_number.startswith('+380') or cleaned_number.startswith('+'):
        return cleaned_number
    
    # Якщо номер починається з '380', але без '+', додаємо його
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number
   
    # В іншому випадку додаємо стандартний код '+38'
    return '+38' + cleaned_number

# Тестові номери
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4568",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Нормалізація
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)