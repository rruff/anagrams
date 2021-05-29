import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')
WORDS_FILE = os.path.join(DATA_DIR, 'words_alpha.txt')

DATABASE = os.path.join(DATA_DIR, 'anagrams.db')

SQL_DIR = os.path.join(BASE_DIR, 'sql')
CREATE_DATABASE = os.path.join(SQL_DIR, 'create.sql')