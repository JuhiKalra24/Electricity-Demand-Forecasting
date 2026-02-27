# Electricity Demand Forecasting & Peak Risk Analysis

## Overview
This project analyzes 50,000+ hourly electricity load observations (2015–2020) from real-world grid data.

The objective was to:
- Improve short-term load forecasting accuracy
- Identify statistically significant demand patterns
- Quantify extreme peak load risk
- Build an automated forecasting pipeline in Python

---

## Key Results

### Forecast Accuracy Improvement
- Baseline (Naive) MAE: 4,468 MW
- Improved Regression MAE: 1,437 MW
- 67.8% reduction in forecasting error

### Statistical Findings
- Weekday demand significantly higher than weekend demand
- Average weekday demand ≈ 58.6 GW
- Average weekend demand ≈ 47.8 GW
- Hypothesis test: p < 0.001

### Peak Demand Risk Analysis
- 95th percentile threshold: 70.8 GW
- Identified 2,514 extreme load hours
- 91% of peak hours occur during winter months (Nov–Feb)

---

## Techniques Used
- Python (Pandas, NumPy, Matplotlib)
- Feature engineering (lag variables)
- Linear Regression
- Time-series modeling
- Hypothesis testing (t-test)
- Error metrics (MAE, RMSE)
- Basic automation via modular pipeline

---

## Business Relevance
Improved short-term forecasting accuracy can reduce imbalance penalties and improve grid planning efficiency. Seasonal peak concentration highlights winter stress risk for capacity planning.