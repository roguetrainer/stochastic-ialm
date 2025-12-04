import numpy as np

class iALM_Simulator:
    """
    Implements the stochastic processes described in Section 3.1 of the paper.
    """
    def __init__(self, dt=1/12):
        self.dt = dt

    def simulate_gbm(self, S0, mu, sigma, n_steps, n_scenarios):
        """
        Simulates Geometric Brownian Motion (GBM) for assets like Equities.
        Based on discrete time process equation (3).
        """
        mu_prime = mu - 0.5 * sigma**2
        dW = np.random.normal(0, np.sqrt(self.dt), (n_steps, n_scenarios))
        
        log_returns = mu_prime * self.dt + sigma * dW
        log_price = np.cumsum(log_returns, axis=0)
        
        # S_t = S_0 * exp(log_price)
        prices = S0 * np.exp(np.vstack([np.zeros((1, n_scenarios)), log_price]))
        
        # Return prices starting from t=1 (removing t=0 S0 row for alignment)
        return prices[1:]

    def simulate_gou(self, R0, alpha, beta, sigma, n_steps, n_scenarios):
        """
        Simulates Geometric Ornstein-Uhlenbeck (GOU) for rates/inflation.
        Uses the log transformation r_t = log(R_t) which is an OU process.
        Based on discrete modelling equation (8).
        """
        # r_0 = log(R_0)
        r_current = np.full(n_scenarios, np.log(R0))
        r_paths = []
        
        # Eq (6) logic
        alpha_prime = alpha - 0.5 * sigma**2
        
        # Pre-compute constants for Eq (8)
        decay = np.exp(-beta * self.dt)
        mean_rev_term = (alpha_prime / beta) * (1 - decay)
        noise_scale = sigma * np.sqrt(self.dt)
        
        for _ in range(n_steps):
            # Epsilon term: N(0, sigma^2)
            epsilon = np.random.normal(0, noise_scale, n_scenarios)
            
            # Eq (8): Discrete update
            r_next = (r_current * decay) + mean_rev_term + epsilon
            
            r_paths.append(r_next)
            r_current = r_next
            
        # Convert back from log space: R_t = exp(r_t)
        return np.exp(np.array(r_paths))