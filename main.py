def input_data():
    pass  # Заглушка для ввода данных

def execute_algorithm(data):
    pass  # Заглушка для выполнения алгоритма

def output_result(result):
    pass  # Заглушка для вывода результата

def main():
    while True:
        print("Меню:")
        print("1. Ввод данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            input_data()
        elif choice == '2':
            data = None  # Здесь будет храниться введённые данные
            result = execute_algorithm(data)
        elif choice == '3':
            output_result(result)
        elif choice == '4':
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main() 
