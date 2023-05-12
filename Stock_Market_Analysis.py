import pandas as pd

# Read the CSV file
df = pd.read_csv('/config/workspace/Mrinalini_DA_Project /tradelog.csv')

# Total Trades
total_trades = len(df)

# Profitable Trades
profitable_trades = len(df[df['Exit Price'] > df['Entry Price']])

# Loss-Making Trades
loss_making_trades = len(df[df['Exit Price'] < df['Entry Price']])

# Win Rate
win_rate = profitable_trades / total_trades

# Average Profit per trade
average_profit = (df['Exit Price'] - df['Entry Price']).mean()

# Average Loss per trade
average_loss = (df['Entry Price'] - df['Exit Price']).mean()

# Risk Reward Ratio
risk_reward_ratio = average_profit / average_loss

# Expectancy
loss_rate = 1 - win_rate
expectancy = (win_rate * average_profit) - (loss_rate * average_loss)

# Average ROR per trade
risk_free_rate = 0.05
average_ror = (expectancy / average_loss) - risk_free_rate

# Sharpe Ratio
standard_deviation = (df['Exit Price'] - df['Entry Price']).std()
sharpe_ratio = average_ror / standard_deviation

# Max Drawdown
cumulative_returns = ((df['Exit Price'] - df['Entry Price']) / df['Entry Price']).cumsum()
max_drawdown = (cumulative_returns - cumulative_returns.cummax()).min()

# Max Drawdown Percentage
max_drawdown_percentage = (max_drawdown / cumulative_returns.cummax().max()) * 100

# CAGR
beginning_value = 200000
ending_value = df['Exit Price'].iloc[-1]
num_periods = len(df)
cagr = (ending_value / beginning_value) ** (1 / num_periods) - 1

# Calmar Ratio
calmar_ratio = cagr / abs(max_drawdown_percentage)

# Print the calculated parameters

print("Total Trades:", total_trades)

print("Profitable Trades:", profitable_trades)

print("Loss-Making Trades:", loss_making_trades)

print("Win Rate:", win_rate)

print("Average Profit per trade:", average_profit)

print("Average Loss per trade:", average_loss)

print("Risk Reward Ratio:", risk_reward_ratio)

print("Expectancy:", expectancy)

print("Average ROR per trade:", average_ror)

print("Sharpe Ratio:", sharpe_ratio)

print("Max Drawdown:", max_drawdown)

print("Max Drawdown Percentage:", max_drawdown_percentage)

print("CAGR:", cagr)

print("Calmar Ratio:", calmar_ratio)
