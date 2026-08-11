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

df["total"] = df["price"] * df["quantity"]


print("----------PART 1----------")

grouped_city_df = df.groupby("city")["total"].sum()
print("Şehirlerin toplam gelirleri:\n",grouped_city_df, sep="")


print("\n----------PART 2----------")

grouped_product_df = df.groupby("product").agg( toplam_miktar=("quantity", "sum"),
                                                toplam_gelir=("total", "sum"),
                                                ortalama_fiyat=("price", "mean"))
print(grouped_product_df)


print("\n----------PART 3----------")


grouped_category_df = df.groupby("category").agg( toplam_gelir=("total","sum"),
                                                  toplam_miktar=("quantity","sum"),
                                                  ortalama_fiyat=("price","mean"))
print(grouped_category_df)


print("\n----------PART 4----------")

grouped_twice_df = df.groupby(["city","product"])["quantity"].sum()
print(grouped_twice_df)


print("\n----------PART 5----------")

sorted_df = grouped_product_df.sort_values("toplam_gelir", ascending=False).head(3)
print(sorted_df)


print("\n----------PART 6----------")

grouped_city_multiple_df = df.groupby("city").agg(toplam_gelir=("total","sum"),
                                                  toplam_miktar=("quantity","sum"),
                                                  ortalama_fiyat=("price","mean" ),
                                                  max_satış=("total","max"))
print(grouped_city_multiple_df)


print("\n----------PART 7----------")

grouped_city_totalmean_df = df.groupby("city")["total"].agg("mean")
best_city = grouped_city_totalmean_df.idxmax()
print(best_city)