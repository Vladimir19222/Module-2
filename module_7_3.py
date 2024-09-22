import io
from pprint import pprint
class WordsFinder:
    file_names = []

    def __init__(self, *files_name):
        self.files_name = [*files_name]

    def get_all_words(self):
        all_words = {}
        for l in self.files_name:
            words = []
            with open(l, 'r', encoding='cp1252') as file:
                strl = ''
                for line in file:
                    strl = strl + line.lower()
                for h in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    strl = strl.replace(h, '')
                words.append(str.split(strl))
            all_words[l] = [x for y in words for x in y]
        return all_words

    def find(self, word):
        dict1_ = {}
        for name, words in self.get_all_words().items():
            for p in words:
                if p == word.lower():
                   dict1_[name] = words.index(p) + 1
                   break
        return dict1_

    def count(self, word):
        dict2_ = {}
        for name, words in self.get_all_words().items():
            dict2_[name] = words.count(word.lower())
        return dict2_

finder2 = WordsFinder('test_file.txt')
print((finder2.get_all_words()))
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
