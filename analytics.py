"""
The analytics module: Gathers, evaluates and displays the analytical data.

Module is called when the user chooses "Show Habits (All or Sort by Periodicity)" or "Analytics".
"""

from db import connect_database


def data_of_all_habits(db) -> list:
    """
    Gets the list of all habits stored in habit_tracker database.

    :param db: To maintain connection with the database.
    :return: list of all habits
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM habit_tracker")
    records = cur.fetchall()
    return records


def data_of_custom_periodicity_habits(db, periodicity) -> list:
    """
    Gets the list of all habits of the specified periodicity.

    :param db: To maintain connection with the database
    :param periodicity: To get list of specified periodicity habits
    :return: list of all specified periodicity habits
    """
    cur = db.cursor()
    query = "SELECT * FROM habit_tracker WHERE periodicity = ?"
    cur.execute(query, (periodicity,))
    records = cur.fetchall()
    return records


def data_of_single_habit(db, habit_name) -> list:
    """
    Returns the data of specified single habit.

    :param db: To maintain connection with the database
    :param habit_name: Habit name to gather data of
    :return: Data of specified habit
    """
    cur = db.cursor()
    query = "SELECT * FROM habit_tracker WHERE habit = ?"
    cur.execute(query, (habit_name,))
    record = cur.fetchall()
    return record


def longest_habit_streak(db, habit_name) -> int:
    """
    Gets and returns the longest habit streak ever achieved from the habit_log database.

    :param db: To maintain connection with the database
    :param habit_name: Habit name to gather data of
    :return: longest streak of specified habit
    """
    cur = db.cursor()
    query = "SELECT MAX(streak) FROM habit_log WHERE habit = ?"
    cur.execute(query, (habit_name,))
    data = cur.fetchone()
    return data[0]


def habit_log(db, habit_name) -> list:
    """
    Fetches specified habit data from the habit_log database and then returns it.

    :param db: To maintain connection with the database
    :param habit_name: Habit name to gather data of
    :return: The data of specified habit name
    """
    cur = db.cursor()
    query = "SELECT * FROM habit_log WHERE habit = ?"
    cur.execute(query, (habit_name,))
    record = cur.fetchall()
    return record


# Table to show periodicity wise habit's data without streak
def show_habits_data(periodicity=None):
    """
    Shows the all the habit data (without streak) in a readable tabular format.

    The table is formatted using string formatting technique and consists of the following columns:
    Name, Periodicity, Category and Date/Time.
    The habit data from database is retrieved and looped throughout to display the rows.
    If no periodicity is provided then all the habits' data will be displayed
    else specified periodicity habits data will be displayed only.

    :param periodicity: Specific Periodicity to display data of (e.g, daily, weekly, or monthly), leaving empty will
    display all the habits' data (default None)
    """
    db = connect_database()
    if periodicity is not None:
        data = data_of_custom_periodicity_habits(db, periodicity)
    else:
        data = data_of_all_habits(db)
    if len(data) > 0:
        # Uses string formatting to set columns and rows for the table
        print("\n{:<10} {:<15} {:<10} {:<15}".format("Name", "Periodicity", "Category", "Date/Time"))
        print("-------------------------------------------------------")
        for row in data:
            print("{:<10} {:<15} {:<10} {:<15}".format(
                row[0].capitalize(),  # Name
                row[1].capitalize(),  # Periodicity
                row[2].capitalize(),  # Streak
                row[3].capitalize()))  # Completion TIme
        print("-------------------------------------------------------\n")

    else:
        print("\nNo habit found for the specified periodicity!\n")


# Table to show habit's streak along with other columns
def show_habit_streak_data(habit=None):
    """
    Shows all or specific habit streak data in a readable tabular format.

    The table is formatted using string formatting technique and consists of the following columns:
    Name, Periodicity, Completion Time and Current Streak -OR- Longest Streak.
    The habit data from database is retrieved and looped throughout to display the rows.
    If no habit name is provided then all the habits' data and their 'current streak' will be displayed
    else specified habit name data will be displayed along with its 'longest streak'.

    :param habit: Name of the habit to display data of, leaving empty will display every habits' data (default None)
    """

    db = connect_database()
    if habit is None:
        data = data_of_all_habits(db)
    else:
        data = data_of_single_habit(db, habit)
    if len(data) > 0:
        # Uses string formatting to set columns and rows for the table
        print("\n{:<10} {:^15} {:>10} {:>10}".format("Name |", "Periodicity |", "Completion Time |",
                                                     "Current Streak" if habit is None else "Longest Streak"))
        print(f"{'_' * 70}")  # Print dashes - 70 times to pretty format the table
        for row in data:
            period = " Day(s)" if row[1] == "daily" else (" Week(s)" if row[1] == "weekly" else " Month(s)")
            print("{:<10} {:^15} {:>10} {:^15}".format(
                row[0].capitalize(),  # Name
                row[1].capitalize(),  # Periodicity
                row[5] if row[5] is not None else "--/--/-- --:--",  # Completion Time
                str(row[4]) + period if habit is None else str(longest_habit_streak(db, habit)) + period))  # Current or Longest Streak
            print(f"{'_' * 70}\n")
    else:
        print("\nNo Habit Found; Please Add a Habit First!\n")


# Displays habits log
def show_habit_logged_data(name_of_habit):
    """
        Shows the log of specified habit.

        The custom table like format consists of "Habit Name", "Completed", "Streak" and "Logged at" columns.
        The habit data from database is retrieved and looped throughout to display it.

        :param name_of_habit: Name of the habit to display log of
        """
    db = connect_database()
    data = habit_log(db, name_of_habit)
    print(f"\n{'-' * 75}")  # Print dashes - 75 times to pretty format the table
    if len(data) > 0:
        for row in data:
            print(f"Habit: {row[0].capitalize()} | "
                  f"Completed : {'True' if row[1] == 1 else 'False'} | "
                  f"Streak: {row[2]} | Logged at: {row[3]}")
    else:
        print("No record found!")
    print(f"{'-' * 75}\n")
