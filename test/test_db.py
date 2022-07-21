from db import add_habit, connect_database, fetch_habits_as_choices, habit_exists, remove_habit, \
    fetch_categories, update_periodicity, fetch_habit_periodicity, update_habit_streak, get_streak_count


class TestDatabase:
    """
    TestDatabase class contains method that tests the important functions of db module
    """

    def setup_method(self):
        self.db = connect_database("test_db.db")
        # Total 6 habits and 4 categories (3 career = only 1 category, 1 atmosphere, 1 growth and 1 games)
        add_habit(self.db, "coding", "daily", "career", "01/01/2022 13:00", 0)
        add_habit(self.db, "study", "daily", "career", "01/02/2022 13:00", 0)
        add_habit(self.db, "gym", "daily", "career", "01/02/2022 13:00", 0)
        add_habit(self.db, "cleaning", "weekly", "atmosphere", "02/01/2022 13:00", 0)
        add_habit(self.db, "reflection", "monthly", "growth", "02/01/2022 13:00", 0)
        add_habit(self.db, "gaming", "daily", "games", "01/01/2022 13:00", 0)

    def test_fetch_habits_as_choices(self):
        assert len(fetch_habits_as_choices(self.db)) == 6

    def test_fetch_categories(self):
        assert len(fetch_categories(self.db)) == 4

    def test_remove_habit(self):
        remove_habit(self.db, "gaming")
        assert habit_exists(self.db, "gaming") is False
        assert len(fetch_habits_as_choices(self.db)) == 5

    def test_update_periodicity(self):
        update_periodicity(self.db, "reflection", "weekly")
        assert fetch_habit_periodicity(self.db, "reflection") == "weekly"

    def test_update_habit_streak(self):
        update_habit_streak(self.db, "coding", 1, "01/02/2022 13:00")
        assert get_streak_count(self.db, "coding") == 1

    def teardown_method(self):
        self.db.close()
        import os
        os.remove("test_db.db")
