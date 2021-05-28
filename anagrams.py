from settings import DATABASE
import sqlite3
import sys

class Anagrams:
    def __init__(self, conn):
        self.conn = conn
    
    def find(self, word):
        try:
            with self.conn as c:
                chars = ''.join(sorted(list(word)))
                cur = c.execute('select word from words where sortedword = (?) and word != ?', (chars, word))
                anagrams = []
                results = cur.fetchmany()
                while results:
                    for a in results:
                        anagrams.append(a)
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