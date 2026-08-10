import numpy as np

sales = np.array([
    [120, 150, 180, 200],
    [100, 130, 170, 210],
    [140, 160, 190, 220],
    [110, 145, 175, 205],
    [130, 155, 185, 215],
    [125, 170, 195, 230]
])


print("----------PART 1----------")

total_sale = np.sum(sales)
mean_sale = np.mean(sales)
max_sale = np.max(sales)
min_sale = np.min(sales)
month_count = np.shape(sales)[0]
store_count = np.shape(sales)[1]

print("Toplam satış", total_sale)
print("Ortalama satış", mean_sale)
print("En yüksek satış", max_sale)
print("En düşük satış", min_sale)
print("Toplam ay sayısı", month_count)
print("Toplam mağaza sayısı", store_count)


print("\n----------PART 2----------")

stores = np.array(["Mağaza 1", "Mağaza 2", "Mağaza 3", "Mağaza 4"])

stores_total_sales = np.sum(sales, axis=0)
n = 0
for i in stores_total_sales:
    print(f"{stores[n]}: ",i)
    n +=1


print("\n----------PART 3----------")

months = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]
months_total_sales = np.sum(sales, axis=1)
best_sale_month = np.argmax(months_total_sales)
k = 0
for i in months_total_sales:
    print(f"{months[k]}: ", i)
    k += 1
print("En fazla satış yapılan ay: ", months[best_sale_month])

print("\n----------PART 4----------")

mask = np.mean(sales, axis=0) > 170
succesful_stores = stores[mask]
print("Başarılı mağzaların listesi: ", succesful_stores)


print("\n----------PART 5----------")

all_sales_deviation = np.std(sales)
all_stores_devaition = np.std(sales, axis=0)

print("Toplam standart sapma: ", all_sales_deviation)
print("Mağazaların standart sapmaları:")
m = 0
for i in all_stores_devaition:
    print(f"{stores[m]}: ", i)
    m += 1


print("\n----------PART 6----------")

mask = sales > 200
rows, columns = np.where(sales > 200)
print("200'den büyük satış sayısı: ", len(rows))
print("Satışlar: ")
for row, column in zip(rows, columns):
    print(stores[column], months[row], sales[row, column])