"""Модуль для расчёта статистики по прочитанным книгам."""

from typing import Dict, List, Tuple
from storage import load_books


def get_average_rating() -> float:
    """Получить среднюю оценку всех книг.

    Returns:
        Средняя оценка, 0.0 если книг нет
    """
    books = load_books()
    if not books:
        return 0.0
    total = sum(book.rating for book in books)
    return total / len(books)


def get_author_stats() -> Dict[str, Dict[str, any]]:
    """Получить статистику по авторам.

    Returns:
        Словарь {автор: {"count": количество, "avg_rating": средняя_оценка}}
    """
    books = load_books()
    stats = {}

    for book in books:
        author = book.author
        if author not in stats:
            stats[author] = {"count": 0, "total_rating": 0}
        stats[author]["count"] += 1
        stats[author]["total_rating"] += book.rating

    for author in stats:
        stats[author]["avg_rating"] = (
            stats[author]["total_rating"] / stats[author]["count"]
        )

    return stats


def get_top_authors(limit: int = 5) -> List[Tuple[str, int]]:
    """Получить топ авторов по количеству прочитанных книг.

    Args:
        limit: Максимальное количество авторов в результате

    Returns:
        Список кортежей [(автор, количество), ...] отсортированный по убыванию
    """
    stats = get_author_stats()
    sorted_authors = sorted(
        stats.items(),
        key=lambda x: x[1]["count"],
        reverse=True
    )
    return [(author, data["count"]) for author, data in sorted_authors[:limit]]
