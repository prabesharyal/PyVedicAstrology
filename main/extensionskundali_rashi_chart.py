# importing image object from PIL
from PIL import Image, ImageDraw, ImageFont

#Scalable Height Width  
w, h = 1000, 1000

per5 = (5/w)
shape = [(per5*w, per5*h), (w-(per5*w), h-(per5*h))]
shape2 = [(w-(per5*w), (per5*h)), ((per5*w), h-(per5*h))]

hrline1 = [((per5*w), (per5*h)), (w-(per5*w), (per5*h))]
hrline2 = [((per5*w), (h/3)), (w-(per5*w), (h/3))]
hrline3 = [((per5*w), ((h/3)*2)), (w-(per5*w), ((h/3)*2))]
hrline4 = [((per5*w), h-(per5*h)), (w-(per5*w), h-(per5*h))]

vrline1 = [((per5*w), (per5*h)), ((per5*w), h-(per5*h))]
vrline2 = [(((w/3)*1), (per5*h)), (((w/3)*1), h-(per5*h))]
vrline3 = [(((w/3)*2), (per5*h)), (((w/3)*2), h-(per5*h))]
vrline4 = [(w-(per5*w), (per5*h)), (w-(per5*w), h-(per5*h))]

# creating new Image object
img = Image.new("RGBA", (w, h), color = "#F9DBB6")
  
# create line image
img1 = ImageDraw.Draw(img)

linestrokewidth = 5 #in a square of 1080p
color = "red"

#Cross
img1.line(shape, fill =color , width = int((linestrokewidth/1080)*w))
img1.line(shape2,fill = color,width = int((linestrokewidth/1080)*h))

#Horizontal Lines
    #Reactangular Bars at Border
img1.line(hrline1,fill = color,width = int((linestrokewidth/1080)*w))
img1.line(hrline4,fill = color,width = int((linestrokewidth/1080)*h))
    #Required Lines
img1.line(hrline2,fill = color,width = int((linestrokewidth/1080)*w))
img1.line(hrline3,fill = color,width = int((linestrokewidth/1080)*h))    

#Vertical Lines
    #Rectangular Borders
img1.line(vrline1,fill = color,width = int((linestrokewidth/1080)*w))
img1.line(vrline4,fill = color,width = int((linestrokewidth/1080)*h))
    #Required Lines
img1.line(vrline2,fill = color,width = int((linestrokewidth/1080)*w))
img1.line(vrline3,fill = color,width = int((linestrokewidth/1080)*h))    

#Adding font
font = ImageFont.truetype("./devnew.ttf", int((50/1080)*((w+h)/2)))
fontcolor = "black"

pos1 , text1  = (int((3/6)*w), int((1/6)*h)),  "1" 
pos2 , text2  =(int((1.25/6)*w), int((0.5/6)*h)),  "2" 
pos3 , text3  = (int((0.5/6)*w), int((1.25/6)*h)) ,  "3"
pos4 , text4  = (int((1/6)*w), int((3/6)*h)) ,  "4"
pos5 , text5  = (int((0.5/6)*w), int((4.5/6)*h)) ,  "5"
pos6 , text6  = (int((1.25/6)*w), int((5.25/6)*h)) ,  "6"
pos7 , text7  = (int(w/2), int((5/6)*h)) ,  "7"
pos8 , text8  = (int((4.5/6)*w), int((5.25/6)*h)) ,  "8"
pos9, text9   = (int((5.25/6)*w), int((4.5/6)*h)) ,  "9"
pos10, text10  = (int((5/6)*w), int((3/6)*h)) , "10"
pos11 , text11 = (int((5.25/6)*w), int((1.25/6)*h)) , "11"
pos12 , text12 = (int((4.5/6)*w), int((0.5/6)*h)) , "12"

#Writing Text to images
img1.text(pos1,text1,fontcolor, font=font)
img1.text(pos2,text2,fontcolor, font=font)
img1.text(pos3,text3,fontcolor, font=font)
img1.text(pos4,text4,fontcolor, font=font)
img1.text(pos5,text5,fontcolor, font=font)
img1.text(pos6,text6,fontcolor, font=font)
img1.text(pos7,text7,fontcolor, font=font)
img1.text(pos8,text8,fontcolor, font=font)
img1.text(pos9,text9,fontcolor, font=font)
img1.text(pos10,text10,fontcolor, font=font)
img1.text(pos11,text11,fontcolor, font=font)
img1.text(pos12,text12,fontcolor, font=font)


#img.save('hello.png')
img.show()

'''
अष्टत्रि शून्यं शशि नंदमेकं खसप्तमेकं रस शुन्यंमेकं ब्रह्मा मपुराणे 
नवभजिताप्तं सत्यं च सत्यं स्थिरराशिचक्रम् ।
'''
#shlok has error due to unique issues

#This will be called whenever required. As of now, this file is completed.
