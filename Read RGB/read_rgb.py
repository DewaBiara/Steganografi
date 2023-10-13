from PIL import Image

# Buka gambar BMP
image_path = "2.bmp"
img = Image.open(image_path)

# Mendapatkan dimensi gambar
width, height = img.size

# Membaca nilai RGB dari gambar
for y in range(height):
    for x in range(width):
        pixel = img.getpixel((x, y))
        red, green, blue = pixel[0], pixel[1], pixel[2]

        print(f"Pixel di posisi ({x}, {y}): R={red}, G={green}, B={blue}")
