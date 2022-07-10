import unittest
from main import player_salary


class Testme(unittest.TestCase):
    def test_player_salary(self):
        player_id = 'curryst01'

    @patch('builtins.input', return_value=player_id)
    def test_player_salary(self, mock_input):
        result = player_salary()
        self.assertEqual(result, 'Stephen Curry made $212078086 in their career.')

        
if __name__ == '__main__':
    unittest.main()
