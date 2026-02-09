# Чтение файлов
with open('file1.txt', 'r', encoding='utf-8') as f1:
    list1 = [line.strip() for line in f1 if line.strip()]  # убираем пробелы и пустые строки

with open('file2.txt', 'r', encoding='utf-8') as f2:
    list2 = [line.strip() for line in f2 if line.strip()]

# Преобразуем в множества для быстрого сравнения
set1 = set(list1)
set2 = set(list2)

# Уникальные значения: есть только в одном из списков (симметрическая разность)
unique_values = set1.symmetric_difference(set2)

# Или по отдельности:
only_in_file1 = set1 - set2  # есть только в первом файле
only_in_file2 = set2 - set1  # есть только во втором файле

# Выводим результаты
print(f"Всего строк в файле 1: {len(list1)}")
print(f"Всего строк в файле 2: {len(list2)}")
print(f"\nУникальных значений (есть только в одном файле): {len(unique_values)}")
print("\nЗначения только в файле 1:")
for val in sorted(only_in_file1):
    print(val)

print("\nЗначения только в файле 2:")
for val in sorted(only_in_file2):
    print(val)

# Сохраняем результат в файл (опционально)
with open('unique_values.txt', 'w', encoding='utf-8') as out:
    out.write("=== Только в файле 1 ===\n")
    for val in sorted(only_in_file1):
        out.write(val + '\n')

    out.write("\n=== Только в файле 2 ===\n")
    for val in sorted(only_in_file2):
        out.write(val + '\n')

print("\nРезультат сохранён в файл unique_values.txt")


# Скопируйте оба .txt файла прямо в папку проекта
# Переименуйте их в простые имена без пробелов и кириллицы, например:
# barcodes1.txt
# barcodes2.txt
# Используйте этот упрощённый скрипт
