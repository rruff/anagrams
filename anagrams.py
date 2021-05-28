#!/usr/bin/env python3

from settings import DATABASE
from utils import sort_chars
import sqlite3
import sys

class Anagrams:
    def __init__(self, conn):
        self.conn = conn
    
    def find(self, word):
        """ Find anagrams for `word`. """
        try:
            with self.conn as c:
                cur = c.execute('select word from words where sortedword = (?) and word != (?)', (sort_chars(word), word))
                anagrams = []
                results = cur.fetchmany()
                while results:
                    for a in results:
                        anagrams.extend(a)
                    results = cur.fetchmany()
        except sqlite3.DatabaseError as e:
            print(f'Database error: {e}')
        
        return anagrams

if __name__ == '__main__':
    conn = sqlite3.connect(DATABASE)
    finder = Anagrams(conn)

    word = sys.argv[1]
    anagrams = finder.find(word)
    print(f'{anagrams=}')