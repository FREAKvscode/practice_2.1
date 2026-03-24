import json
import os

library_json = 'library.json'

def load_library():
    if os.path.exists(library_json):
        with open(library_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []

def save_library(library):
    with open(library_json, 'w', encoding='utf-8') as f:
        json.dump(library, f, ensure_ascii=False, indent=4)

def show_all_books(library):
    if not library:
        print("Библиотека пуста")
    else:
        for book in library:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Доступна: {book['available']}")

def search_books(library, keyword, search_by='title'):
    result = [book for book in library if keyword.lower() in book[search_by].lower()]
    return result

def add_book(library):
    new_id = max([book['id'] for book in library], default=0) + 1
    title = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = input("Введите год издания: ")
    new_book = {
        'id': new_id,
        'title': title,
        'author': author,
        'year': year,
        'available': True
    }
    library.append(new_book)
    save_library(library)
    print("Книга добавлена")

def change_availability(library, book_id, is_available):
    for book in library:
        if book['id'] == book_id:
            book['available'] = is_available
            save_library(library)
            print(f"Статус книги ID {book_id} изменен")
            return
    print("Книга с таким ID не найдена")

def delete_book(library, book_id):
    for i, book in enumerate(library):
        if book['id'] == book_id:
            del library[i]
            save_library(library)
            print(f"Книга с ID {book_id} удалена")
            return
    print("Книга с таким ID не найдена")

def export_available_books(library):
    available_books = [book for book in library if book['available']]
    with open('available_books.txt', 'w', encoding='utf-8') as f:
        for book in available_books:
            f.write(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}\n")
    print("Доступные книги экспортированы в 'available_books.txt'")

def main():
    library = load_library()

    while True:
        print("\nМеню:")
        print("1. Просмотр всех книг")
        print("2. Поиск по названию")
        print("3. Поиск по автору")
        print("4. Добавить книгу")
        print("5. Взять книгу")
        print("6. Вернуть книгу")
        print("7. Удалить книгу")
        print("8. Экспорт доступных книг")
        print("9. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            show_all_books(library)
        elif choice == '2':
            keyword = input("Введите название для поиска: ")
            results = search_books(library, keyword, 'title')
            for book in results:
                print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Доступна: {book['available']}")
        elif choice == '3':
            keyword = input("Введите автора для поиска: ")
            results = search_books(library, keyword, 'author')
            for book in results:
                print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Доступна: {book['available']}")
        elif choice == '4':
            add_book(library)
        elif choice == '5':
            try:
                book_id = int(input("Введите ID книги, которую берете: "))
                change_availability(library, book_id, False)
            except ValueError:
                print("Некорректный ID")
        elif choice == '6':
            try:
                book_id = int(input("Введите ID книги, которую возвращаете: "))
                change_availability(library, book_id, True)
            except ValueError:
                print("Некорректный ID")
        elif choice == '7':
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                delete_book(library, book_id)
            except ValueError:
                print("Некорректный ID")
        elif choice == '8':
            export_available_books(library)
        elif choice == '9':
            print("Выход")
            break
        else:
            print("Некорректный выбор. Попробуйте снова")

if __name__ == '__main__':
    main()

