from astropy.visualization import make_lupton_rgb
from astropy.nddata import NDDataArray
import matplotlib.pyplot as plt
import matplotlib.image as mpimg




def makeRGB(r,g,b):
    image = make_lupton_rgb(r, g, b, stretch=0.5)
    return image
def NOAARGB(ch1,ch2):
    Green=(ch1+ch2)/2 #computes the avarage of channel 2 and 1 that will be used for Green channel
    return makeRGB(ch2,Green,ch1)
def NOAATHERMAL(ch4):
    cmap=plt.cm.hot
    return cmap(ch4)
def NOAADUST(ch4,ch5):
    numerator = NDDataArray.subtract(ch5, ch4)
    denominator = NDDataArray.add(ch4, ch5)
    dust = NDDataArray.divide(numerator, denominator)
    plt.imshow(dust,cmap="hot")
    plt.show()
    return dust

def FENGYUNVEG(ch5,ch4,ch3):
    return  make_lupton_rgb(ch5, ch4, ch3, stretch=0.5)

def FENGYUNSWIR(ch7,ch5,ch4):
    return make_lupton_rgb(ch7, ch5, ch4, stretch=0.5)

def NDVI():
    import time

    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    from astropy.nddata import NDDataArray
    print("This programm will lead you through creating a NDVI map from images")
    print("It works under assumption that you input two images into it: A Red band image and Near infrared image")
    print("The images must be monochrome, cloudless and it would be best if they had a ocean mask applied.")
    print("If they contain clouds/waterbodies, those will also be falsely ranged on scale.")
    print("NIR is Band 4, R is Band 3 or broadband VIS")
    # pathNIR=input("Please input the path to near infrared image:    ")
    # pathR=input("Please input the path to red image:    ")
    print("Please select a color pallete you want to use. Available palletes:")
    print("Greens   Greys   hot    seismic")
    cmapN = input()

    r = mpimg.imread('C:/Users/Karol/Desktop/NIR.png')
    nir = mpimg.imread('C:/Users/Karol/Desktop/R.png')
    numerator = NDDataArray.subtract(nir, r)
    denominator = NDDataArray.add(nir, r)
    ndvi = NDDataArray.divide(numerator, denominator)
    plt.imshow(ndvi, cmap=cmapN)
    plt.colorbar()
    plt.show()






