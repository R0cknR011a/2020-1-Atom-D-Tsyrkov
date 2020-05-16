import random
import string


class TextGenerator:
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    english_alphabet = string.ascii_lowercase
    numbers = string.digits
    marks = string.punctuation
    marks_weights = [1] * 29
    marks_weights.insert(12, 50)
    marks_weights.insert(13, 10)
    marks_weights.insert(14, 50)
    available_languages = ['RUS', 'ENG']

    def __init__(self, language):
        self.language = language
        self._dictionary = []
        self._hashmap = {}

    @property
    def dictionary(self):
        return self._dictionary

    @dictionary.setter
    def dictionary(self, value):
        if isinstance(value, list):
            for word in value:
                if not isinstance(word, str):
                    raise ValueError('Input values should be type of [str]')
            self._dictionary = value

    @property
    def hashmap(self):
        return self._hashmap
    
    def get_MFQ(self, k):
        tmp = {k: v for k, v in sorted(self._hashmap.items(), key=lambda item: item[1], reverse=True)}
        result = {}
        for key, value in tmp.items():
            result[key] = value
            if len(result) == k:
                break
        return result

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value in self.available_languages:
            self._language = value
            return
        raise ValueError('Language is not available')

    def generate_dictionary(self, word_min, word_max, length):
        alphabet = {
            'RUS': self.russian_alphabet,
            'ENG': self.english_alphabet,
        }[self._language]
        for _ in range(length):
            self.dictionary.append(''.join(random.choices(alphabet, k=random.randint(word_min, word_max))))

    def reset_hashmap(self):
        self._hashmap = {}

    def get_line(self, line_min, line_max):
        result = []
        chars = ['word', 'mark', 'number']
        for i in range(random.randint(line_min, line_max)):
            choice = random.choices(chars, weights=[6, 2, 1])[0]
            if choice == 'word':
                word = random.choices(self.dictionary)[0]
                if word in self.hashmap:
                    self.hashmap[word] += 1
                else:
                    self.hashmap[word] = 0
            else:
                word = None
            result.append({
                'word': word,
                'mark': ''.join(random.choices(self.marks, k=random.choices([1, 2, 3], weights=[50, 5, 1])[0], weights=self.marks_weights)),
                'number': ''.join(random.choices(self.numbers, k=random.randint(1, 3))),
            }[choice])
        return ' '.join(result)

    def get_text(self, line_min, line_max, lines):
        self._hashmap = {}
        result = []
        for _ in range(lines):
            result.append(self.get_line(line_min, line_max))
        return '\n'.join(result)
