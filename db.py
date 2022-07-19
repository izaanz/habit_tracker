"""
The database module: Primarily creates database tables, stores information and returns data.
"""

import sqlite3


def connect_database(name="main.db"):
    """
    Function to create and maintain connection with database.

    :param name: Name of the database to create or connect with (default main.db)
    :return: Returns the database connection
    """
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    """
    Creates two database tables: namely 'habit_tracker and 'habit_log'.

    The habit_tracker database consists of the following columns: habit, periodicity, category,
    creation_time, streak, and completion_time.
    The habit_log database has the following columns: habit, completed, streak, and completion_time.

    :param db: To maintain connection with the database
    """
    cur = db.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS habit_tracker (
               habit TEXT PRIMARY KEY , 
               periodicity TEXT,
               category TEXT,
               creation_time TEXT,
               streak INT,
               completion_time TEXT   
           )''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS habit_log (
            habit TEXT,
            completed BOOL,
            streak INT DEFAULT 0,
            completion_time TIME,
            FOREIGN KEY (habit) REFERENCES habit_tracker(habit)
        )''')
    db.commit()


def add_habit(db, name, periodicity, category, creation_time, streak, completion_time=None):
    """
    Adds the habit information to the habit_tracker database.

    :param db: To maintain connection with the database
    :param name: Name of the habit
    :param periodicity: Periodicity of the habit (e.g., daily, weekly, or monthly)
    :param category: Category of the habit
    :param creation_time: Time of habit creation
    :param streak: Streak of the habit (if any), int
    :param completion_time: Time when habit was marked as completed, optional
    """
    cur = db.cursor()
    cur.execute("INSERT INTO habit_tracker VALUES(?, ?, ?, ?, ?, ?)",
                (name, periodicity, category,
                 creation_time, streak, completion_time))
    db.commit()


def update_log(db, name, is_completed, streak, completion_time):
    """
    Updates the habit_log database with the provided data.

    :param db: To maintain connection with the database
    :param name: Name of the habit
    :param is_completed: Whether habit was completed or not, boolean
    :param streak: Streak of the habit, int
    :param completion_time: Time when habit was marked as completed
        """
    cur = db.cursor()
    cur.execute("INSERT INTO habit_log VALUES(?, ?, ?, ?)",
                (name, is_completed, streak, completion_time))
    db.commit()


def habit_exists(db, habit_name):
    """
    Checks if the provided habit exists in database or not.

    :param db: To maintain connection with the database
    :param habit_name: Name of the habit
    :return: Returns True if habit is in the database already else returns False
    """
    cur = db.cursor()
    query = """SELECT * FROM habit_tracker WHERE habit = ?"""
    cur.execute(query, (habit_name,))
    data = cur.fetchone()
    return True if data is not None else False


def remove_habit(db, habit_name):
    """
    Removes the provided habit from the habit_tracker database and also resets the log
    of the specified habit.

    :param db: To maintain connection with the database
    :param habit_name: Name of the habit
    """
    cur = db.cursor()
    cur.execute(f"DELETE FROM habit_tracker WHERE habit == '{habit_name}';")
    db.commit()
    reset_logs(db, habit_name)


def fetch_categories(db):
    """
    Gets all the categories listed in the habit_tracker database.

    :param db: To maintain connection with the database
    :return: Returns the list of category names
    """
    cur = db.cursor()
    cur.execute("SELECT category FROM habit_tracker")
    data = cur.fetchall()
    return [i[0].capitalize() for i in set(data)]


def delete_category(db, category_name):
    """
    Deletes the specified category from the habit_tracker database.

    :param db: To maintain connection with the database
    :param category_name: Name of the category
    """
    cur = db.cursor()
    cur.execute(f"DELETE FROM habit_Tracker where category == '{category_name}';")
    db.commit()


def fetch_habits_as_choices(db):
    """
    Gets all the habits listed in the habit_tracker database.

    :param db: To maintain connection with the database
    :return: Returns the list of habit names
    """
    cur = db.cursor()
    cur.execute("SELECT habit FROM habit_tracker")
    data = cur.fetchall()
    return [i[0].capitalize() for i in set(data)] if len(data) > 0 else None


def update_periodicity(db, habit_name, new_periodicity):
    """
    Changes the periodicity of the specified habit to a new periodicity and also resets logs
    of the specified habit.

    :param db: To maintain connection with the database
    :param habit_name: Name of the habit
    :param new_periodicity: New periodicity to assign to the habit
    """
    cur = db.cursor()
    query = "UPDATE habit_tracker SET periodicity = ?, streak = 0, completion_time = NULL WHERE habit = ?"
    data = (new_periodicity, habit_name)
    cur.execute(query, data)
    db.commit()
    reset_logs(db, habit_name)


def get_streak_count(db, habit_name):
    """
    Returns the current streak of the specified habit.

    :param db: To maintain connection with the database
    :param habit_name: Name of the habit
    :return: Returns the current streak count of the specified habit, int
    """
    cur = db.cursor()
    query = "SELECT streak FROM habit_tracker WHERE habit = ?"
    cur.execute(query, (habit_name,))
    streak_count = cur.fetchall()
    return streak_count[0][0]


def update_habit_streak(db, habit_name, streak, time=None):
    """
    Updates the streak of the specified habit.

    :param db: To maintain connection with the database
    :param habit_name: Name of the habit
    :param streak: New streak for the habit, int
    :param time: Time when the streak has been updated
    """
    cur = db.cursor()
    query = "UPDATE habit_tracker SET streak = ?, completion_time = ? WHERE habit = ?"
    data = (streak, time, habit_name)
    cur.execute(query, data)
    db.commit()


def reset_logs(db, habit_name):
    """
    Resets the old log entries of the specified habit.

    :param db: To maintain connection with the database
    :param habit_name: Name of the habit
    """
    cur = db.cursor()
    query = "DELETE FROM habit_log WHERE habit = ?"
    cur.execute(query, (habit_name,))
    db.commit()


def get_habit_completion_time(db, habit_name):
    """
    Returns the last time when the habit was marked as completed.

    :param db: To maintain connection with the database
    :param habit_name: Name of the habit
    :return: Returns the time, int
    """
    cur = db.cursor()
    query = "SELECT completion_time FROM habit_tracker WHERE habit = ?"
    cur.execute(query, (habit_name,))
    data = cur.fetchall()
    return data[0][0]


def fetch_habit_periodicity(db, habit_name):
    """
    Returns the assigned periodicity of the specified.

    :param db: To maintain connection with the database
    :param habit_name: Name of the habit
    :return: Returns the periodicity assigned to the habit
    """
    cur = db.cursor()
    query = "SELECT periodicity FROM habit_tracker WHERE habit =?"
    cur.execute(query, (habit_name,))
    data = cur.fetchall()
    return data[0][0]
