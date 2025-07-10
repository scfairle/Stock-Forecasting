# 📈 Stock Price Forecasting – Barrick Gold (ARIMA Model)

This project forecasts Barrick Gold's (ticker: GOLD) stock prices using a univariate ARIMA time series model.

---

## 🔍 Data Overview

- Daily closing prices (2019–2024)
- Cleaned, indexed by date
- Source: Yahoo Finance

---

## 🧠 Model

- Model: **ARIMA(5,1,0)**
- Forecast horizon: **30 business days**
- Libraries: `pandas`, `matplotlib`, `statsmodels`

---

## 📊 Insights

- Recent trends and volatility are captured through rolling averages and daily return analysis
- ARIMA effectively models and forecasts short-term price momentum

---

## 📁 Files

- `barrick_gold_stock_data_cleaned.csv` — input data
- `stock_forecasting_arima.py` — analysis + forecast
- `arima_forecast_plot.png` — forecast visualization

---

## 🧠 Business Application

- Helps estimate near-future price movement
- Useful for short-term trading signals, investment timing, or scenario planning

---

👤 Author: **Samuel Fairley**  
📎 [LinkedIn](https://www.linkedin.com/in/samuelfairley) | 📁 [GitHub](https://github.com/scfairle)
