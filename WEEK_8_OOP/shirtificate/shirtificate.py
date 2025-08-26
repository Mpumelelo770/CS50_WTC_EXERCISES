
from fpdf import FPDF


def main():


    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margin(0)
    pdf.set_font("Times", style = "B", size = 30)
    pdf.cell(160, 40, "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C", center = True)
    pdf.image("shirtificate.png")
    pdf.set_font("Times", style = "B", size = 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(120)
    pdf.cell(16, 4, f"{name} took CS50", new_x = "LMARGIN", new_y = "NEXT", align = "C", center = True)
    pdf.output("shirtificate.pdf")








if __name__ == "__main__":
    main()
