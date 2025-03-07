import random

def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list:

    if min_val < 1 or max_val > 1000 or quantity < 1 or quantity > (max_val - min_val + 1):
        return []
    
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    return sorted(numbers)

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
