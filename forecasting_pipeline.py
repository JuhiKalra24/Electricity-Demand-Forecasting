import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def run_forecast(data):
    data = data.copy()

    data["lag_1"] = data["load_actual"].shift(1)
    data["lag_24"] = data["load_actual"].shift(24)

    data = data.dropna()

    features = ["hour", "dayofweek", "month", "solar_gen", "wind_gen", "lag_1", "lag_24"]

    X = data[features]
    y = data["load_actual"]

    split_index = int(len(data) * 0.8)

    X_train = X.iloc[:split_index]
    X_test = X.iloc[split_index:]

    y_train = y.iloc[:split_index]
    y_test = y.iloc[split_index:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)

    return mae