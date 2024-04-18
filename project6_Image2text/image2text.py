import datetime
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract"
def main():
    convert()

def convert():
    img = Image.open("Capture.PNG")
    img2text=pytesseract.image_to_string(img)
    name = datetime.datetime.now()
    filename= f"D:/python/projects20/pythonProject1/project6/script-{name.day}-{name.hour}-{name.minute}-{name.second}.txt"
    with open(filename, "w") as file:
        file.write(img2text)


if __name__=="__main__":
    main()