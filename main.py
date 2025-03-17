# main.py
from playfair import encrypt_playfair, decrypt_playfair
from hill import encrypt_hill, decrypt_hill, get_key_matrix
from vigenere import encrypt_vigenere, decrypt_vigenere

def main():
    print("Выберите шифр:")
    print("1. Шифр Плейфейера")
    print("2. Шифр Хилла")
    print("3. Шифр Виженера")
    choice = input("Ваш выбор (1/2/3): ")

    if choice == "1":
        mode = input("Введите 'e' для шифрования или 'd' для расшифрования: ").lower()
        key = input("Введите ключ (английское слово не менее 7 букв): ")
        text = input("Введите текст (фамилия, имя, отчество на английском): ")
        if mode == 'e':
            result = encrypt_playfair(text, key)
        else:
            result = decrypt_playfair(text, key)
        print("Результат:", result)

    elif choice == "2":
        mode = input("Введите 'e' для шифрования или 'd' для расшифрования: ").lower()
        text = input("Введите текст (фамилия, имя, отчество на английском): ")
        # Для простоты предлагаем ввести элементы ключевой матрицы через запятую
        key_input = input("Введите 9 чисел через пробел (ключевая матрица 3х3, детерминант не равен 0): ")
        key_values = list(map(int, key_input.split()))
        key_matrix = get_key_matrix(key_values)
        if mode == 'e':
            result = encrypt_hill(text, key_matrix)
        else:
            result = decrypt_hill(text, key_matrix)
        print("Результат:", result)

    elif choice == "3":
        mode = input("Введите 'e' для шифрования или 'd' для расшифрования: ").lower()
        key = input("Введите ключ (ваше полное имя): ")
        text = input("Введите текст (фамилия, имя, отчество): ")
        if mode == 'e':
            result = encrypt_vigenere(text, key)
        else:
            result = decrypt_vigenere(text, key)
        print("Результат:", result)

    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()
