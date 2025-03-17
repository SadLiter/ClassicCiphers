import string

def generate_matrix(key):
    # Приводим ключ к верхнему регистру и убираем пробелы
    key = key.upper().replace(" ", "")
    matrix = ""
    # Убираем повторяющиеся символы
    for ch in key:
        # Считаем I и J одинаковыми
        if ch == "J":
            ch = "I"
        if ch not in matrix and ch in string.ascii_uppercase:
            matrix += ch
    # Заполняем оставшимися буквами (объединяя I и J)
    for ch in string.ascii_uppercase:
        if ch == "J":  # пропускаем J
            continue
        if ch not in matrix:
            matrix += ch
    # Разбиваем на строки по 5 символов
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]

def process_text(text):
    # Убираем пробелы и приводим к верхнему регистру, заменяем J на I
    text = text.upper().replace(" ", "").replace("J", "I")
    processed = ""
    i = 0
    while i < len(text):
        processed += text[i]
        if i+1 < len(text):
            if text[i] == text[i+1]:
                processed += "X"
                i += 1
            else:
                processed += text[i+1]
                i += 2
        else:
            processed += "X"
            i += 1
    return processed

def find_position(letter, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def encrypt_playfair(plaintext, key):
    matrix = generate_matrix(key)
    text = process_text(plaintext)
    ciphertext = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        if row1 == row2:
            # Замещаем символ следующей буквой в строке (циклический сдвиг)
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            # Замещаем буквой из следующей строки (циклический сдвиг)
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            # Меняем столбцы
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

def decrypt_playfair(ciphertext, key):
    matrix = generate_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        if row1 == row2:
            plaintext += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plaintext += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext
