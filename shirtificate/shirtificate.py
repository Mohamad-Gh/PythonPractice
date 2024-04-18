from fpdf import FPDF
pdf = FPDF()

def main():
    pdfmaker(input("Name: "))


def pdfmaker(name):
    pdf.add_page()
    pdf.set_font("helvetica", "B", 36)
    pdf.cell(200,100, text="CS50 Shirtificate",new_x ="LMARGIN" , new_y="NEXT", align="c")
    pdf.image("shirtificate.png", 20, 80, 175)
    pdf.set_font("helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(200, 50,f"{name} Took CS50", align="c")
    pdf.output("shirtificate.pdf")
    return

if __name__=="__main__":
    main()
