import random
import string

def generate_password(length, use_numbers, use_symbols):
    if length <= 0:
        raise ValueError("Length must be greater than 0")

    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password