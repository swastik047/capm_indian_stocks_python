# **CAPM Analysis for Indian Stocks Using Python**

This project applies the **Capital Asset Pricing Model (CAPM)** to analyze the risk and return characteristics of **Indian stocks listed on the NSE**, using the **NIFTY 50 Index (`^NSEI`) as the market benchmark**. The objective is to combine **financial theory with practical data analytics** by estimating each stock’s **systematic risk (Beta)**, measuring **model fit through R²**, and calculating **expected returns** based on a user-defined **risk-free rate**.

The methodology begins with fetching **historical closing price data** for selected NSE stocks and the NIFTY 50 over a **user-configurable time period**. From this data, **daily returns** are computed and used in a **linear regression model**, where stock returns are regressed against market returns. This allows the estimation of key CAPM metrics, including **Beta (β)**, **Alpha (α)**, and **R-squared (R²)**, which help evaluate both the stock’s sensitivity to market movements and the explanatory power of the model.

Using the CAPM equation, the project then calculates the **expected return** for each stock:

E(R_i)=R_f+\beta_i\left(E(R_m)-R_f\right)

The analysis is further supported by **scatter plots with fitted regression lines**, helping visualize the **risk–return relationship** in an intuitive way.

Final outputs include **regression summaries, Beta estimates, R² values, expected returns, formatted result tables, and visual regression plots**, making it a strong demonstration of both **financial modeling and data-driven analysis skills**.


