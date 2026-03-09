import pandas as pd
import matplotlib.pyplot as plt

# dataset
data = {
    "Year":[1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020,2022,2024,2026],
    "Oil_Price":[3,12,35,27,22,18,28,54,79,52,41,100,82,90]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,5))
plt.plot(df["Year"],df["Oil_Price"],marker="o")

plt.title("Global Oil Price Trend 1970-2026")
plt.xlabel("Year")
plt.ylabel("Oil Price USD")
plt.grid()

plt.show()

# Libya revenue estimation
df["Libya_Revenue_Index"] = df["Oil_Price"] * 1.2

print(df)
