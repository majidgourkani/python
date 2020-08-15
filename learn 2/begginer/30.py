from PIL import Image

image = Image.open('Rose.jpg')

w , h = image.size
for x in range(w):
    for y in range(h):
        pix_pos = (x,y)
        #in the PNG pic, we need alpha channel
        r, g, b = image.getpixel(pix_pos)
        negetiv_color = (255-r , 255-g , 255-b)
        image.putpixel(pix_pos, negetiv_color)

image.show()
image.save("negetive_rose.jpg")
