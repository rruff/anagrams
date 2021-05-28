#!/usr/bin/python3

import sqlite3
from settings import CREATE_DATABASE, DATABASE, WORDS_FILE

class AnagramsLoader:
    """ Pre-load words and their anagrams into a SQLite database for easy queries. """
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        with open(CREATE_DATABASE) as sql:
            with self.conn as c:
                c.executescript(sql.read())

    def load_words(self):
        """ 
        Load the words from `WORDS_FILE` into memory and then insert into the DB. 
        The words are read into a list of tuples, where the first element is the word, and
        the second element is the characters in the word sorted alphabetically, e.g. ('xenomorphic', 'cehimnooprx').
        """
        with open(WORDS_FILE) as f:
            words = [(w, self._sort_chars(w.lower())) for w in f.read().split()]

        self._insert_words(words)
    
    def _insert_words(self, words):
        try:
            with self.conn as c:
                c.executemany('insert into words (word, sortedword) values (?, ?)', words)
        except sqlite3.DatabaseError as e:
            print(f'Database error {e}')

    def _sort_chars(self, word):
        """ Sort the characters in `word` alphabetically. """
        return ''.join(sorted(list(word)))

if __name__ == '__main__':
    conn = sqlite3.connect(DATABASE)
    aloader = AnagramsLoader(conn)
    aloader.load_words()
    conn.close()
