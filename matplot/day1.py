import pandas as p
import matplotlib .pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 17000, 16000, 18000, 20000],
    "Profit": [3000, 3500, 4200, 3900, 4500, 5000],
    "Customers": [120, 140, 160, 155, 180, 200],
    "Marketing_Spend": [2000, 2200, 2500, 2400, 2600, 3000],
    "Rating": [4.1, 4.3, 4.0, 4.2, 4.4, 4.5]
}
df=p.DataFrame(data)
# print(df)
# df.plot()
# plt.show()

# plt.bar(df["Month"],df["Sales"], color=["deeppink","cyan","brown","orange","blue","lightgreen"])
# plt.bar(df["Month"],df["Profit"], color=["grey","violet","blue","lightpink","deepwhite","lightyellow"])
# plt.legend(["Sales","Profit"])


# plt.show()
# plt.barh(df["Month"],df["Sales"], color=["deeppink","cyan","brown","orange","blue","lightgreen"])
# plt.barh(df["Month"],df["Profit"], color=["grey","violet","blue","lightpink","deepwhite","lightyellow"])
# plt.legend(["Sales","Profit"])


# plt.show()

# plt.pie(df["Sales"],labels=df["Month"],autopct="%1.0f%%")
# plt.title("sales distribution")
# plt.show()


plt.fill_between(df["Month"],df["Sales"],alpha=1)
plt.show()