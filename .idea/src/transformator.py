from datetime import datetime

# Даты
dates = {
    "The Moscow Times": "Wednesday, October 2, 2002",
    "The Guardian": "Friday, 11.10.13",
    "Daily News": "Thursday, 18 August 1977"
}

# Форматы
formats = {
    "The Moscow Times": "%A, %B %d, %Y",
    "The Guardian": "%A, %d.%m.%y",
    "Daily News": "%A, %d %B %Y"
}

# Парсинг
for newspaper, date_str in dates.items():
    dt = datetime.strptime(date_str, formats[newspaper])
    print(f"{newspaper}: {dt}")
