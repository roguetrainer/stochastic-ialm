import unittest
import numpy as np
from src.ialm.engines import iALM_Simulator

class TestEngines(unittest.TestCase):
    def setUp(self):
        self.sim = iALM_Simulator(dt=1/12)

    def test_gbm_shape(self):
        prices = self.sim.simulate_gbm(S0=100, mu=0.05, sigma=0.1, n_steps=10, n_scenarios=5)
        self.assertEqual(prices.shape, (10, 5))
        self.assertTrue(np.all(prices > 0)) # Prices should be positive

    def test_gou_mean_reversion(self):
        # High starting value should revert downwards
        paths = self.sim.simulate_gou(R0=1.10, alpha=0.03, beta=2.0, sigma=0.001, n_steps=50, n_scenarios=100)
        final_mean = np.mean(paths[-1])
        # Should be closer to alpha (1.03 approx) than start (1.10)
        self.assertTrue(final_mean < 1.10)

if __name__ == '__main__':
    unittest.main()