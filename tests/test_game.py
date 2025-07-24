import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from game import determine_winner

class TestRockPaperScissors(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(determine_winner('rock', 'rock'), "tie")
        self.assertEqual(determine_winner('paper', 'paper'), "tie")
        self.assertEqual(determine_winner('scissors', 'scissors'), "tie")

    def test_win(self):
        self.assertEqual(determine_winner('rock', 'scissors'), "win")
        self.assertEqual(determine_winner('paper', 'rock'), "win")
        self.assertEqual(determine_winner('scissors', 'paper'), "win")

    def test_lose(self):
        self.assertEqual(determine_winner('rock', 'paper'), "lose")
        self.assertEqual(determine_winner('paper', 'scissors'), "lose")
        self.assertEqual(determine_winner('scissors', 'rock'), "lose")

    # Tests que fallarán a propósito
    def test_fail_1(self):
        self.assertEqual(determine_winner('rock', 'scissors'), "lose")  # Falla

    def test_fail_2(self):
        self.assertEqual(determine_winner('paper', 'scissors'), "win")  # Falla

if __name__ == "__main__":
    unittest.main()
