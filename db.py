import sqlite3
from sqlite3 import Error

DB = 'db/anagrams.db'
CREATE_DB_SCRIPT = 'db/anagrams.sql'

class DataSource:
    def __init__(self):
        self.conn = sqlite3.connect(DB)
        self.cursor = self.conn.cursor()
        self._init_db()
    
    def _init_db(self):
        with open(CREATE_DB_SCRIPT) as sql:
            self.cursor.executescript(sql.read())

class AnagramsDao:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def insert_anagrams(self, word_id, anagrams):
        if not type(anagrams) is list:
            anagrams = [anagrams]
        self.cursor.executemany('insert into anagrams (word_id, anagram) values (?, ?)',
                list(tuple([word_id, a]) for a in anagrams))
        self.conn.commit()
        return self.cursor.fetchall()
    
    def find_all_by_word(self, word):
        self.cursor.execute('select anagram from anagrams a join words w on a.word_id = w.id where word = ?', (word,))
        return list(t[0] for t in self.cursor.fetchall())

class WordsDao:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()
        
    def insert_word(self, word):
        self.cursor.execute('insert into words (word) values (?)', (word,))
        self.conn.commit()
        return self.cursor.fetchone()
    
    def find(self, word):
        self.cursor.execute('select id, word from words where word = ?', (word,))
        return self.cursor.fetchone()
