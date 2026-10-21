import re
from collections import Counter

# === Функції для базових операцій з рядками ===

def find_substring(text, substring):
    """
    Пошук підрядка в тексті.
    Повертає індекс першого входження або -1, якщо підрядок не знайдено.
    """
    return text.find(substring)

def replace_substring(text, old, new):
    """
    Заміна підрядка в тексті.
    """
    return text.replace(old, new)

def split_text(text, delimiter=' '):
    """
    Розділення тексту за роздільником.
    """
    return text.split(delimiter)

def format_string_f(name, age):
    """
    Форматування рядка з використанням f-string.
    Приклад: "Мене звати [name] і мені [age] років."
    """
    return f"Мене звати {name} і мені {age} років."

def format_string_method(name, age):
    """
    Форматування рядка з використанням методу .format().
    Приклад: "Мене звати [name] і мені [age] років."
    """
    return "Мене звати {} і мені {} років.".format(name, age)

# === Функції для роботи з регулярними виразами ===

def extract_emails(text):
    """
    Витяг email адрес з тексту.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def validate_phone_number(number):
    """
    Валідація українського телефонного номера.
    Формат: +380xxxxxxxxx
    """
    pattern = r'^\+?3?8?(0\d{9})$'
    return bool(re.match(pattern, number))

def extract_hashtags(text):
    """
    Витяг хештегів з тексту.
    """
    return re.findall(r'#\w+', text)

def extract_mentions(text):
    """
    Витяг згадувань користувачів з тексту (напр. @user).
    """
    return re.findall(r'@\w+', text)

# === Функції для аналізу тексту ===

def count_words(text):
    """
    Підрахунок кількості слів у тексті.
    """
    return len(re.findall(r'\w+', text))

def count_sentences(text):
    """
    Підрахунок кількості речень у тексті.
    """
    return len(re.findall(r'[.!?]+', text))

def word_frequency(text):
    """
    Підрахунок частоти слів у тексті.
    Повертає об'єкт Counter.
    """
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def analyze_text(text):
    """
    Комплексний аналіз тексту.
    Повертає словник з результатами аналізу.
    """
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    freq = word_frequency(text)
    emails = extract_emails(text)
    hashtags = extract_hashtags(text)
    mentions = extract_mentions(text)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "word_frequency": freq.most_common(5),
        "emails": emails,
        "hashtags": hashtags,
        "mentions": mentions
    }

def format_analysis_results(results):
    """
    Форматування результатів аналізу для зручного виведення.
    """
    output = "Результати аналізу тексту:\n"
    # Додайте форматування для кожного елементу в `results`
    output += f"Кількість слів: {results['word_count']}\n"
    output += f"Кількість речень: {results['sentence_count']}\n"

    output += "Топ 5 найчастіших слів\n"
    for word, count in results['word_frequency']:
        output += f"{word}: {count}\n"

    output += f"\nЗнайдені email адреси: {', '.join(results["emails"])}\n"
    output += f"Знайдені хештеги: {', '.join(results["hashtags"])}\n"
    output += f"Знайдені згадування: {', '.join(results["mentions"])}\n"

    return output

# === Функція для вилучення даних за варіантом ===

def extract_variant_data(text, variant_pattern):
    """
    Вилучає дані з тексту за допомогою патерну, специфічного для варіанту.
    """
    return re.findall(variant_pattern, text)

# === Головна частина програми ===

def read_file_content(filepath):
    """
    Читає вміст файлу.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом {filepath}")
        return None

def main():
    """
    Головна функція, що керує виконанням програми.
    """
    print("Ласкаво просимо до аналізатора тексту!")

    # Шлях до файлу з текстом
    text_filepath = 'C:/Git/lab_4/src/data/neoterra_text.txt'

    # Читання тексту з файлу
    text_to_analyze = read_file_content(text_filepath)
    if not text_to_analyze:
        return # Завершити, якщо файл не прочитано

    while True:
        try:
            print("\nОберіть опцію:")
            print("1. Аналіз тексту 'NeoTerra 3000'")
            print("2. Валідація телефонного номера")
            print("3. Вилучення даних за варіантом")
            print("4. Вихід")
            choice = input("Ваш вибір: ")

            if choice == '1':
                results = analyze_text(text_to_analyze)
                print(format_analysis_results(results))

            elif choice == '2':
                phone = input("Введіть номер телефону для валідації: ")
                if validate_phone_number(phone):
                    print("Номер телефону валідний.")
                else:
                    print("Номер телефону невалідний.")

            elif choice == '3':
                variant = input("Введіть номер вашого варіанту (1-30): ") # 18
                if not variant == '18':
                   print("Не вірний варіант")
                   continue

                print("Цю частину необхідно реалізувати самостійно згідно вашого варіанту.")

                pattern = r'\b[A-Z]{2}-[A-Za-z]{8}\b'
                # pattern2 = r'\bAI-[A-Za-z]+\b'
                variant_data = extract_variant_data(text_to_analyze, pattern)
                print(f"Знайдені дані: {variant_data}")
            elif choice == '4':
                print("Дякуємо за використання аналізатора!")
                break

            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except Exception as e:
            print(f"Виникла помилка: {e}")

if __name__ == '__main__':
    main()
