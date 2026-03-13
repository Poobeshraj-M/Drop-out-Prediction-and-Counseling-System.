import sqlite3
import os
from datetime import datetime

DB_PATH = 'students.db'

def test_logs():
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found.")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Trigger a dummy log (similar to log_event but directly for test)
    username = "test_user"
    event = "Test Event"
    details = "Verifying local timestamp"
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"Current local time: {current_time}")
    
    cursor.execute('INSERT INTO audit_logs (username, event, details, timestamp) VALUES (?, ?, ?, ?)', 
                 (username, event, details, current_time))
    conn.commit()
    
    # Check latest audit logs
    cursor.execute('SELECT * FROM audit_logs ORDER BY id DESC LIMIT 1')
    log = cursor.fetchone()
    print(f"Last Log in DB: {log}")
    
    conn.close()

if __name__ == "__main__":
    test_logs()
