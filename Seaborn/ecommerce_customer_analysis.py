import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

data = {
    "customer_id": range(1, 16),
    "age": [19, 24, 31, 42, 27, 35, 51, 23, 46, 38, 29, 55, 33, 41, 26],
    "city": [
        "Istanbul", "Ankara", "Izmir", "Istanbul", "Bursa",
        "Ankara", "Istanbul", "Izmir", "Bursa", "Istanbul",
        "Ankara", "Izmir", "Istanbul", "Bursa", "Ankara"
    ],
    "category": [
        "Electronics", "Clothing", "Electronics", "Books", "Clothing",
        "Electronics", "Books", "Clothing", "Electronics", "Books",
        "Clothing", "Electronics", "Books", "Clothing", "Electronics"
    ],
    "spending": [320, 180, 450, 120, 240, 510, 95, 210, 390, 160, 275, 620, 140, 230, 480],
    "orders": [3, 2, 5, 1, 3, 6, 1, 2, 4, 2, 3, 7, 2, 3, 5]
}

df = pd.DataFrame(data)


print("----------PART 1----------")

sns.set_theme()

sns.barplot(data=df, x="category", y="spending", hue="city")

plt.title("Mean values of spending by categories")
plt.xlabel("Categories")
plt.ylabel("Mean Spending")
plt.grid(True)

plt.text(
    0.98, 0.98,
    "Electronics has got most mean value of spending\n" \
    "Books has got least mean value of spending",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.show()


print("\n----------PART 2----------")

sns.set_theme()

sns.countplot(data=df, x="city")

plt.title("Customer Distribution by City")
plt.xlabel("City")
plt.ylabel("Customer Count")
plt.grid(True)

plt.text(
    0.98, 0.98,
    "Highest: İstanbul\n" \
    "Lowest: İzmir and Bursa",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.show()


print("\n----------PART 3----------")

sns.set_theme()

sns.scatterplot(data=df, x="age", y="spending", hue="category")

plt.title("Distirbution Between Age and Spending")
plt.xlabel("Age")
plt.ylabel("Spending")
plt.grid(True)

plt.text(
    0.98, 0.98,
    "Age and Spending don't seem to have a strong collebration.\n" \
    "Electronics customers show some of the highest spending values.",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.show()


print("\n----------PART 4----------")

sns.set_theme()

sns.histplot(data=df, x="spending", bins=8, kde=True)

plt.title("Spending ranges of customers")
plt.xlabel("Spending Range")
plt.ylabel("Count")
plt.grid(True)

plt.text(
    0.98, 0.98,
    "Most spending values are concentrated\nbetween 100 and 300.",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.show()


print("\n----------PART 5----------")

sns.set_theme()

sns.boxplot(data=df, x="category", y="spending")

plt.title("Boxplot of category and spending")
plt.xlabel("Category")
plt.ylabel("Spending")
plt.grid(True)

plt.text(
    0.98, 0.98,
    "There are no clear outliers.\nElectronics has the widest spread of spending values.",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.show()


print("\n----------PART 6----------")

sns.set_theme()

sns.lineplot(data=df, x="orders", y="spending")

plt.title("Relationship Between Orders and Spending")
plt.xlabel("Orders")
plt.ylabel("Spending")
plt.grid(True)

plt.text(
    0.98, 0.98,
    "There is a positive correlation between orders spending.\n" \
    "The maximum spending value is 620",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.show()


print("\n----------PART 7----------")

sns.set_theme()

correlation = df[["age", "spending", "orders"]].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="viridis"
)

plt.title("Correlation between age, spending and orders")

plt.text(
    0.98, 0.98,
    "There is a strong positive correlation between orders and spending.\n" \
    "There is not a clear correlation between spending and age.",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8)
)

plt.show()


print("\n----------PART 8----------")

sns.set_theme()

sns.pairplot(
    df[["age", "spending", "orders", "category"]],
    hue="category"
)

# plt.text(
#     0.98, 0.98,
#     "Electronics is the most ordering category.\n" \
#     "Clothing category spendings are clustered around 230",
#     transform=plt.gca().transAxes,
#     ha="right",
#     va="top",
#     bbox=dict(boxstyle="round", alpha=0.8)
# )

plt.show()

