

from pyfiglet import Figlet
import random
import sys



def fonts():
    figlet = Figlet()
    if len(sys.argv) == 3:
        font = sys.argv[2]
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and font in figlet.getFonts():
            text = input("Input: ")
            figlet.setFont(font=font)
            return figlet.renderText(text)
        else:
            sys.exit("Invalid inputs")

    elif len(sys.argv) == 1:
        text = input("Input: ")
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
        return figlet.renderText(text)

    else:
        sys.exit("Invalid inputs")




print(fonts())


