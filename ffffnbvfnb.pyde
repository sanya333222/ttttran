img=0
uee=0
eee=0
x=1
w=1
u=1
def setup():
    size(400,600)
    global img
    global uee
    global eee
    img=loadImage("1.jpg")
    uee=loadImage("2.jpg")
    eee=loadImage("3.jpg")
def draw():
    global img
    global uee
    global eee
    global x
    global w
    global u
    image(img,10,200,100,100)
    image(uee,10,340,100,100)
    image(eee,10,470,100,100)
