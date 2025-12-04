import numpy as np

class WealthProjector:
    """
    Simulates the evolution of household net financial wealth over time.
    Integrates the asset returns (Stage 1) with liability outflows (Stage 2).
    Reference: Section 4.3 'Reality Check'.
    """
    def __init__(self, asset_simulator, liability_simulator, portfolio_simulator):
        """
        asset_simulator: Instance of iALM_Simulator (for environment/inflation)
        liability_simulator: Instance of LiabilitySimulator (for outflows)
        portfolio_simulator: Instance/Function generating portfolio returns
        """
        self.asset_sim = asset_simulator
        self.liab_sim = liability_simulator
        self.portfolio_sim = portfolio_simulator
        
    def run_simulation(self, initial_wealth, income_streams, n_steps, n_scenarios):
        """
        Runs the wealth evolution loop for N scenarios.
        
        initial_wealth: Starting liquid assets
        income_streams: List of income dicts or a LiabilitySimulator instance for positive flows
        """
        # Initialize wealth grid: (Steps + 1, Scenarios)
        wealth_paths = np.zeros((n_steps + 1, n_scenarios))
        wealth_paths[0] = initial_wealth
        
        # Pre-calculate market drivers if not already done
        # For this module, we assume portfolio_returns are pre-calculated or passed in.
        # This function expects `portfolio_simulator` to return (steps, scenarios) array of returns.
        portfolio_returns = self.portfolio_sim
        
        # Pre-calculate total liabilities (L_t)
        total_liabilities = self.liab_sim.total_liabilities
        
        # Pre-calculate Income (treated as negative liability or separate flow)
        total_income = income_streams.total_liabilities if hasattr(income_streams, 'total_liabilities') else np.zeros((n_steps, n_scenarios))

        for t in range(n_steps):
            # 1. Previous Wealth
            w_prev = wealth_paths[t]
            
            # 2. Portfolio Growth: W * (1 + r)
            r_t = portfolio_returns[t]
            w_invested = w_prev * (1 + r_t)
            
            # 3. Net Cashflow: Income - Liabilities
            net_cashflow = total_income[t] - total_liabilities[t]
            
            # 4. Update
            wealth_paths[t+1] = w_invested + net_cashflow
            
        return wealth_paths

    def calculate_solvency(self, wealth_paths):
        """
        Calculates the probability of solvency (Wealth > 0) at the end of the horizon.
        """
        final_wealth = wealth_paths[-1]
        n_scenarios = len(final_wealth)
        solvent_scenarios = np.sum(final_wealth > 0)
        return solvent_scenarios / n_scenarios