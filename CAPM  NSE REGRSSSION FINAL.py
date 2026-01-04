import numpy as np
import pandas as pd
import yfinance as yf
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
import statsmodels.api as sm

def capm(stocks, start_date, end_date, rf):
    # Create empty DataFrame to store stock prices
    data = pd.DataFrame()

    # Download data using yfinance
    for stock in stocks:
        ticker = yf.Ticker(stock)
        stock_data = ticker.history(start=start_date, end=end_date)
        data[stock] = stock_data['Close']  # Using Close price

    # ✅ FIXED LINE (no FutureWarning, finance-correct)
    returns = data.pct_change(fill_method=None).dropna()

    results = []

    # Set up figure for plots
    fig, axes = plt.subplots(
        nrows=len(stocks) - 1,
        ncols=1,
        figsize=(12, 4 * (len(stocks) - 1))
    )
    fig.tight_layout(pad=4.0)

    plot_index = 0
    benchmark = '^NSEI'  # Indian market benchmark

    for stock in stocks:
        if stock != benchmark:
            # Calculate benchmark return
            bench_ret = (np.prod(1 + returns[benchmark]) - 1)

            # Linear regression for beta
            beta, alpha, r_value, p_value, std_err = stats.linregress(
                returns[benchmark],
                returns[stock]
            )

            # CAPM expected return
            capm_return = (rf / 100) + beta * (bench_ret - rf / 100)

            results.append([stock, beta, r_value ** 2, capm_return * 100])

            # Statsmodels regression
            X = sm.add_constant(returns[benchmark])
            model = sm.OLS(returns[stock], X).fit()

            print(f"\n--- Regression Summary for {stock} vs {benchmark} ---")
            print(model.summary().tables[1])

            # Plot
            ax = axes[plot_index]
            sns.regplot(
                x=returns[benchmark],
                y=returns[stock],
                ax=ax,
                scatter_kws={'alpha': 0.3}
            )

            equation = f"y = {alpha:.4f} + {beta:.4f}x"
            r_squared = f"R² = {r_value ** 2:.4f}"

            ax.text(0.05, 0.95, equation, transform=ax.transAxes,
                    fontsize=12, verticalalignment='top')
            ax.text(0.05, 0.90, r_squared, transform=ax.transAxes,
                    fontsize=12, verticalalignment='top')

            ax.set_title(f"{stock} vs {benchmark}")
            ax.set_xlabel(f"{benchmark} Daily Returns")
            ax.set_ylabel(f"{stock} Daily Returns")

            plot_index += 1

    # Results table
    headers = ["Stock", "Beta", "R-squared", "Expected Return (%)"]
    print("\n--- CAPM Analysis Results ---")
    print(tabulate(results, headers=headers, floatfmt=".4f"))

    plt.show()


# Example usage
indian_stocks = [
    'RELIANCE.NS',
    'TCS.NS',
    'HDFCBANK.NS',
    'INFY.NS',
    'BHARTIARTL.NS',
    '^NSEI'
]

rf_rate = 4.5  # Risk-free rate (India)
capm(indian_stocks, '2025-01-01', '2025-12-31', rf_rate)
