import sqlite3


def import_receipts():
    conn = sqlite3.connect('receiptsdb')
    cd = conn.cursor()

    conn.commit()
    conn.close()

