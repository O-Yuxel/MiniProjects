import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = {
    "transport": [
        "Bus", "Metro", "Taxi", "Bicycle",
        "Bus", "Metro", "Taxi", "Bicycle",
        "Bus", "Metro", "Taxi", "Bicycle"
    ],
    "distance": [8, 12, 6, 4, 15, 18, 10, 7, 5, 9, 20, 3],
    "duration": [30, 25, 18, 20, 50, 38, 28, 32, 22, 20, 45, 15],
    "cost": [25, 30, 120, 10, 35, 40, 180, 15, 20, 28, 250, 8],
    "weather": [
        "Sunny", "Cloudy", "Rainy", "Sunny",
        "Rainy", "Sunny", "Cloudy", "Cloudy",
        "Sunny", "Rainy", "Sunny", "Rainy"
    ],
    "day_type": [
        "Weekday", "Weekday", "Weekend", "Weekend",
        "Weekday", "Weekend", "Weekday", "Weekend",
        "Weekend", "Weekday", "Weekend", "Weekday"
    ]
}

df = pd.DataFrame(data)


print("----------PART 1----------")

sns.set_theme()

sns.scatterplot(data=df,
                x="distance",
                y="duration",
                hue="transport",
                style="weather")

plt.title("Four dimension transportation analysis")
plt.xlabel("Distance")
plt.ylabel("Duration")
plt.grid(True)

plt.text(
    0.98, 0.98,
    "Bus has got the longest duration.\n" \
    "Long-distance trips appear more frequently on sunny days in this dataset.",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8, color="black"),
    color="white",
)

plt.show()

print("Graph 1 was showed.")


print("\n----------PART 2----------")

sns.set_theme()

g = sns.relplot(data=df,
                x="distance",
                y="duration",
                hue="transport",
                col="day_type")

g.set_axis_labels("Distance", "Duration")
g.figure.suptitle("Distribution between distance and duration")

g.figure.subplots_adjust(top=0.85)

plt.show()

print("Graph 2 was showed.")


print("\n----------PART 3----------")

sns.set_theme()

g = sns.relplot(data=df,
                x="distance",
                y="duration",
                hue="transport",
                col="day_type",
                row="weather")

g.set_axis_labels("Distance", "Duration")
g.figure.suptitle("Distance and Duration by Weather and Day Type")
g.figure.subplots_adjust(top=0.90)

plt.show()

print("Graph 3 was showed.")


print("\n----------PART 4----------")

sns.set_theme()

g = sns.catplot(data=df,
                x="transport",
                y="cost",
                hue="day_type",
                col="weather",
                kind="box")

g.figure.suptitle("Transportation Cost by Weather")
g.set_axis_labels("Transport", "Cost")
g.figure.subplots_adjust(top=0.85)

g.figure.text(
    0.98, 0.98,
    "On every weather taxi has got highest cost.\n" \
    "On every weather bicycle has got lowest cost.",
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8, color="black"),
    color="white"
)

plt.show()

print("Graph 4 was showed.")


print("\n----------PART 5----------")

sns.set_theme()

g = sns.FacetGrid(
    data=df,
    col="weather")

g.map_dataframe(
    sns.scatterplot,
    x="distance",
    y="duration"
)

g.set_axis_labels("Distance", "Duration")
g.figure.suptitle("Distance and Duration by Weather")
g.figure.subplots_adjust(top=0.85)

g.figure.text(
    0.98, 0.98,
    "On sunny days it seems like duration and distance have positive distribution.\n" \
    "Cloudy-day observations do not show a clear positive relationship between distance and duration.",
    ha="right",
    va="top",
    bbox=dict(boxstyle="round", alpha=0.8, color="black"),
    color="white"
)

plt.show()

print("Graph 5 was showed.")