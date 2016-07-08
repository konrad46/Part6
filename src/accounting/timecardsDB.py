import sqlite3


def import_timecards():
    conn = sqlite3.connect('timecardsdb')
    cd = conn.cursor()

    conn.commit()
    conn.close()