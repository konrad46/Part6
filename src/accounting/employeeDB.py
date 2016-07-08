import sqlite3

def import_employees():
    conn = sqlite3.connect('employeeDB')
    cd = conn.cursor()



    conn.commit()
    conn.close()


