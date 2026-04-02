import statistics
import sys
import math


# From task_2
def human_readable_size(size_bytes, precision=2):
    """Преобразует размер в байтах в человекочитаемый формат."""
    if size_bytes == 0:
        return '0B'
    SIZE_NAMES = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    i = math.floor(
        math.log(size_bytes, 1024))  # в какую степень 1024 нужно возвести, чтобы получить исходное число байтов
    i = 4 if i > 4 else i
    p = math.pow(1024, i)
    s = round(size_bytes / p, precision)  # Результат с точность 2 знака после запятой
    return f'{s} {SIZE_NAMES[i]}'


def get_mean_size(lines):
    if not lines:
        return 'Empty folder'
    try:
        size = [int(line.split()[4]) for line in lines if line.startswith('-')]
        if not size:
            return 'No file in folder'
        return human_readable_size(statistics.mean(size))
    except ValueError:
        return 'Failed to get file sizes'
    except:
        return 'Failed, unknown error'


if __name__ == '__main__':
    input_lines = sys.stdin.readlines()[1:]
    print(get_mean_size(input_lines))