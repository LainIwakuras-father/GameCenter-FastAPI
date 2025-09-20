import random
import string

async def generate_random_password(length=8):
    """Генерация случайного пароля заданной длины"""
    # Все возможные символы для пароля
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Генерация пароля
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password