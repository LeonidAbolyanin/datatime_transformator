from datetime import datetime

# Поддерживаемые форматы дат
formats = [
    "%A, %B %d, %Y",           # The Moscow Times: Wednesday, October 2, 2002
    "%A, %d.%m.%y",            # The Guardian: Friday, 11.10.13
    "%A, %d %B %Y",            # Daily News: Thursday, 18 August 1977
    "%Y-%m-%d",                # ISO формат: 2002-10-02
    "%d/%m/%Y",                # Европейский формат: 02/10/2002
]

print("Введите дату в одном из форматов или 'exit' для выхода:")
print("Примеры форматов:")
print("  Wednesday, October 2, 2002")
print("  Friday, 11.10.13")
print("  Thursday, 18 August 1977")
print("  2002-10-02")
print("  02/10/2002")
print("-" * 40)

while True:
    user_input = input("Введите дату: ").strip()

    if user_input.lower() == 'exit':
        print("Программа завершена.")
        break

    if not user_input:
        continue

    parsed = False
    for fmt in formats:
        try:
            dt = datetime.strptime(user_input, fmt)
            print(f"Распознано: {dt}")
            parsed = True
            break
        except ValueError:
            continue

    if not parsed:
        print("Ошибка: Не удалось распознать формат даты. Попробуйте другой формат.")
