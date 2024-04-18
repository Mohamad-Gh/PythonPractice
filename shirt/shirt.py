# implement a program that expects exactly two command-line arguments:
import os.path
import sys
import pathlib
from PIL import Image, ImageOps


def main():
    in_put, out_put = command_line_arg_check()
    shirt(in_put, out_put)

def command_line_arg_check():
    # if the input is more than 3 words
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # if the input is less than 3 words
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # input name is not jpeg, jpg, png
    sufix= os.path.splitext(sys.argv[1])
    sufix_2 = os.path.splitext(sys.argv[2])
    if sufix[1].lower() == '.jpg' or sufix[1].lower() == '.jpeg' or sufix[1].lower() == '.png':
        if sufix[1].lower() != sufix_2[1].lower():
            sys.exit("Files with different format")
    else:
        sys.exit(f"Could not read {sys.argv[1]}")
        # return the command-line arguments for the next code
    return sys.argv[1], sys.argv[2]

def shirt(file1, file2):
    image = Image.open(file1)
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    resized_image = ImageOps.fit(image, shirt_size)
    resized_image.paste(shirt, mask=shirt)
    resized_image.save(file2)



if __name__=="__main__":
    main()