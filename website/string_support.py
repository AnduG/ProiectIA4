import hashlib

def has_numbers(to_check):
    for char in to_check:
        if char.isdigit():
            return True
    return False

def has_letters(to_check):
    for char in to_check:
        if char.isalpha():
            return True
    return False

def has_special_characters(to_check):
    for char in to_check:
        if not char.isalnum():
            return True
    return False

def has_uppercase(to_check):
    for char in to_check:
        if char.isupper():
            return True
    return False

def has_lowercase(to_check):
    for char in to_check:
        if char.islower():
            return True
    return False

def hash_string(input_string):
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    hashed_string = sha256.hexdigest()
    return hashed_string