import os
import datetime

calculator_log = 'calculator.log'

def show_last_operations():
    if os.path.exists(calculator_log):
        with open(calculator_log, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            last_lines = lines[-5:]
            print("Последние 5 операций:")
            for line in last_lines:
                print(line.strip())
    else:
        print("Лог-файл пуст или не существует")

def log_operation(expression, result):
    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    log_line = f"[{now}] {expression} = {result}\n"
    with open(calculator_log, 'a', encoding='utf-8') as f:
        f.write(log_line)

def clear_log():
    if os.path.exists(calculator_log):
        os.remove(calculator_log)
        print("Лог-файл очищен")
    else:
        print("Лог-файл не существует")

def main():
    show_last_operations()

    while True:
        print("\nВыберите действие:")
        print("1. Выполнить расчет")
        print("2. Очистить лог-файл")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                operation = input("Введите операцию (+, -, *, /): ")

                if operation not in ['+', '-', '*', '/']:
                    print("Некорректная операция")
                    continue

                if operation == '+':
                    result = a + b
                elif operation == '-':
                    result = a - b
                elif operation == '*':
                    result = a * b
                elif operation == '/':
                    if b == 0:
                        print("Ошибка: деление на ноль")
                        continue
                    result = a / b

                expression = f"{a} {operation} {b}"
                print(f"Результат: {result}")
                log_operation(expression, result)

            except ValueError:
                print("Некорректный ввод чисел")
        elif choice == '2':
            clear_log()
        elif choice == '3':
            print("Выход из программы")
            break
        else:
            print("Некорректный выбор")

if __name__ == "__main__":
    main()


