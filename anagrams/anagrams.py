#!/usr/bin/env python3

from settings import DATABASE
from utils import sort_chars
import sqlite3
import sys

class Anagrams:
    def __init__(self, conn=sqlite3.connect(DATABASE)):
        self._conn = conn
    
    def __del__(self):
        if self._conn:
            self._conn.close()
    
    def find(self, word):
        """ Returns a list of anagrams for `word`. """
        anagrams = []
        try:
            with self._conn as c:
                results = c.execute('select word from words where sortedword = (?) and word != (?)', (sort_chars(word), word))
                for row in results:
                    anagrams.extend(row)
        except sqlite3.DatabaseError as e:
            print(f'Database error: {e}')
        
        return anagrams

    def find_many(self, words):
        """ Returns a dictionary mapping words to lists of anagrams. """
        anagrams = {}
        for w in words:
            anagrams[w] = self.find(w)

        return anagrams

if __name__ == '__main__':
    finder = Anagrams()

    word = sys.argv[1]
    anagrams = finder.find(word)

    if anagrams:
        print(f'Anagrams for {word}:')
        print(*anagrams)
    else:
        print(f'No anagrams found for {word}')