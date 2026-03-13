import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'students.db')

def migrate():
    print(f"Connecting to database at {DB_PATH}...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check current columns in students table
    cursor.execute("PRAGMA table_info(students)")
    columns = [row[1] for row in cursor.fetchall()]
    print(f"Current columns: {columns}")
    
    # Add email if missing
    if 'email' not in columns:
        print("Adding 'email' column to 'students' table...")
        cursor.execute("ALTER TABLE students ADD COLUMN email TEXT")
    else:
        print("'email' column already exists.")
        
    # Add phone if missing
    if 'phone' not in columns:
        print("Adding 'phone' column to 'students' table...")
        cursor.execute("ALTER TABLE students ADD COLUMN phone TEXT")
    else:
        print("'phone' column already exists.")
        
    conn.commit()
    conn.close()
    print("Migration completed successfully!")

if __name__ == "__main__":
    migrate()
