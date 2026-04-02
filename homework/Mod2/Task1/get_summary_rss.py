import math
import os


def human_readable_size(size_bytes, precision=2):
    """Преобразует размер в байтах в человекочитаемый формат."""
    if size_bytes == 0:
        return '0B'
    SIZE_NAMES = ("KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    i = math.floor(
        math.log(size_bytes, 1024))  # в какую степень 1024 нужно возвести, чтобы получить исходное число байтов
    i = 4 if i > 4 else i
    p = math.pow(1024, i)
    s = round(size_bytes / p, precision)  # Результат с точность 2 знака после запятой
    return f'{s} {SIZE_NAMES[i]}'


def get_summary_rss(path: os.path, precision=2) -> str:
    """Возвращает суммарный объем потребляемой памяти процессами в человекочитаемом формате."""
    with open(path, 'r') as file:
        lines = file.readlines()[1:]
        summary_bytes = sum(int(line.split()[5]) for line in lines)
        return human_readable_size(summary_bytes, precision)


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, 'output_file.txt')
    print(get_summary_rss(BOOK_FILE))