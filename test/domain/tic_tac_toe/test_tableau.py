import unittest

from test.domain.tic_tac_toe.test_tic_tac_toe import Tableau


class MyTableauTest(unittest.TestCase):
    def test_initial_tableau_position(self):
        tableau = Tableau([[None, None, None], [None, None, "X"], [None, None, None]])
        self.assertEqual(None, tableau[0, 0])
        self.assertEqual("X", tableau[1, 2])

    def test_initial_tableau_position_default(self):
        tableau = Tableau()
        self.assertEqual([[None, None, None], [None, None, None], [None, None, None]], tableau)
        self.assertEqual(None, tableau[1, 2])

    def test_can_set_a_value(self):
        tableau = Tableau()
        tableau[1, 2] = "X"
        self.assertEqual("X", tableau[1, 2])

    def test_if_tableau_is_full(self):
        full_tableau = Tableau([["X", "Y", "X"], ["Y", "X", "Y"], ["X", "Y", "X"]])
        self.assertTrue(full_tableau.is_full())

    def test_can_detect_an_empty_tableau(self):
        empty_tableau = Tableau([[None, None, None], [None, None, None], [None, None, None]])
        self.assertFalse(empty_tableau.is_full())

    def test_if_there_is_a_winner_when_tableau_is_full(self):
        full_tableau = Tableau([["X", "Y", "X"], ["X", "X", "Y"], ["Y", "X", "Y"]])
        self.assertIsNone(full_tableau.who_is_the_winner())

    def test_if_there_is_a_winner_when_tableau_is_not_full(self):
        full_tableau = Tableau([["X", "Y", "X"], ["X", "X", "Y"], ["Y", None, "Y"]])
        self.assertIsNone(full_tableau.who_is_the_winner())