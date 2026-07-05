import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("Retail_data.csv")
#plt.scatter(df["discount"],df["footfall"])
#plt.xlabel("Discount")
#plt.ylabel("Footfall")
#plt.title("Discount vs Footfall")
#plt.show()
#Percentage of price difference (Our price vs competitor price)-KPI

promo_footfall = df.groupby("promotion_intensity")["footfall"].mean()

promo_footfall.plot(kind="bar")

plt.title("Average Footfall by Promotion Intensity")
plt.xlabel("Promotion Intensity")
plt.ylabel("Average Footfall")

plt.show()
