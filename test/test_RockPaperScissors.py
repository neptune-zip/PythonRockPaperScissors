import unittest
from src.Engine.RockPaperScissors import RockPaperScissors

class RockPaperScissorTest(unittest.TestCase):

    rock = RockPaperScissors()

    def test_determine_winner(self):
        self.assertEqual("Draw", self.rock.determine_winner(0,0))


    def test_get_user_choice_request(self):
        self.assertEqual()
