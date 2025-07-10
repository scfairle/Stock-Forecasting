
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load data
df = pd.read_csv("barrick_gold_stock_data_cleaned.csv", parse_dates=["Date"])
df.set_index("Date", inplace=True)
close_series = pd.to_numeric(df["Close"], errors="coerce").dropna()

# Fit ARIMA model
model = ARIMA(close_series, order=(5, 1, 0))
result = model.fit()

# Forecast
forecast = result.forecast(steps=30)
forecast_df = pd.DataFrame({
    "Date": pd.date_range(start=close_series.index[-1] + pd.Timedelta(days=1), periods=30, freq="B"),
    "Forecast": forecast
}).set_index("Date")

# Combine for plotting
combined = pd.concat([close_series.tail(60), forecast_df["Forecast"]])

# Plot
plt.figure(figsize=(12, 6))
plt.plot(close_series.tail(60), label="Recent Close Price", color="steelblue")
plt.plot(forecast_df["Forecast"], label="ARIMA Forecast (Next 30 Days)", linestyle="--", color="orange")
plt.title("Barrick Gold - ARIMA Forecast")
plt.ylabel("Price (USD)")
plt.legend()
plt.tight_layout()
plt.savefig("arima_forecast_plot.png")
plt.show()
