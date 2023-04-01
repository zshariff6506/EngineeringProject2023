from PIL import Image
from convert import converttorgb as rgb

fileinput = input('Enter the file name:')

filename, saveas = fileinput+'.png', fileinput+'_convert.png'

im = Image.open(filename)
pix, size = im.load(), im.size

try:
    for x in range(size[0]):
        for y in range(size[1]):
           givenrgb = pix[x,y]
           rgbfactor = (givenrgb[0]+givenrgb[1]+givenrgb[2])/3
           wavelength = (300*rgbfactor/255)+400
           color = rgb(wavelength)
           pix[x,y] = color
except TypeError:
    print('Sorry, this file is not compatible. Try to take a screenshot and try again.')
im.save(saveas)
