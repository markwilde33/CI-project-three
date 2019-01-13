import unittest
import app


class TestRiddleGame(unittest.TestCase):
    """
    Collection of riddle tests
    """

    def test_get_users(self):
        """
        Test to ensure we can retrieve the users list from users.json
        """
        users = app.get_users()
        self.assertEqual(len(users), 1)

    def test_get_leaders(self):
        """
        Test to ensure we can retrieve the leaders list from leaderboard.json
        """
        leaders = app.get_leaders()
        self.assertEqual(len(leaders), 1)
