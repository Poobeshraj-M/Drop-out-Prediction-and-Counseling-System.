import sqlite3
import os
from datetime import datetime

DB_PATH = 'students.db'

def seed_data():
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found.")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Dummy data
    students = [
        ('Alice Smith', 'CS001', 'Computer Science', 85.0, 78.5, 0, 9, 2, 5.0, 4, 1, 'Low', 'Keep up the good work.'),
        ('Bob Jones', 'EL002', 'Electronics', 60.5, 55.0, 2, 6, 1, 15.0, 7, -1, 'High', 'Seek counseling immediately.'),
        ('Charlie Brown', 'ME003', 'Mechanical', 72.0, 68.0, 1, 8, 2, 10.0, 5, 0, 'Medium', 'Attend extra classes.'),
        ('Diana Prince', 'CS004', 'Computer Science', 95.0, 92.0, 0, 10, 3, 2.0, 2, 1, 'Low', 'Excellent performance.'),
    ]
    
    for s in students:
        cursor.execute('''
            INSERT INTO students 
            (student_name, roll_number, department, attendance, marks, arrears, assignments, family_income, 
             travel_distance, stress_level, feedback_sentiment, dropout_risk, counseling_recommendation, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', s + (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
    
    conn.commit()
    conn.close()
    print("Seed data inserted successfully!")

if __name__ == "__main__":
    seed_data()
