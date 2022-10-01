# importing image object from PIL
import math
from PIL import Image, ImageDraw
  
w, h = 1080, 1080
shape = [(5, 5), (w-5, h-5)]
shape2 = [(w-5, 5), (5, h-5)]

hrline1 = [(5, 5), (w-5, 5)]
hrline2 = [(5, 358), (w-5, 358)]
hrline3 = [(5, 716), (w-5, 716)]
hrline4 = [(5, h-5), (w-5, h-5)]

vrline1 = [(5, 5), (5, h-5)]
vrline2 = [(358, 5), (358, h-5)]
vrline3 = [(716, 5), (716, h-5)]
vrline4 = [(w-5, 5), (w-5, h-5)]

# creating new Image object
img = Image.new("RGB", (w, h))
  
# create line image
img1 = ImageDraw.Draw(img)

#Cross
img1.line(shape, fill =None , width = 0)
img1.line(shape2,fill = None,width = 0)

#Horizontal Lines
    #Reactangular Bars at Border
img1.line(hrline1,fill = None,width = 0)
img1.line(hrline4,fill = None,width = 0)
    #Required Lines
img1.line(hrline2,fill = None,width = 0)
img1.line(hrline3,fill = None,width = 0)    

#Vertical Lines
    #Rectangular Borders
img1.line(vrline1,fill = None,width = 0)
img1.line(vrline4,fill = None,width = 0)
    #Required Lines
img1.line(vrline2,fill = None,width = 0)
img1.line(vrline3,fill = None,width = 0)    


img.show()