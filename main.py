"""Консольное приложение для трекинга прочитанных книг."""

from models import Book
from storage import add_book, load_books, delete_book
from stats import get_average_rating, get_author_stats


def main():
    """Главная функция приложения с меню."""
    while True:
        print("\n" + "=" * 40)
        print("  Трекер прочитанных книг")
        print("=" * 40)
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        print("=" * 40)

        choice = input("\nВыберите действие (1-6): ").strip()

        if choice == "1":
            add_book_menu()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            show_average_rating()
        elif choice == "4":
            show_author_stats()
        elif choice == "5":
            delete_book_menu()
        elif choice == "6":
            print("\nДо свидания!")
            break
        else:
            print("\nНеверный выбор. Попробуйте снова.")


def add_book_menu():
    """Меню для добавления книги."""
    print("\n--- Добавление книги ---")
    author = input("Автор: ").strip()
    title = input("Название: ").strip()

    while True:
        try:
            rating = int(input("Оценка (1-5): ").strip())
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть от 1 до 5!")
        except ValueError:
            print("Введите число от 1 до 5!")

    date_read = input("Дата прочтения (YYYY-MM-DD): ").strip()

    book = Book(author=author, title=title, rating=rating, date_read=date_read)
    add_book(book)
    print("\nКнига добавлена!")


def show_all_books():
    """Показать все книги."""
    print("\n--- Все книги ---")
    books = load_books()
    if not books:
        print("Список пуст.")
        return

    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")


def show_average_rating():
    """Показать среднюю оценку."""
    print("\n--- Средняя оценка ---")
    avg = get_average_rating()
    if avg == 0:
        print("Нет данных для расчёта.")
    else:
        print(f"Средняя оценка: {avg:.2f}")


def show_author_stats():
    """Показать статистику по авторам."""
    print("\n--- Статистика по авторам ---")
    stats = get_author_stats()
    if not stats:
        print("Нет данных.")
        return

    for author, data in stats.items():
        print(f"{author}: {data['count']} книг, средняя оценка: {data['avg_rating']:.2f}")


def delete_book_menu():
    """Меню для удаления книги."""
    print("\n--- Удаление книги ---")
    books = load_books()
    if not books:
        print("Список пуст.")
        return

    show_all_books()
    title = input("\nНазвание книги для удаления: ").strip()
    author = input("Автор книги для удаления: ").strip()

    if delete_book(title, author):
        print("\nКнига удалена!")
    else:
        print("\nКнига не найдена.")


if __name__ == "__main__":
    main()
