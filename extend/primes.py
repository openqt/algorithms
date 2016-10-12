"""
Generate primes
"""
from __future__ import print_function
import logging
import sqlite3
from projecteuler.e0007_10001st_primes import prime

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    conn = sqlite3.connect('primes.sqlite')
    cursor = conn.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS primes (id INT PRIMARY KEY ASC);')
    conn.commit()

    try:
        n = cursor.execute('SELECT max(id) FROM primes;').fetchone()[0] or 1
        logging.info('start from {}'.format(n))

        while True:
            for i in prime(start=n, stop=100):
                cursor.execute('INSERT OR IGNORE INTO primes VALUES (?);', (i,))
            n = i
            conn.commit()
            logging.info('committed to {}'.format(i))
    finally:
        logging.info('close sqlite.')
        conn.commit()
        conn.close()
