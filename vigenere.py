import string

ALPHABET = string.ascii_uppercase

def format_text(text):
    # Приводим к верхнему регистру и убираем лишние пробелы
    return text.upper().replace(" ", "")

def extend_key(text, key):
    key = format_text(key)
    if len(key) == 0:
        raise ValueError("Ключ не должен быть пустым!")
    # Повторяем ключ до длины текста
    return (key * ((len(text) // len(key)) + 1))[:len(text)]

def encrypt_vigenere(plaintext, key):
    plaintext = format_text(plaintext)
    extended_key = extend_key(plaintext, key)
    ciphertext = ""
    for p, k in zip(plaintext, extended_key):
        shift = (ALPHABET.index(p) + ALPHABET.index(k)) % 26
        ciphertext += ALPHABET[shift]
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    ciphertext = format_text(ciphertext)
    extended_key = extend_key(ciphertext, key)
    plaintext = ""
    for c, k in zip(ciphertext, extended_key):
        shift = (ALPHABET.index(c) - ALPHABET.index(k)) % 26
        plaintext += ALPHABET[shift]
    return plaintext
