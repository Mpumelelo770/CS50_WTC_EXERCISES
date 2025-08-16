
from PIL import Image
from PIL import ImageOps # for resizing and cropping
import sys



def main():


    validation()
    first = sys.argv[1]
    second = sys.argv[2]
    overlay(first, second)




def validation():

    if len(sys.argv) < 3:
       sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].lower().endswith((".jpg","jpeg","png")) or not sys.argv[2].lower().endswith(("jpg", "jpeg", "png")):
        sys.exit("Invalid output")

    extension1 = sys.argv[1].split(".")
    extension2 = sys.argv[2].split(".")

    if extension1[-1] != extension2[-1]:
        sys.exit("Input and output have different extensions")






def overlay(initial,final):
    try:
        with Image.open(initial,"r") as background, Image.open("shirt.png", "r") as shirt:
            size_shirt = shirt.size
            overlay = shirt.convert("RGBA")
            sized_background = ImageOps.fit(background, size_shirt, 3, 0, (0.5,0.5))

            sized_background.paste(shirt, overlay)
            sized_background.save(final)
    except FileNotFoundError:
        sys.exit("Input does not exist")





if __name__ == "__main__":
    main()
