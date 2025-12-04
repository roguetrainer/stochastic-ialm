# stochastic-ialm

**Python implementation of iALM: Dynamic Stochastic Programming for modeling household wealth, liability flows, and sustainable spending.**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

---
![iALM](./img/iALM.jpg)
---

See [docs/overview.md](./docs/overview.md)

## Overview

**stochastic-ialm** is an open-source implementation of the **Individual Asset Liability Management (iALM)** meta-model described in the paper *"Asset Liability Management for Individual Households"* (Dempster & Medova, 2010).

Unlike traditional financial planning tools that use static returns (e.g., "7% average growth"), this model uses **Dynamic Stochastic Programming (DSP)**. It simulates thousands of possible market and life scenarios to determine if a household's spending goals are sustainable.



### Core Philosophy
1.  **Wealth ≠ Net Worth:** Wealth is defined as **sustainable spending** over a lifetime.
2.  **Risk ≠ Volatility:** Risk is the probability of failing to meet essential liabilities (e.g., mortgage, education).
3.  **Behavioral Utility:** The model uses **Prospect Theory** to prioritize goals into Minimum, Acceptable, and Desirable levels.

---

## Key Features

* **Stochastic Engines (`src/ialm/engines.py`)**:
    * **Equities:** Simulated via Geometric Brownian Motion (GBM).
    * **Inflation/Rates:** Simulated via Geometric Ornstein-Uhlenbeck (GOU) processes to capture mean reversion.
* **Liability Modeling (`src/ialm/liabilities.py`)**:
    * Distinguishes between **Fixed Liabilities** (mortgages) and **Indexed Liabilities** (living costs, school fees) that react to stochastic inflation shocks.
* **Behavioral Utility (`src/ialm/utility.py`)**:
    * Implements piece-wise linear utility functions to model goal priorities.
* **Reality Check (`src/ialm/analysis.py`)**:
    * Projects the "Wealth Cloud" to visualize the full distribution of future outcomes and calculate solvency probabilities.

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/stochastic-ialm.git](https://github.com/your-username/stochastic-ialm.git)
    cd stochastic-ialm
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Quick Start

The best way to understand the model is to run the Jupyter Notebooks in order:

1.  **`notebooks/01_Asset_Simulator.ipynb`**
    * *Visualizes the stochastic drivers (Equity paths and Inflation cycles).*
2.  **`notebooks/02_Liability_Projections.ipynb`**
    * *Demonstrates how high-inflation scenarios impact future liabilities like school fees.*
3.  **`notebooks/03_Reality_Check_Example.ipynb`**
    * *Runs the full "Pimlott Family" case study to test solvency probability.*

---

## Project Structure

```text
stochastic-ialm/
├── data/
│   └── profiles/           # JSON/YAML household profiles
├── docs/
│   └── overview.md         # Detailed theory and equation mapping
├── notebooks/              # Interactive examples
├── src/
│   └── ialm/
│       ├── engines.py      # GBM/GOU mathematical engines
│       ├── liabilities.py  # Cash outflow logic
│       ├── utility.py      # Behavioral finance logic
│       └── analysis.py     # Solvency & Wealth calculation
└── tests/                  # Unit tests
```

## Theory & References

For a deep dive into the equations used (GBM, GOU, and Prospect Theory utility), please see [docs/overview.md](docs/overview.md).

**Reference Paper:**
Dempster, M. A. H., & Medova, E. A. (2010). *Asset Liability Management for Individual Households*.

---

## License

This project is licensed under the MIT License.