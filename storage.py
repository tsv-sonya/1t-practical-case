"""Модуль для хранения и управления книгами в JSON-файле."""

import json
from pathlib import Path
from typing import List, Optional
from models import Book


BOOKS_FILE = Path(__file__).parent / "books.json"


def load_books() -> List[Book]:
    """Загрузить все книги из файла."""
    if not BOOKS_FILE.exists():
        return []
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Book.from_dict(book) for book in data]
    except (json.JSONDecodeError, KeyError):
        return []


def save_books(books: List[Book]) -> None:
    """Сохранить все книги в файл."""
    data = [book.to_dict() for book in books]
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_book(book: Book) -> None:
    """Добавить книгу в хранилище."""
    books = load_books()
    books.append(book)
    save_books(books)


def delete_book(title: str, author: str) -> bool:
    """Удалить книгу по названию и автору.

    Returns:
        True если книга была удалена, False если не найдена
    """
    books = load_books()
    original_len = len(books)
    books = [b for b in books if not (b.title == title and b.author == author)]
    if len(books) < original_len:
        save_books(books)
        return True
    return False


def find_books(author: Optional[str] = None) -> List[Book]:
    """Найти книги по автору.

    Args:
        author: Автор для фильтрации, если None - вернуть все книги

    Returns:
        Список найденных книг
    """
    books = load_books()
    if author:
        books = [b for b in books if b.author.lower() == author.lower()]
    return books
