import pandas as pd 

data = {
    "product": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Laptop", "Mouse", "Keyboard", "Monitor"
    ],
    "category": [
        "Electronics", "Accessories", "Accessories", "Electronics",
        "Electronics", "Accessories", "Accessories", "Electronics",
        "Electronics", "Accessories", "Accessories", "Electronics"
    ],
    "city": [
        "Istanbul", "Ankara", "Istanbul", "Izmir",
        "Ankara", "Izmir", "Istanbul", "Ankara",
        "Izmir", "Istanbul", "Ankara", "Izmir"
    ],
    "price": [
        30000, 800, 1500, 12000,
        32000, 750, 1700, 11500,
        31000, 850, 1600, 12500
    ],
    "quantity": [
        2, 10, 5, 3,
        1, 15, 4, 2,
        3, 8, 6, 4
    ]
}

df = pd.DataFrame(data)


print("----------PART 1----------")

first5_row = df.head()
sale_count = df.shape[0]
column_name = df.columns
column_type = df.dtypes

print("Dataframe'in ilk 5 sütunu:\n",first5_row, sep="")
print("Toplam satış sayısı: ",sale_count)
print("Sütunların ismi: ",column_name)
print("Sütunların veri tipi:\n",column_type, sep="")


print("\n----------PART 2----------")

df["total"] = df["price"] * df["quantity"]
print("Ürünlerin total satış ücretleri dataframe:\n", df, sep="")


print("\n----------PART 3----------")

mask1 = df["price"] > 10000
greater10k_df = df[mask1]

mask2 = df["city"] ==  "Istanbul"
istanbul_df = df[mask2]

mask3 = (df["price"] > 1000) & (df["quantity"] > 3)
price_quantity_df = df[mask3]

mask4 = (df["city"] == "Istanbul") | (df["city"] == "Ankara")
ist_ank_df = df[mask4]

print(greater10k_df)
print(istanbul_df)
print(price_quantity_df)
print(ist_ank_df)


print("\n----------PART 4----------")

loc_df = df.loc[df["city"] == "Istanbul", ["product", "city", "total"]]
print("İstanbulun analizleri:\n", loc_df, sep="")


print("\n----------PART 5----------")

iloc_df = df.iloc[0:5, [0, 3, 4]]
print(iloc_df)


print("\n----------PART 6----------")

sale_city_df = df["city"].value_counts()
sale_product_df = df["product"].value_counts()

print(sale_city_df)
print(sale_product_df)


print("\n----------PART 7----------")

sorted_df = df.sort_values("total", ascending=False)
sorted_columns = sorted_df[["product","city", "total"]]
print(sorted_columns.head(3))


print("\n----------PART 8----------")

total_sale = df["total"].sum()
mean_sale = df["total"].mean()
max_sale = df["total"].max()
min_sale = df["total"].min()
best_sale_city = sale_city_df.idxmax()
best_sale_product = sale_product_df.idxmax()

print("Toplam satış: ", total_sale)
print("Ortalama satış: ", mean_sale)
print("Max satış: ", max_sale)
print("Minimum satış", min_sale)
print("En fazla satış yapan şehir: ", best_sale_city)
print("En fazla satış yapan ürün: ", best_sale_product)