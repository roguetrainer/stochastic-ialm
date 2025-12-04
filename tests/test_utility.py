import unittest
from src.ialm.utility import GoalUtility

class TestUtility(unittest.TestCase):
    def setUp(self):
        # Weights: 10 (Critical), 5 (Important), 1 (Nice to have)
        self.util = GoalUtility(min_h=100, acc_s=200, des_g=300, weights=(10, 5, 1))

    def test_zone_1_critical(self):
        # Below min, high negative utility
        u = self.util.calculate_utility(50)
        # (50 - 100) * 10 = -500
        self.assertEqual(u, -500)

    def test_zone_2_acceptable(self):
        # Above min, below acceptable
        u = self.util.calculate_utility(150)
        # (150 - 100) * 10 = 500
        self.assertEqual(u, 500)

    def test_zone_4_surplus(self):
        # Above desirable
        u = self.util.calculate_utility(400)
        # Zone 2 full: (200-100)*10 = 1000
        # Zone 3 full: (300-200)*5  = 500
        # Zone 4 part: (400-300)*1  = 100
        # Total = 1600
        self.assertEqual(u, 1600)

if __name__ == '__main__':
    unittest.main()