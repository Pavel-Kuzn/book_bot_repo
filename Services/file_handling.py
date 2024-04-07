import os
import sys

BOOK_PATH = 'Book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    signs = [',', '.', '!', ':', ';', '?']
    new_text = text[start:start+size]
    for i in range(len(new_text) - 1, 0, -1):
        if new_text[-1] in signs and text[i + 1] not in signs:
            return (new_text, len(new_text))
        else:
            new_text = new_text[0:i]


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    
        start = 0
        number = 1
        while start < len(text):
            page, leng = _get_part_text(text, start, PAGE_SIZE)
            book[number] = page.strip()
            start += leng
            number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))