import argparse
from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter


def make_filter_sepia(image):
    sepia_r, sepia_g, sepia_b = 112, 66, 20

    sepia_image = Image.new('RGB', image.size)


    for x in range(image.width):
        for y in range(image.height):

            r, g, b = image.getpixel((x,y))

            new_r = int(r * 0.393 + g * 0.769 + b * 0.189)
            new_g = int(r * 0.349 + g * 0.686 + b * 0.168)
            new_b = int(r * 0.272 + g * 0.534 + b * 0.131)

            sepia_r = min(new_r, 255)
            sepia_g = min(new_g, 255)
            sepia_b = min(new_b, 255)

            sepia_image.putpixel((x,y), (sepia_r, sepia_g, sepia_b))

    sepia_image.save("images/new_photo.png", "png")

def make_filter_bw(image):
    new_photo = image.convert('L')
    new_photo.save("images/new_photo.png", "png")

def make_filter_сontrast(image):
    new_photo = ImageOps.autocontrast(image, cutoff=5)
    new_photo.save("images/new_photo.png", "png")

def make_filter_blur(image):
    new_photo = image.filter(ImageFilter.GaussianBlur(radius=2.4))
    new_photo.save("images/new_photo.png", "png")

def make_filter_median(image):
    image.filter(ImageFilter.MedianFilter(size=3))
    image.save("images/new_photo.png", "png")

def make_filter_frame(image):
    width, height = image.size
    frame_image = image.transform((width + 100, height + 100), Image.EXTENT,
                        (-10, -10, width + 10, height + 10), Image.BILINEAR)
    frame_image.save("images/new_photo.png", "png")
 
def main():
    parser = argparse.ArgumentParser()


    parser.add_argument("--enable_sepia_filter", action="store_true", help="проверить хочет ли пользователь включить фильтр сепии"),

    parser.add_argument("--enable_bw_filter", action="store_true", help="проверить хочет ли пользователь включить черно-белый фильтр"),

    parser.add_argument("--enable_contrast_filter", action="store_true", help="проверить хочет ли пользователь включить контрастный фильтр"),

    parser.add_argument("--enable_blur_filter", action="store_true", help="проверить хочет ли пользователь включить фильтр размытия"),

    parser.add_argument("--enable_median_filter", action="store_true", help="проверить хочет ли пользователь включить медианный фильтр"),

    parser.add_argument("--enable_frame_filter", action="store_true", help="проверить хочет ли пользователь включить фильтр рамки"),

    parser.add_argument('-file_name', help='Имя входного файла', default='photo_one.jpg')

    args = parser.parse_args()
    
    image = Image.open(f"images/{args.file_name}")

    if args.enable_sepia_filter:
        make_filter_sepia(image)
    if args.enable_bw_filter:
        make_filter_bw(image)
    if args.enable_blur_filter:
        make_filter_blur(image)
    if args.enable_contrast_filter:
        make_filter_сontrast(image)
    if args.enable_frame_filter:
        make_filter_frame(image)
    if args.enable_median_filter:
        make_filter_median(image)

if __name__ == "__main__":
    main()
