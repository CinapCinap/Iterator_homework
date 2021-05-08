import json
from hashlib import md5


# Задача 1 - класс итератора
class CountryIterator:

    def __init__(self, path: str):
        self.start = 0
        self.file = open(path, encoding='utf-8')
        self.data = json.load(self.file)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.start >= len(self.data):
                self.file.close()
                raise StopIteration
            country_name = self.data[self.start]['name']['common']
            self.start += 1
            return country_name
        except TypeError:
            self.file.close()


def country_print(file_r, file_w):
    for country in CountryIterator(file_r):
        with open(file_w, 'a', encoding='utf-8') as f:
            f.write(f'{country} : http://en.wikipedia.org/wiki/{country}\n')


# Задача 2 - генератор
def hash_generate(path):
    with open(path) as file:
        for line in file:
            yield md5(line.encode()).hexdigest()


if __name__ == '__main__':
    country_print('countries.json', 'wiki_links.txt')
    for item in hash_generate('countries.json'):
        print(item)
