import argparse
import os

# 1. Запускать скрипт из текущей директории
# 2. Указать полный путь к файлу

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Введите путь к папке файлов")
parser.add_argument("value", help="Введите значение поиска")
args = parser.parse_args()

# Собираем все названия файлов из папки
files = os.listdir(args.path)

# Производим поиск в каждом файле
for file in files:
    with open(os.path.join(args.path, file)) as logs:
        for i, line in enumerate(logs):
            if args.value in line:
                print(f"Файл: {file}, Строка {i}: {line}")
