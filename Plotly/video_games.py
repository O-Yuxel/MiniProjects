import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "game": [
        "Eclipse", "Frontier", "Shadow Realm", "Neon Drift",
        "Iron Kingdom", "Starfall", "Pixel Quest", "Dark Horizon",
        "Cyber Strike", "Mystic Lands", "Rogue Protocol", "Skybound",
        "Frozen Core", "Wild West", "Titan Arena",
        "Moonlight", "Battlefront", "Deep Space", "Dragon Age",
        "Velocity"
    ],

    "genre": [
        "Action", "RPG", "RPG", "Racing",
        "Strategy", "RPG", "Adventure", "Action",
        "Shooter", "Adventure", "Action", "Adventure",
        "Strategy", "Action", "Fighting",
        "Adventure", "Shooter", "Simulation", "RPG", "Racing"
    ],

    "platform": [
        "PC", "PS5", "PC", "Xbox",
        "PC", "PS5", "Switch", "PS5",
        "Xbox", "Switch", "PC", "PS5",
        "PC", "Xbox", "PS5",
        "Switch", "PC", "Xbox", "PS5", "PC"
    ],

    "price": [
        59.99, 69.99, 49.99, 39.99,
        44.99, 69.99, 29.99, 59.99,
        64.99, 34.99, 54.99, 39.99,
        49.99, 59.99, 69.99,
        24.99, 64.99, 44.99, 69.99, 34.99
    ],

    "rating": [
        8.7, 9.2, 8.4, 7.6,
        8.1, 9.4, 7.9, 8.8,
        8.5, 7.4, 8.9, 8.0,
        7.7, 8.6, 8.3,
        7.8, 9.0, 7.5, 9.1, 7.2
    ],

    "hours_played": [
        42, 87, 63, 28,
        76, 94, 35, 51,
        68, 41, 59, 32,
        71, 48, 38,
        27, 82, 56, 91, 24
    ],

    "sales_million": [
        8.4, 12.7, 6.8, 4.2,
        7.5, 15.3, 5.1, 9.6,
        11.2, 4.7, 8.9, 6.2,
        5.8, 10.4, 7.1,
        3.9, 13.6, 5.4, 14.2, 3.5
    ]
})


print("----------PART 1----------")

fig = px.scatter(
    df,
    x="price",
    y="sales_million",
    color="genre",
    title="Distribution between price and sales"
)

fig.update_layout(
    xaxis_title="Price",
    yaxis_title="Sales (Million)",
    legend_title="Genres"
)

fig.show()


print("\n----------PART 2----------")

grouped_df = df.groupby("genre")["sales_million"].sum()

fig2 = px.bar(
    x=grouped_df.index,
    y=grouped_df.values,
    title="Sales by genres"
)

fig2.update_layout(
    xaxis_title="Groups",
    yaxis_title="Sales (Million)",
)

fig2.show()


print("\n----------PART 3----------")


fig3 = px.histogram(
    df,
    x="rating",
    nbins=10,
    title="Ranges in which the ratings are found"
)

fig3.update_layout(
    xaxis_title="Rating Ranges",
    yaxis_title="Count"
)

fig3.show()


print("\n----------PART 4----------")

fig4 = px.box(
    df,
    x="genre",
    y="rating",
    title="Ratings by genres"
)

fig4.update_layout(
    xaxis_title = "Genres",
    yaxis_title = "Ratings"
)

fig4.show()


print("\n----------PART 5----------")

fig5 = px.scatter(
    df,
    x="hours_played",
    y="sales_million",
    color="genre",
    size="rating",
    hover_data=["game"],
    title="Sales by hours played"
)

fig5.update_layout(
    xaxis_title="Hours Played",
    yaxis_title="Sales (Million)",
    legend_title = "Genres"
)

fig5.show()

fig5.write_html("game_analysis.html")