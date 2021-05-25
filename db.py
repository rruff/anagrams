import sqlite3

class AnagramsDao:
    def __init__(self, ds):
        self.ds = ds

    def insert_anagrams(self, word_id, anagrams):
        if not type(anagrams) is list:
            anagrams = [anagrams]
        self.ds.executemany('insert into anagrams (word_id, anagram) values (?, ?)',
                list(tuple([word_id, a]) for a in anagrams))
        self.ds.commit()
    
    def find_all_by_word(self, word):
        self.ds.execute('select anagram from anagrams a join words w on a.word_id = w.id where word = ?', (word,))
        return list(t[0] for t in self.cursor.fetchall())

class WordsDao:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        
    # def insert_anagrams(self, word_id, anagrams):

    def insert_word(self, word):
        result = self.cursor.execute('insert into words (word) values (?)', (word,))
        self.conn.commit()
        return result
    
    def insert_words(self, words):
        """ Accepts a list of words and inserts them into the database. """
        # `executemany` expects a sequence of tuples, so map each word to a single item tuple.
        self.cursor.executemany('insert into words (word) values (?)', list((w,) for w in words))
        self.conn.commit()

    def find(self, word):
        self.cursor.execute('select id, word from words where word = ?', (word,))
        return self.cursor.fetchone()
