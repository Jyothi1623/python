import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 17000, 16000, 18000, 20000],
    "Profit": [3000, 3500, 4200, 3900, 4500, 5000],
    "Customers": [120, 140, 160, 155, 180, 200],
    "Marketing_Spend": [2000, 2200, 2500, 2400, 2600, 3000],
    "Rating": [4.1, 4.3, 4.0, 4.2, 4.4, 4.5]
}

df = pd.DataFrame(data)

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].plot(df["Month"], df["Sales"],color="pink")
axs[0, 0].set_title("Sales")


axs[0, 1].bar(df["Month"], df["Profit"],color="cyan")
axs[0, 1].set_title("Profit")

axs[1, 0].barh(df["Month"], df["Customers"],color="lightgreen")
axs[1, 0].set_title("Customers")

axs[1, 1].pie(df["Sales"], labels=df["Rating"], autopct="%0.0f%%",colors=["brown"])
axs[1, 1].set_title("Rating")

plt.tight_layout()
plt.show()
