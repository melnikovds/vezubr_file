from collections import Counter

# Чтение файла с подсчётом повторений
def find_duplicates(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = [line.strip() for line in f if line.strip()]

    counter = Counter(lines)
    duplicates = {line: count for line, count in counter.items() if count > 1}

    print(f"Файл: {filename}")
    print(f"Всего строк: {len(lines)}")
    print(f"Уникальных значений: {len(counter)}")
    print(f"Дубликатов: {len(lines) - len(counter)}")

    if duplicates:
        print(f"\nНайдено {len(duplicates)} повторяющихся строк:\n")
        for line, count in sorted(duplicates.items()):
            print(f"{line} → повторений: {count}")

        # Сохраняем в файл
        with open('дубликаты.txt', 'w', encoding='utf-8') as out:
            out.write(f"Дубликаты в файле {filename}:\n\n")
            for line, count in sorted(duplicates.items()):
                out.write(f"{line}\t(повторов: {count})\n")
        print("\n📋 Список дубликатов сохранён в 'дубликаты.txt'")
    else:
        print("\nДубликатов не найдено")


# Запуск анализа для второго файла
find_duplicates('barcodes2.txt')


# проверка какие именно строки повторяются и сколько раз