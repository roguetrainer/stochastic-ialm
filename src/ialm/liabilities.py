import numpy as np

class LiabilitySimulator:
    """
    Implements the Liability Simulation described in Section 3.1.20 - 3.1.21.
    Calculates forward cash outflows based on stochastic inflation paths.
    """
    def __init__(self, inflation_paths):
        self.inflation_paths = inflation_paths
        self.n_steps, self.n_scenarios = inflation_paths.shape
        self.total_liabilities = np.zeros((self.n_steps, self.n_scenarios))

    def add_liability(self, name, initial_value, start_step, end_step, 
                      is_indexed=True, r_add=0.0):
        """
        Adds a liability stream.
        Logic based on Eq (17) for indexed growth and Eq (291) for fixed flows.
        
        r_add: Additional deterministic growth (e.g. school fees > CPI).
        """
        liability_flow = np.zeros((self.n_steps, self.n_scenarios))
        current_value = np.full(self.n_scenarios, initial_value)
        
        for t in range(self.n_steps):
            if start_step <= t < end_step:
                if is_indexed:
                    # Lagged inflation: Use t-1 to determine growth for t
                    # Inflation path is R_t (e.g. 1.03), so r_infl is (Path - 1.0)
                    if t > 0:
                        r_infl = self.inflation_paths[t-1] - 1.0 
                    else:
                        r_infl = np.zeros(self.n_scenarios)
                        
                    # Eq (17): l_t = l_{t-1}(1 + r_infl + r_add)
                    growth_factor = 1.0 + r_infl + r_add
                    current_value = current_value * growth_factor
                    liability_flow[t] = current_value
                else:
                    # Fixed liability (Eq 291)
                    liability_flow[t] = initial_value

        # Eq (305): Aggregate into total L_t
        self.total_liabilities += liability_flow
        return liability_flow