import sqlite3
import os

DB_PATH = 'students.db'

def check_db():
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found.")
        return
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    print("--- Students Table ---")
    cursor.execute("SELECT DISTINCT department FROM students")
    depts = cursor.fetchall()
    for row in depts:
        print(f"Department: '{row['department']}'")
    
    cursor.execute("SELECT COUNT(*) as count FROM students")
    count = cursor.fetchone()['count']
    print(f"Total students: {count}")
    
    conn.close()

if __name__ == "__main__":
    check_db()
