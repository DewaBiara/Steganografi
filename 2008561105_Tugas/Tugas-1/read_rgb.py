from PIL import Image

# Buka gambar BMP
image = "2.bmp"
img = Image.open(image)

# Mendapatkan dimensi gambar
width, height = img.size

# Meminta pengguna untuk memasukkan titik (x, y)
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

# Pastikan titik (x, y) berada dalam batas gambar
if 0 <= x < width and 0 <= y < height:
    pixel = img.getpixel((x, y))
    red, green, blue = pixel[0], pixel[1], pixel[2]
    print(f"Pixel di posisi ({x}, {y}): R={red}, G={green}, B={blue}")
else:
    print("Titik (x, y) berada di luar batas gambar.")
