import random
import string

def input_data():
    choice = input("Выберите способ ввода (1 - вручную, 2 - случайно): ")
    if choice == '1':
        return input("Введите текст: ")
    elif choice == '2':
        length = int(input("Введите длину случайного текста: "))
        return ''.join(random.choices(string.ascii_letters + string.punctuation + ' ', k=length))
    else:
        print("Неверный выбор!")
        return ""

def execute_algorithm(data):
    frequency = {}
    total_chars = len(data)
    
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    for char in frequency:
        frequency[char] /= total_chars
        
    return frequency

def output_result(result):
    for char, freq in result.items():
        print(f"'{char}': {freq:.4f}")

def main():
    data = ""
    result = {}
    
    while True:
        print("Меню:")
        print("1. Ввод данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            data = input_data()
            result = {}  # Сбрасываем результат при новом вводе
        elif choice == '2':
            if data:  # Проверяем, что данные введены
                result = execute_algorithm(data)
            else:
                print("Сначала введите данные!")
        elif choice == '3':
            output_result(result)
        elif choice == '4':
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()