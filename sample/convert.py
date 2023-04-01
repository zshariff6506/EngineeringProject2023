def converttorgb(wavelength):
    R, G, B=0, 0, 0

    if(wavelength < 400 and wavelength > 700):
        return "invalid"

    if(wavelength > 400 and wavelength < 444.721):
        R = -(1/16)*(wavelength-400)**2+125
    elif(wavelength > 444.721 and wavelength < 514.285714):
        R = 0
    elif(wavelength >= 514.285714 and wavelength < 575):
        R = (wavelength-514.285714)*4.2
    elif(wavelength >= 575 and wavelength < 700):
        R = 255

    if(wavelength >= 400 and wavelength < 425):
        B = (wavelength*4.2)-1530
    elif(wavelength > 425 and wavelength <= 500):
        B = 255
    elif(wavelength > 500 and wavelength < 514.285714):
        B = -17.85*wavelength+255
    else:
        B = 0

    if(wavelength > 444.721 and wavelength < 500):
        G = 4.61296333*(wavelength-444.721)
    elif(wavelength > 500 and wavelength < 575):
        G = 255
    elif(wavelength > 575 and wavelength < 645):
        G = -3.64285714*(wavelength-645)

    R = round(R)
    G = round(G)
    B = round(B)

    return (R, G, B)

if __name__ == "__main__":
    print('The purpose of this file is as a module.')