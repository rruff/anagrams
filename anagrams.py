#!/usr/bin/python3
import sys
# from db import AnagramsDao, WordsDao, DataSource, init_words

WORDS_FILE = '/usr/share/dict/words'

# class Anagrams:
#     def __init__(self, anagrams_dao, words_dao):
#         self.anagrams_dao = anagrams_dao
#         self.words_dao = words_dao
    
#     def add(self, word, anagrams):
#         found = self.words_dao.find(word)
#         word_id, word = found if found else self.words_dao.insert_word(word)
#         self.anagrams_dao.insert_anagrams(word_id, anagrams)
    
#     def find(self, word):
#         return self.anagrams_dao.find_all_by_word(word)

def find_anagrams(word, word_list):
    anagrams = []
    chars = sort_chars(word)
    for w in word_list:
        if sort_chars(w) == chars and w != word:
            anagrams.append(w)

    return anagrams

def sort_chars(word):
    return ''.join(sorted(list(word)))

if __name__ == '__main__':
    words = []
    with open(WORDS_FILE, 'r') as lines:
        for line in lines:
            words.append(line.strip())

    if len(sys.argv) > 1:
        in_word = sys.argv[1].strip()
    else:
        in_word = input("Enter a word: ").strip()
    
    anagrams = find_anagrams(in_word, words)
    print(anagrams if anagrams else f"No anagrams found for word {in_word}")
