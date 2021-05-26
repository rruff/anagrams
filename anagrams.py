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
        words = tuple(f.read().split())

    return words

def insert_words(conn, words):
    words_dao = WordsDao(conn)
    words_dao.insert_words(words)

def build_anagrams_map(words):
    anagrams = {}
    for word in words:
        chars = sort_chars(word)
        if chars in anagrams:
            val = anagrams[chars]
            anagrams[chars] = val[0:] + (word,)
        else:
            anagrams[chars] = tuple()
    return anagrams

def find_anagrams(word, anagrams_map):
    return tuple(a for a in anagrams_map[sort_chars(word)] if a != word)

def sort_chars(word):
    return ''.join(sorted(list(word)))

if __name__ == '__main__':
    conn = sqlite3.connect(DB)
    init_db(conn)

    english_words = load_words()
    insert_words(conn, english_words)
