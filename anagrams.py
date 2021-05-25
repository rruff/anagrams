#!/usr/bin/python3
import sqlite3
from db import WordsDao

DB = 'db/anagrams.db'
CREATE_DB_SCRIPT = 'db/anagrams.sql'
WORDS_FILE = 'data/words_alpha.txt'

def init_db(conn):
    with open(CREATE_DB_SCRIPT) as sql:
        conn.cursor().executescript(sql.read())

def load_words():
    with open(WORDS_FILE) as f:
        words = set(f.read().split())
    
    # words_dict = {}
    # for w in words:
    #     key = sort_chars(w)
    #     if key in words_dict:
    #         words_dict[key].append(w)
    #     else:
    #         words_dict[key] = [w]
    
    return [(w, sort_chars(w)) for w in words]

def insert_words(conn, words):
    words_dao = WordsDao(conn)
    words_dao.insert_words(words)

def find_anagrams(word, word_dict):
    anagrams = []
    chars = sort_chars(word).lower()
    words = word_dict.setdefault(chars, [])
    anagrams.extend([w for w in words if w != word])

    return anagrams

def sort_chars(word):
    return ''.join(sorted(list(word)))

if __name__ == '__main__':
    conn = sqlite3.connect(DB)
    init_db(conn)

    english_words = load_words()
    # Flatten the values into a single list of words
    insert_words(conn, [w for l in english_words.values() for w in l])
    # words = {}
    # with open(WORDS_FILE, 'r') as lines:
    #     for line in lines:
    #         word = line.strip()
    #         sorted_chars = sort_chars(word.lower())
    #         if not sorted_chars in words:
    #             words[sorted_chars] = [word]
    #         else:
    #             words[sorted_chars].append(word)
    
    # load_words(words)
    # w = input("Enter a word: ").strip()
    # print(find_anagrams(w, words))