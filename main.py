import questionary as qt
import get
from habit import Habit
import analytics

# Greeting message
print("""
*** Welcome to the Habit Tracker ***
""")


#  CLI Interface
def menu():
    """
    CLI Interface utilized with questionary library to
    pretty display the menu of the habit tracker for the user.
    """
    # Shows 6 choices for the user to choose from
    choice = qt.select(
        "What do you want to do?",
        choices=[
            "Add/Remove Habit OR Category",
            "Modify Habit's Periodicity",
            "Mark Habit as Completed",
            "Show Habits (All or Sort by Periodicity)",
            "Analytics",
            "Exit"
        ]).ask()

    if choice == "Add/Remove Habit OR Category":
        # 4 sub-choices
        second_choice = qt.select(
            "Would you like to Add, Remove Habit or Category?",
            choices=[
                "Add Habit",
                "Remove Habit",
                "Delete Category",
                "Back to Main Menu"
            ]).ask()

        if second_choice == "Add Habit":
            habit_name = get.habit_name()
            habit_periodicity = get.habit_periodicity()
            habit_category = get.habit_category()
            habit = Habit(habit_name, habit_periodicity, habit_category)
            habit.add()

        elif second_choice == "Remove Habit":
            try:
                habit_name = get.habits_from_db()
            except ValueError:  # ValueError is raised when there are no habits in the database
                print("\nOops! No habit found in database: Please add a habit first.\n")
            else:
                habit = Habit(habit_name)
                if get.habit_delete_confirmation(habit_name):
                    habit.remove()
                else:
                    print("\nNo problem! We all get confused sometimes :)\n")

        elif second_choice == "Delete Category":
            try:
                habit_category = get.defined_categories()
            except ValueError:  # ValueError is raised when there are no categories in the database
                print("\nNo category found! Please add a habit & category using the 'Add habit' function.\n")
            else:
                if get.category_delete_confirmation():
                    habit = Habit(category=habit_category)
                    habit.delete_category()
                else:
                    print("\nThanks for confirming!\n")

        elif second_choice == "Back to Main Menu":
            menu()

    elif choice == "Modify Habit's Periodicity":
        try:
            habit_name = get.habits_from_db()
        except ValueError:  # ValueError is raised when there are no habits in the database
            print("\nDatabase empty; Please add a habit first.\n")
        else:
            new_periodicity = get.habit_periodicity()
            if get.periodicity_change_confirmed():
                habit = Habit(habit_name, new_periodicity)
                habit.change_periodicity()
            else:
                print(f"\nPeriodicity of {habit_name} remains unchanged! Thanks for confirming.\n")

    elif choice == "Mark Habit as Completed":
        try:
            habit_name = get.habits_from_db()
        except ValueError:  # ValueError is raised when there are no habits in the database
            print("\nNo habit defined; please add a habit first to complete it!\n")
        else:
            habit = Habit(habit_name)
            habit.mark_as_completed()

    elif choice == "Show Habits (All or Sort by Periodicity)":
        second_choice = get.show_period_choices()  # Fetches choices list from Get module
        if second_choice == "View All Habits":
            analytics.show_habits_data()  # Analytics module contains the tabular formatted data visualizer
        elif second_choice == "View Daily Habits":
            analytics.show_habits_data("daily")
        elif second_choice == "View Weekly Habits":
            analytics.show_habits_data("weekly")
        elif second_choice == "View Monthly Habits":
            analytics.show_habits_data("monthly")
        elif second_choice == "Back to Main Menu":
            menu()

    elif choice == "Analytics":
        second_choice = get.analytics_choices()
        if second_choice == "View All Habit's Streaks":
            analytics.show_habit_streak_data()
        elif second_choice == "View Longest Streak of Specific Habit":
            try:
                habit_name = get.habits_from_db()
            except ValueError:  # ValueError is raised when there are no habits in the database
                print("\nNo habit data found in the database; Please add a habit first\n")
            else:
                analytics.show_habit_streak_data(habit_name)
        elif second_choice == "View Streak Log of Specific Habit":
            try:
                habit_name = get.habits_from_db()
            except ValueError:  # ValueError is raised when there are no habit's log in the database
                print("\nNo habit log found; Please add a habit first\n")
            else:
                analytics.show_habit_logged_data(habit_name)
        elif second_choice == "Back to Main Menu":
            menu()

    elif choice == "Exit":
        print("\nGoodbye! Remember to maintain your habit streaks!")  # Goodbye message
        exit()  # exit() completely exits the program


if __name__ == "__main__":
    while True:
        menu()
