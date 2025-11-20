import pandas as pd
import matplotlib .pyplot as plt

info = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    "Visitors": [220, 260, 240, 280, 300, 350],
    "Clicks": [120, 135, 128, 150, 160, 180],
    "Bounce_Rate": [45, 42, 40, 38, 35, 30],
    "Conversion": [12, 15, 13, 18, 20, 22],
    "Avg_Time_on_Site": [3.5, 3.8, 4.0, 4.2, 4.5, 5.0]
}

df=pd.DataFrame(info)
# print(df)
# df.plot()
# plt.show()

fig, axs=plt.subplots(2,2, figsize=(12,8))

axs[0,0].plot(df["Day"],df["Visitors"],color="violet")
axs[0,0].set_title("D VS V")
axs[0,1].bar(df["Day"],df["Clicks"],color="orange")
axs[0,1].set_title("D VS C")
axs[1,0].barh(df["Bounce_Rate"],df["Clicks"],color="black")
axs[1,0].set_title("B VS C")
axs[1,1].pie(df["Bounce_Rate"],labels=df["Avg_Time_on_Site"],autopct="%1.1f%%",colors=["cyan"])
axs[1,1].set_title("B VS A")

plt.tight_layout()
plt.show()
