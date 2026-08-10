import numpy as np

image = np.array([
    [120, 90, 200, 50],
    [80, 255, 100, 60],
    [40, 150, 220, 30],
    [10, 70, 180, 240]
])

print("----------PART 1----------")

image_shape = image.shape
total_pixel = image.size
bright_mean = np.mean(image)
most_bright_pixel = np.max(image)
less_bright_pixel = np.min(image)

print("Fotoğrafın boyutu: ", image_shape)
print("Fotoğrafın toplam pixel sayısı: ", total_pixel)
print("Fotoğrafın ortalama parlaklığı: ", bright_mean)
print(f"Fotoğraftaki en parlak pixel {np.unravel_index(np.argmax(image), image.shape)} konumundadır ve parlaklığı {most_bright_pixel} ")
print(f"Fotoğraftaki en az parlak pixel {np.unravel_index(np.argmin(image), image.shape)} konumundadır ve parlaklığı {less_bright_pixel} ")


print("\n----------PART 2----------")

image_plus30 = image + 30
clipped_image = np.clip(image_plus30,0,255)
print("Fotoğrafın parlaklığının 30 arttırılmış hali: \n", clipped_image)


print("\n----------PART 3----------")

image_negative = 255 - image
print("Fotoğrafın negatif hali: \n", image_negative)


print("\n----------PART 4----------")

images_column_middle = int(image.shape[0] / 2)
images_row_middle = int(image.shape[1] / 2)
image_2x2 = image[images_row_middle - 1 : images_row_middle + 1 , images_column_middle - 1: images_column_middle + 1]
print("Fotoğrafın ortası: \n", image_2x2)


print("\n----------PART 5----------")

mask = image > 180

print(f"Fotoğrafta çok parlak {len(image[mask])} adet pixel vardır.")
print("Bunlar: ", image[mask])
