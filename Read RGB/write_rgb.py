from PIL import Image

def read_rgb_pixel(image, x, y):
    """
    Membaca nilai RGB pixel di titik (x, y) dari citra.
    """
    pixel = image.getpixel((x, y))
    return pixel

def write_rgb_pixel(image, x, y, rgb):
    """
    Menulis nilai RGB ke pixel di titik (x, y) pada citra.
    """
    image.putpixel((x, y), rgb)

def main():
    # Buka citra sumber
    source_image = Image.open("2.bmp")

    # Buka citra cover
    cover_image = Image.open("3.bmp")

    # Tentukan titik (x, y) di citra sumber untuk membaca nilai RGB
    x_source = 100
    y_source = 200

    # Baca nilai RGB dari citra sumber
    rgb_value = read_rgb_pixel(source_image, x_source, y_source)
    print(f"Nilai RGB di ({x_source}, {y_source}): {rgb_value}")

    # Tentukan titik (x, y) di citra cover untuk menulis nilai RGB
    x_cover = 50
    y_cover = 60

    # Menulis nilai RGB ke citra cover
    write_rgb_pixel(cover_image, x_cover, y_cover, rgb_value)

    # Simpan citra cover yang telah diubah
    cover_image.save("cover_with_rgb.bmp")

if __name__ == '__main__':
    main()
