# iALM: Philosophy & Methodology

## 1. The Core Philosophy
Traditional financial planning often asks, "How can I maximize my pot of money?" or uses static rules of thumb like "Equity Allocation = 100 - Age".

**Individual Asset Liability Management (iALM)** shifts the objective entirely. It asserts two main principles:
1.  **Wealth is Sustainable Spending:** True wealth isn't the number in an account; it is the inflation-indexed real income that your assets can sustain over a lifetime.
2.  **Risk is Failure to Meet Goals:** Risk is not just portfolio volatility (standard deviation); it is the probability of falling short of essential liabilities or life goals.

### Behavioral Finance Integration
The model incorporates **Prospect Theory** (Kahneman & Tversky) to handle human behavior. Instead of a single "risk tolerance" number, the model uses a **Piece-Wise Linear Utility Function**.
* **Narrow Framing:** We assess risk regarding specific goals (e.g., "Can I pay the mortgage?").
* **Broad Framing:** We simultaneously maximize lifetime satisfaction from wealth.

## 2. The Simulation Engine: Dynamic Stochastic Programming (DSP)
Unlike static Monte Carlo simulations that often assume a fixed portfolio strategy, iALM uses **Dynamic Stochastic Programming**. This models the reality that households make *decisions* over time (rebalancing, changing spending) in response to market conditions.

### A. Asset Simulation (Stage 1)
We do not simply assume a "7% average return." We simulate distinct stochastic processes for different asset classes:
* **Equities (GBM):** Modeled using **Geometric Brownian Motion**. This captures the random walk of stock prices where volatility scales with time.
* **Inflation & Rates (GOU):** Modeled using the **Geometric Ornstein-Uhlenbeck** process. This captures "mean reversion"—the tendency of interest rates and inflation to be pulled back to a long-term central target (e.g., Central Bank targets).

### B. Liability Simulation (Stage 2)
Liabilities are not static. They react to the economic environment simulated in Stage 1.
* **Fixed Liabilities ($L^0$):** Mortgages or loans fixed in currency terms.
* **Indexed Liabilities ($L^1$):** Living expenses or school fees that grow with stochastic inflation ($r^{infl}$) plus a specific spread ($r^{add}$).

*If inflation spikes in a specific scenario, the "Indexed Liabilities" automatically increase, putting pressure on the household's solvency in that specific timeline.*

## 3. The Optimization Logic
The model seeks to maximize utility across three distinct zones of spending for every goal:

1.  **Minimum ($h$):** The "poverty line" or absolute essential payment (e.g., Mortgage). Failure here is catastrophic (high negative utility).
2.  **Acceptable ($s$):** The standard of living the household expects.
3.  **Desirable ($g$):** The "nice-to-haves" (e.g., Luxury travel).

The slope of the utility curve acts as the **priority**. Essential goals have a steep slope (high priority), ensuring the optimizer allocates capital there first before funding "Desirable" goals.

## 4. Code Implementation Map

| Concept | Paper Reference | Code Module | Description |
| :--- | :--- | :--- | :--- |
| **Asset Simulation** | Eq 3 (GBM), Eq 8 (GOU) | `src/ialm/engines.py` | Simulates market returns and inflation paths. |
| **Liability Indexing** | Eq 17, Eq 305 | `src/ialm/liabilities.py` | Calculates $L_t = L^0 + L^1$ considering inflation shocks. |
| **Goal Utility** | Section 3.2.3, Fig 4 | `src/ialm/utility.py` | Implements the Min/Acceptable/Desirable priority logic. |
| **Solvency Check** | Section 4.3 | `src/ialm/analysis.py` | The "Reality Check": projects Net Wealth evolution. |