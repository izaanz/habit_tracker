import db
from datetime import datetime


class Habit:
    """
        Habit class for interacting with different habits
    """
    def __init__(self, name: str = None, periodicity: str = None, category: str = None):
        """
        Parameters
        ----------
        name : str, optional
            The name of the habit (default is None)
        periodicity : str, optional
            The period of the habit (e.g, daily, weekly or monthly) (default is None)
        category : str, optional
            The category of the habit (default is None)
                """
        self.name = name
        self.periodicity = periodicity
        self.category = category
        self.db = db.connect_database()
        self.streak = 0
        self.current_time = datetime.now().strftime("%m/%d/%Y %H:%M")

    def add(self):
        """
        Adds habit information to the habit_tracker database and updates the log.
        """
        if db.habit_exists(self.db, self.name) is False:
            db.add_habit(self.db, self.name, self.periodicity, self.category, self.current_time, self.streak)
            db.update_log(self.db, self.name, False, 0, self.current_time)
            print(f"\nYour request to add '{self.name.capitalize()}' as '{self.periodicity.capitalize()}' "
                  f"Habit in '{self.category.capitalize()}' has been completed.\n")
        else:
            print("\nHabit already exists, please choose another habit.\n")

    def remove(self):
        """
        Removes the habit from the habit_tracker database.
        """
        db.remove_habit(self.db, self.name)
        print(f"\nDeleted '{self.name.capitalize()}' from database successfully.\n")

    def delete_category(self):
        """
        Deletes the category and all the assigned habit to that category from the habit_tracker database.
        """
        db.delete_category(self.db, self.category)
        print(f"\nSuccessfully deleted the category '{self.category.capitalize()}'.\n")

    def change_periodicity(self):
        """
        Changes the habit periodicity and updates the log.
        """
        db.update_periodicity(self.db, self.name, self.periodicity)
        db.update_log(self.db, self.name, False, 0, self.current_time)
        print(f"\nChanged Periodicity of the Habit '{self.name.capitalize()}' to '{self.periodicity.capitalize()}'\n")

    def increment_streak(self):
        """
        Gets the current habit streak from database and increments it by 1.
        """
        self.streak = db.get_streak_count(self.db, self.name)
        self.streak += 1

    def reset_streak(self):
        """
        Resets the habit streak to 1, also updates the log and the database.
        """
        self.streak = 1
        db.update_habit_streak(self.db, self.name, self.streak, self.current_time)
        db.update_log(self.db, self.name, False, db.get_streak_count(self.db, self.name), self.current_time)
        print("\nOops! Looks like you missed your streak. Your streak has been reset.")
        print(f"Your new streak for Habit '{self.name.capitalize()}' is now {self.streak} because you completed it.\n")

    def update_streak(self):
        """
        Calls increment_streak() and updates the habit streak and the log.
        """
        self.increment_streak()
        db.update_habit_streak(self.db, self.name, self.streak, self.current_time)
        db.update_log(self.db, self.name, True, db.get_streak_count(self.db, self.name), self.current_time)
        print(f"\nGreat! Your new streak for habit '{self.name.capitalize()}' is {self.streak}\n")

    def mark_as_completed(self):
        """
        Marks the habit as completed.

        This function checks the periodicity of the habit and calls the relevant method to
        verify whether the streak should be incremented or not depending on the day/week/month of the habit.
        """
        # Daily Streak Tracker & Assignment
        if db.fetch_habit_periodicity(self.db, self.name) == "daily":
            if self.daily_habit_streak_verification() == 0:
                print("\nYou have already completed this habit today, please try again tomorrow.\n")
            elif self.daily_habit_streak_verification() == 1:
                self.update_streak()
            else:
                self.reset_streak()

        # Weekly Streak Tracker & Assignment
        elif db.fetch_habit_periodicity(self.db, self.name) == "weekly":
            if self.weekly_habit_streak_verification() == 1:
                print("\nYou have already completed the habit this week, please try again next week.\n")
            elif self.weekly_habit_streak_verification() == 2:
                self.update_streak()
            else:
                self.reset_streak()

        # Monthly Streak Tracker & Assignment
        elif db.fetch_habit_periodicity(self.db, self.name) == "monthly":
            if self.monthly_habit_streak_verification() == 0:
                print("\nYou have already completed the habit this month, please try again next month.\n")
            elif self.monthly_habit_streak_verification() == 1:
                self.update_streak()
            else:
                self.reset_streak()

    def daily_habit_streak_verification(self):
        """
        Return the number of day(s) passed since the last habit completion.
        :return date.days: Number of day(s) since last completion of habit
        """
        last_visit = db.get_habit_completion_time(self.db, self.name)
        previous_streak = db.get_streak_count(self.db, self.name)
        if previous_streak == 0 or last_visit is None:
            return 1
        else:
            today = self.current_time
            date = datetime.strptime(today[:10], "%m/%d/%Y") - datetime.strptime(last_visit[:10], "%m/%d/%Y")
            return date.days

    def weekly_habit_streak_verification(self):
        """
        Return the number of week(s) passed since the last habit completion.
        :return week: Number of week(s) since last completion of habit
        """
        last_streak = db.get_habit_completion_time(self.db, self.name)
        previous_streak = db.get_streak_count(self.db, self.name)
        if (previous_streak == 0) or (last_streak is None):
            return 2
        else:
            today = self.current_time
            delt = datetime.strptime(today[:10], "%m/%d/%Y") - datetime.strptime(last_streak[:10], "%m/%d/%Y")
            week = 3 if delt.days > 14 else (2 if delt.days > 7 else 1)
            return week

    def monthly_habit_streak_verification(self):
        """
        Return the number of month(s) passed since the last habit completion.
        :return months: Number of month(s) since last completion of habit
        """
        last_visit = db.get_habit_completion_time(self.db, self.name)
        previous_streak = db.get_streak_count(self.db, self.name)
        if (previous_streak == 0) or (last_visit is None):
            return 1
        else:
            current_month = self.current_time
            month = int(current_month[:2]) - int(last_visit[:2])
            print(month)
            return month
