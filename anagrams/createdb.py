#!/usr/bin/env python3

from settings import CREATE_DATABASE, DATABASE
import sqlite3

def create_db(conn):
    with open(CREATE_DATABASE) as sql:
        with conn:
            conn.executescript(sql.read())

def main():
    try:
        conn = sqlite3.connect(DATABASE)
        create_db(conn)
    finally:
        conn.close()

if __name__ =='__main__':
    main()