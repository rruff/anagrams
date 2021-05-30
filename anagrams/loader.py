#!/usr/bin/python3

import sqlite3
from settings import CREATE_DATABASE, DATABASE, WORDS_FILE
from utils import sort_chars

class AnagramsLoader:
    """ Pre-loads words and their anagrams into a SQLite database for easy queries. """
    def __init__(self, connection):
        self.conn = connection
        self._init_db()

    def _init_db(self):
        with open(CREATE_DATABASE) as sql:
            with self.conn as c:
                c.executescript(sql.read())

    def load_words(self):
        """ Load the words from `WORDS_FILE` into the database. """
        with open(WORDS_FILE) as f:
            # Read the words into a list of tuples, each containing the original word and
            # the word with its characters sorted alphabetically, e.g. ('xenomorphic', 'cehimnooprx').
            reader = (line.strip() for line in f)
            words = [(w, sort_chars(w.lower())) for w in reader]

        self._insert_words(words)
    
    def _insert_words(self, words):
        try:
            with self.conn as c:
                c.executemany('insert into words (word, sortedword) values (?, ?)', words)
        except sqlite3.DatabaseError as e:
            print(f'Database error {e}')

if __name__ == '__main__':
    try:
        conn = sqlite3.connect(DATABASE)
        aloader = AnagramsLoader(conn)
        aloader.load_words()
    finally:
        conn.close()