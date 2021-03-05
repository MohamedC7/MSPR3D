from PIL import Image
import logging as log

def compare(image1, image2):

    im1 = Image.open(image1)
    im2 = Image.open(image2)
    if list(im1.getdata()) == list(im2.getdata()):
        print("ok")
    else:
        print("no")

compare("ressources/Aipom_Colored.png", "ressources/Aipom.png")