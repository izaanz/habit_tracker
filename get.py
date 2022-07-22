"""
The get module: Serves to improve function re-usability by utilizing questionary library.

The module essentially manages different types of input from the user like fetching the list
of habits stored in the database, with the help of db module, and then shows them to the user.
Asks for user confirmation if they want to delete something and other different yet similar functions.
Hence, increasing the re-usability of the code.
"""

import questionary as qt
from db import connect_database, fetch_categories, fetch_habits_as_choices


def habit_name():
    """
    Prompts the user to enter the name of the habit.

    Habit name is restricted to alphabets only. No whitespaces or special
    characters are allowed.

    :return: Returns the name of the habit provided by the user
    """
    return qt.text("Please Enter the Name of Your Habit:",
                   validate=lambda name: True if name.isalpha() and len(name) > 1
                   else "Please enter a valid name").ask().lower()


def habit_periodicity():
    """
    Displays the periodicity choices for the user to select from.

    :return: Returns the selected habit periodicity
    """
    return qt.select("Please Select Habit Periodicity",
                     choices=["Daily", "Weekly", "Monthly"]).ask().lower()


def habit_category():
    """
    Prompts the user to enter the name of the category.

    Category name is restricted to alphabets only. No whitespaces or special
    characters are allowed.

    :return: Returns the name of the category provided by the user
    """
    return qt.text("Please Enter the Name of Your Category:",
                   validate=lambda category: True if category.isalpha() and len(category) > 1
                   else "Please enter a valid category").ask().lower()


def defined_categories():
    """
    Displays the categories available in the database for the user to choose from.

    :return: Returns the selected category from the list of choices
    :raises ValueError: If no categories are available in the database then raises a ValueError
    """
    db = connect_database()
    arr = fetch_categories(db)
    if len(arr) > 0:
        return qt.select("Please Select a Category",
                         choices=sorted(arr)).ask().lower()
    else:
        raise ValueError("No categories found in Database; Please define a category using 'Add habit' function")


def category_delete_confirmation():
    """
    Prompts the user to confirm whether they like to delete the category or not.

    :return: Return True if yes else returns False
    """
    return qt.confirm("Deleting the category will also delete all the assigned habits, "
                      "would you still like to proceed?").ask()


def periodicity_change_confirmed():
    """
    Prompts the user to confirm whether they like to change the periodicity or not.

    :return: Return True if yes else returns False
    """
    return qt.confirm("Changing periodicity of the habit will reset streak, would you like to continue?").ask()


def habits_from_db():
    """
    Displays the habit names available in the database for the user to choose from.

    :return: Returns the selected habit from the list of choices
    :raises ValueError: If no habits are available in the database then raises a ValueError
    """
    db = connect_database()
    list_of_habits = fetch_habits_as_choices(db)
    if list_of_habits is not None:
        return qt.select("Please Select a Habit",
                         choices=sorted(list_of_habits)).ask().lower()
    else:
        raise ValueError("No habit in database; Add a habit first to use this function")


def habit_delete_confirmation(habit_name_to_delete):
    """
    Prompts the user to confirm whether they like to delete the habit or not.

    :return: Return True if yes else returns False
    """
    return qt.confirm(f"Would you like to delete '{habit_name_to_delete}' habit from database?").ask()


def show_period_choices():
    """
    Prompts the user to select from the list of provided period display choices.

    :return: Return the chosen action as str
    """
    choice = qt.select("Would you like to view all habits or sort habit by periodicity?",
                       choices=[
                           "View All Habits",
                           "View Daily Habits",
                           "View Weekly Habits",
                           "View Monthly Habits",
                           "Back to Main Menu"
                       ]).ask()
    return choice


def analytics_choices():
    """
    Prompts the user to select from the list of provided analytical choices.

    :return: Return the chosen action as str
    """
    choice = qt.select("Please choose an option:",
                       choices=[
                           "View All Habit's Streaks",
                           "View Longest Streak of Specific Habit",
                           "View Streak Log of Specific Habit",
                           "Back to Main Menu"
                       ]).ask()
    return choice
