import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "name": [
        "Ali", "Ayşe", "Mehmet", "Zeynep", "Can",
        "Elif", "Mert", "Ece", "Burak", "Defne",
        "Kerem", "Selin", "Emir", "Buse", "Arda",
        "Naz", "Kaan", "Duru", "Eren", "İrem",
        "Berk", "Ada", "Yiğit", "Ceren", "Deniz",
        "Sude", "Ozan", "Lina", "Furkan", "Mina"
    ],
    "hours_studied": [
        2.1, 4.5, 3.2, 6.1, 1.8,
        5.4, 3.7, 7.2, 2.9, 6.5,
        4.1, 5.8, 3.4, 2.5, 7.8,
        4.9, 6.3, 3.1, 5.2, 8.1,
        2.7, 6.9, 4.3, 5.6, 3.8,
        7.5, 1.9, 4.7, 6.7, 5.1
    ],
    "score": [
        58, 72, 65, 88, 51,
        81, 69, 94, 61, 86,
        75, 84, 67, 59, 96,
        78, 89, 64, 80, 98,
        55, 91, 73, 83, 68,
        93, 49, 76, 87, 79
    ],
    "group": [
        "A", "A", "B", "B", "A",
        "C", "B", "C", "A", "C",
        "B", "C", "B", "A", "C",
        "B", "C", "A", "B", "C",
        "A", "C", "B", "C", "B",
        "C", "A", "B", "C", "B"
    ]
})

fig = px.scatter(
    df,
    x="hours_studied",
    y="score",
    color="group",
    hover_data=["name"])


fig.show()