import numpy as np
import string

ALPHABET = string.ascii_uppercase

def get_key_matrix(key_values):
    # Принимаем список из 9 чисел и возвращаем матрицу 3х3
    if len(key_values) != 9:
        raise ValueError("Нужно ввести ровно 9 чисел для матрицы 3x3.")
    return np.array(key_values).reshape(3, 3)

def text_to_numbers(text):
    # Приводим текст к верхнему регистру и переводим буквы в числа (A=0,...,Z=25)
    text = text.upper().replace(" ", "")
    return [ALPHABET.index(ch) for ch in text if ch in ALPHABET]

def numbers_to_text(numbers):
    return ''.join([ALPHABET[num % 26] for num in numbers])

def chunk_text(text, size=3):
    # Разбиваем текст на блоки размера size, дополняем X (или A) при необходимости
    text = text.upper().replace(" ", "")
    chunks = []
    for i in range(0, len(text), size):
        chunk = text[i:i+size]
        if len(chunk) < size:
            chunk += "X" * (size - len(chunk))
        chunks.append(chunk)
    return chunks

def mod_inverse(a, m):
    # Находим обратное число по модулю m (для чисел, взаимно простых с m)
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Обратного элемента не существует.")

def matrix_mod_inv(matrix, modulus):
    # Находим обратную матрицу по модулю modulus для 3x3 матрицы
    det = int(round(np.linalg.det(matrix))) % modulus
    det_inv = mod_inverse(det, modulus)
    # Вычисляем матрицу миноров и транспонируем (кофакторы)
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    ) % modulus
    return matrix_mod_inv

def encrypt_hill(plaintext, key_matrix):
    chunks = chunk_text(plaintext, 3)
    ciphertext = ""
    for chunk in chunks:
        vec = np.array(text_to_numbers(chunk))
        # Шифрование: умножение на матрицу по модулю 26
        res = key_matrix.dot(vec) % 26
        ciphertext += numbers_to_text(res)
    return ciphertext

def decrypt_hill(ciphertext, key_matrix):
    chunks = chunk_text(ciphertext, 3)
    plaintext = ""
    inv_matrix = matrix_mod_inv(key_matrix, 26)
    for chunk in chunks:
        vec = np.array(text_to_numbers(chunk))
        res = inv_matrix.dot(vec) % 26
        plaintext += numbers_to_text(res)
    return plaintext
