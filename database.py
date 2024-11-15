import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('habit_tracker.db')
cursor = conn.cursor()

# Create the Habits table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    description TEXT
);
''')

# Create a table for habit completion records if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS HabitCompletion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_id INTEGER,
    date TEXT NOT NULL,
    completed BOOLEAN,
    FOREIGN KEY (habit_id) REFERENCES Habits(id)
);
''')

# Commit changes and close the connection
conn.commit()

# Function to add a new habit
def add_habit(name, description):
    start_date = "2024-11-15"  
    cursor.execute('''
    INSERT INTO Habits (name, start_date, description)
    VALUES (?, ?, ?)
    ''', (name, start_date, description))
    conn.commit()

# Function to mark a habit as completed for today
def mark_habit_completed(habit_id):
    today = "2024-11-15"  
    cursor.execute('''
    INSERT INTO HabitCompletion (habit_id, date, completed)
    VALUES (?, ?, ?)
    ''', (habit_id, today, True))
    conn.commit()

# Function to get all habits
def get_all_habits():
    cursor.execute('SELECT * FROM Habits')
    return cursor.fetchall()

# Function to get habit completion history
def get_habit_completion(habit_id):
    cursor.execute('SELECT * FROM HabitCompletion WHERE habit_id = ?', (habit_id,))
    return cursor.fetchall()

# Close the connection
def close_db():
    conn.close()


