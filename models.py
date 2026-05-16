"""Модель книги для трекера прочитанных книг."""


class Book:
    """Класс представляющий книгу."""

    def __init__(self, author: str, title: str, rating: int, date_read: str):
        """Инициализация книги.

        Args:
            author: Автор книги
            title: Название книги
            rating: Оценка от 1 до 5
            date_read: Дата прочтения в формате YYYY-MM-DD
        """
        self.author = author
        self.title = title
        self.rating = rating
        self.date_read = date_read

    def to_dict(self) -> dict:
        """Преобразовать книгу в словарь."""
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """Создать книгу из словаря."""
        return cls(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date_read=data["date_read"]
        )

    def __str__(self) -> str:
        """Строковое представление книги."""
        return f"{self.title} — {self.author} ({self.rating}/5)"
