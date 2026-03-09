import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("oil_prices.csv")

# plot oil price trend
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["Oil_Price"], marker="o")

plt.title("Global Oil Price Trend (1970-2024)")
plt.xlabel("Year")
plt.ylabel("Oil Price USD")
plt.grid()

plt.show()

# Libya economic dependency simulation
df["Libya_Revenue_Index"] = df["Oil_Price"] * 1.15

print(df)
