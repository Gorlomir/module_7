import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    punctuation = ',.!?;:"\'-'
                    content_without_punctuation = ''.join(char for char in content if char not in punctuation)
                    words = content_without_punctuation.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except UnicodeDecodeError:
                print(f"Ошибка декодирования при чтении файла {file_name}")

        return all_words

    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            try:
                index = next(i for i, w in enumerate(words) if w.lower() == word.lower())
                result[file_name] = index
            except StopIteration:
                result[file_name] = None

        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word.lower())

        return result

    def print_results(self):
        for method_name in ['get_all_words', 'find', 'count']:
            method = getattr(self, method_name)
            result = method()

            if isinstance(result, dict):
                pprint(result, indent=4)
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего