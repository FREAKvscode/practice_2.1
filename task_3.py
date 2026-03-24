import csv

products_file = 'products.csv'

def read_products():
    products = []
    try:
        with open(products_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                product = {
                    'Название': row['Название'].strip(),
                    'Цена': float(row['Цена'].strip()),
                    'Количество': int(row['Количество'].strip())
                }
                products.append(product)

    except FileNotFoundError:
        print(f"Файл {products_file} не найден")
    return products

def add_product(products):
    try:
        name = input("Введите название товара: ")
        price = float(input("Введите цену: "))
        quantity = int(input("Введите количество: "))
        products.append({'Название': name, 'Цена': price, 'Количество': quantity})

    except ValueError:
        print("Некорректный ввод цены или количества")

def search_product(products):
    search_name = input("Введите название товара для поиска: ")
    found = False
    for product in products:
        if product['Название'].lower() == search_name.lower():
            print(f"Найден товар: {product['Название']}")
            print(f"Цена: {product['Цена']}")
            print(f"Количество: {product['Количество']}")
            found = True
            break
    if not found:
        print("Товар не найден")

def calculate_total_value(products):
    total = 0
    for product in products:
        total += product['Цена'] * product['Количество']
    print(f"Общая стоимость всех товаров: {total}")

def save_products(products):
    with open(products_file, 'w', newline='') as csv_file:
        fieldnames = ['Название', 'Цена', 'Количество']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        csv_writer.writeheader()
        for product in products:
            row = {
                'Название': product['Название'],
                'Цена': str(product['Цена']),
                'Количество': str(product['Количество'])
            }
            csv_writer.writerow(row)

def main():
    products = read_products()

    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть все товары")
        print("2. Добавить товар")
        print("3. Поиск товара по названию")
        print("4. Рассчитать общую стоимость")
        print("5. Выйти и сохранить изменения")
        choice = input("Введите номер действия: ")

        if choice == '1':
            if not products:
                print("Список товаров пуст")
            else:
                for product in products:
                    print(f"- {product['Название']}: Цена {product['Цена']}, Количество {product['Количество']}")
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            search_product(products)
        elif choice == '4':
            calculate_total_value(products)
        elif choice == '5':
            save_products(products)
            print("Данные сохранены")
            break
        else:
            print("Некорректный выбор, попробуйте снова")

if __name__ == '__main__':
    main()

