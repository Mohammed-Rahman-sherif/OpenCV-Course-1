from PIL import Image

img = Image.open('alpha.png')

#img2 = Image.open('eagle1.jpg')

Nimg = img.resize((640,480))   # image resizing

#Nimg2 = img2.resize((640,480))



output = Nimg.save('alpha1.png')
#output1 = Nimg2.save('resized_eagle1.png')