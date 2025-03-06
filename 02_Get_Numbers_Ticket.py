import random

def get_numbers_ticket(min_val, max_val, quantity):

    if not (1 <= min_val <= max_val <= 1000) or not (min_val <= quantity <= max_val):
        return []
    
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    return sorted(numbers)

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 64, 10)
print("Ваші лотерейні числа:", lottery_numbers)
