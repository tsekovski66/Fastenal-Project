Fastenal (FAST): Integrated Financial Valuation & Quantitative Risk Engine
Author: Martin Tsekovski

Tools Used: Microsoft Excel, Python (NumPy, Seaborn, Matplotlib)

Disciplines: Investment Banking (DCF), Corporate Finance (FP&A), Quantitative Risk, Credit Stress Testing

Executive Summary
This repository contains a fully integrated, multi-disciplinary financial model for Fastenal Company (NASDAQ: FAST). It moves beyond deterministic, top-down forecasting by bridging bottom-up unit economics with stochastic Monte Carlo simulations to generate risk-adjusted intrinsic equity valuations.

The project evaluates management’s physical footprint strategy (shifting from public branches to Onsite deployments) and stress-tests the balance sheet against macroeconomic contraction, working capital liquidity drains, and debt covenant thresholds.

Core Modules
1. Corporate Finance (FP&A) & Unit Economics Engine
Bottom-Up Revenue Build: Forecasts top-line revenue not through flat percentage growth, but by modeling the physical reality of the business.

Strategic Transition: Disaggregates consolidated sales into legacy branch closures (-50/year) and new Onsite installations (+300/year), factoring in historical throughput and 3.0% annual pricing power.

2. Fundamental Valuation (3-Statement DCF)
Integrated Financials: A fully linked 3-statement architecture forecasting Unlevered Free Cash Flow (UFCF) over a 5-year jump-off period.

Valuation Bridge: Bridges Enterprise Value to Implied Equity Value using a WACC discount rate and Terminal EBITDA Multiple, supported by multi-variable sensitivity data tables.

3. Quantitative Finance & Stochastic Pricing (Python)
Monte Carlo Simulation: A 10,000-iteration stochastic pricing engine scripted in Python and NumPy.

Normal Probability Distributions: Randomizes physical operational bottlenecks (Onsite deployment variance) and macroeconomic inflation (pricing power) rather than generic revenue percentages.

Risk-Adjusted Outputs: Compresses extreme tail-risk scenarios to generate a highly accurate, risk-adjusted 80% confidence interval for intrinsic share price.

4. Credit Risk & Solvency Stress Testing
Liquidity Shocks: An interactive Excel override module modeling the cash-drain impact of Days Sales/Inventory Outstanding (DSO/DIO) spikes during a severe economic downturn.

Covenant Headroom: Evaluates operating margin de-leveraging to validate Interest Coverage safety buffers.

Heatmap Matrix: A multi-variable scenario-analysis matrix scripted in Python (Seaborn), testing 100 simultaneous revenue and margin contraction scenarios.

Repository Navigation
DCF_project.xlsx: The master Excel workbook containing the FP&A build, DCF, and Stress-Test toggles.

dcf_monte_carlo_sim.py: The 10,000-iteration Python simulation modeling normal distributions of unit-level deployments.

stress_test_dcf.py: The Python script generating the Interest Coverage risk matrix.

/visuals/: Directory containing output charts, confidence intervals, and the Seaborn risk matrix.
