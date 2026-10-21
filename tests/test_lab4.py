import unittest
import sys
import os

# Додаємо шлях до папки src, щоб можна було імпортувати lab4
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab4 import (
    find_substring,
    replace_substring,
    split_text,
    format_string_f,
    format_string_method,
    extract_emails,
    validate_phone_number,
    extract_hashtags,
    extract_mentions,
    count_words,
    count_sentences,
    word_frequency,
    # Додайте сюди інші функції, які хочете протестувати
)

class TestTextAnalyzer(unittest.TestCase):

    def test_find_substring(self):
        """Тест для функції find_substring."""
        self.assertEqual(find_substring("Hello, world!", "world"), 7)

    def test_replace_substring(self):
        """Тест для функції replace_substring."""
        self.assertEqual(replace_substring("Hello, world!", "world", "Python"), "Hello, Python!")

    def test_split_text(self):
        """Тест для функції split_text."""
        self.assertEqual(split_text("Hello, world!", ", "), ["Hello", "world!"])

    def test_format_string_f(self):
        """Тест для функції format_string_f."""
        self.assertEqual(format_string_f("Влад", 19), "Мене звати Влад і мені 19 років.")

    def test_format_string_method(self):
        """Тест для функції format_string_method."""
        self.assertEqual(format_string_method("Захар", 20), "Мене звати Захар і мені 20 років.")

    def test_extract_emails(self):
        """Тест для функції extract_emails."""
        text = "Contact us at info@example.com or support@test.com"
        expected = ["info@example.com", "support@test.com"]
        self.assertEqual(extract_emails(text), expected)

    def test_validate_phone_number(self):
        """Тест для функції validate_phone_number."""
        self.assertTrue(validate_phone_number("+380123456789"))
        self.assertFalse(validate_phone_number("12345"))

    def test_extract_hashtags(self):
        """Тест для функції extract_hashtags."""
        text = "I love #Python and #Programming"
        expected = ["#Python", "#Programming"]

        self.assertEqual(extract_hashtags(text), expected)

    def test_extract_mentions(self):
        """Тест для функції extract_mentions."""
        text = "Hey, @Rorty, can you forward that file to @d1schon?"
        expected = ["@Rorty", "@d1schon"]

        self.assertEqual(extract_mentions(text), expected)

    def test_count_words(self):
        """Тест для функції count_words."""
        text = "This is a test sentence to figure out how many words are here"
        self.assertEqual(count_words(text), 13)

    def test_count_sentences(self):
        """Тест для функції count_sentences."""
        text = "This is a test text. It has multiple sentences for a test. Br Br patapim."
        self.assertEqual(count_sentences(text), 3)

    # === Додайте власні тести для інших функцій та варіантів ===

    def test_words_frequency(self):
        """Тест для функції word_frequency."""
        text = "This is a test text, where I will try to find how frequent different words are. Apart from that, I love cats and I love petting them all the time."
        self.assertEqual(word_frequency(text).most_common(5), [('i', 3), ('love', 2), ('this', 1), ('is', 1), ('a', 1)])

if __name__ == '__main__':
    # Запуск тестів
    unittest.main(verbosity=2)
