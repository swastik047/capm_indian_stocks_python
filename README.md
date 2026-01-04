# capm_indian_stocks_python
# CAPM Analysis for Indian Stocks using Python

## 📌 Overview
This project implements the **Capital Asset Pricing Model (CAPM)** using Python to analyze **Indian equities listed on the NSE**, with **NIFTY 50** as the market benchmark.  
It estimates **systematic risk (Beta)**, evaluates **model fit (R²)** through regression analysis, and calculates **expected returns**, combining financial theory with real-world market data.

## 🎯 Objectives
Apply the **CAPM framework** to Indian stocks
Estimate **Beta** using linear regression
Measure **R-squared** to assess explanatory power
Calculate **expected returns** using a given risk-free rate
Visualise **risk–return relationships** through regression plots
Bridge **financial theory and data-driven analysis**

## 📊 Methodology
1. Fetch historical price data for selected stocks and NIFTY 50  
2. Compute **daily returns**
3. Perform **linear regression** of stock returns against market returns
4. Estimate:
    **Beta (β)** – systematic risk
    **Alpha (α)** – excess return component
    **R²** – goodness of fit
5. Calculate **expected return** using the CAPM formula:

\[
E(R_i) = R_f + \beta_i (E(R_m) - R_f)
\]

6. Visualize results using scatter plots with regression lines

## 🧾 Data & Assumptions
- **Market Proxy:** NIFTY 50 Index (`^NSEI`)
- **Stock Universe:** NSE-listed equities (e.g., Reliance, TCS, HDFC Bank, Infosys)
- **Returns Frequency:** Daily
- **Risk-Free Rate:** User-defined (example: 4.5%)
- **Price Used:** Closing prices
- **Time Period:** Configurable by user

## Technologies & Libraries
- Python
- NumPy
- Pandas
- yFinance
- SciPy
- Statsmodels
- Matplotlib
- Seaborn
- Tabulate

## 📈 Outputs
  Regression summaries for each stock
  Estimated **Beta**, **R²**, and **Expected Return**
  Tabulated results for easy interpretation
  Scatter plots with fitted regression lines

