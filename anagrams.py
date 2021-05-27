#!/usr/bin/python3
import sqlite3
from db import WordsDao

DB = 'db/anagrams.db'
CREATE_DB_SCRIPT = 'db/anagrams.sql'
WORDS_FILE = 'data/words_alpha.txt'

class AnagramsLoader:
    """ Pre-load words and their anagrams into a SQLite database for easy queries. """
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        with open(CREATE_DB_SCRIPT) as sql:
            self.cursor.executescript(sql.read())

    def load_words(self):
        with open(WORDS_FILE) as f:
            words = tuple(f.read().split())

        self._insert_words(words)
    
    def _insert_words(self, words):
        self.cursor.executemany('insert into words (word) values (?)', list((w,) for w in words))
        self.conn.commit()

    def load_anagrams(self):
        self.cursor.arraysize = 100
        self.cursor.execute('select id, word from words limit 10000')
        anagrams = {}
        results = self.cursor.fetchmany()
        while results:
            # results is a list of tuples
            self.build_anagrams_map(results, anagrams)
            results = self.cursor.fetchmany()
        return anagrams

    def build_anagrams_map(self, words, anagrams_map):
        for id, word in words:
            chars = self._sort_chars(word)
            if chars in anagrams_map:
                anagrams_map[chars].append(id)
            else:
                anagrams_map[chars] = []

    def _sort_chars(self, word):
        return ''.join(sorted(list(word)))

    def _placeholders(self, count):
        return "?," * (count - 1) + "?"


# def load_anagrams(cursor, map):
    # cursor.execute('select id, word from words')
    # results = cursor.fetchmany()
    # while results:
    #     for r in results:
    #         id, word = r
    #         anagrams = (a for a in map[sort_chars(word)] if a != word)
    #         select = f'select id, word from words where word in ({create_placeholders(len(anagrams))})'
    #         cursor.execute(select, anagrams)


# def find_anagrams(word, anagrams_map):
#     return tuple(a for a in anagrams_map[sort_chars(word)] if a != word)

# if __name__ == '__main__':
    # conn = sqlite3.connect(DB)
    # init_db(conn)

    # english_words = load_words()
    # insert_words(conn, english_words)
