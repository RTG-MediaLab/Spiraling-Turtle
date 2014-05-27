import turtle
import random
import winsound


wn = turtle.Screen()
print(wn.screensize())


#wn.bgcolor("#808000")
#wn.bgcolor("lightgreen")
wn.bgcolor("orange")
print(turtle.window_height(), turtle.window_width())
#turtle.setup(width=_CFG["width"], height=_CFG["height"], startx=_CFG["leftright"], starty=_CFG["topbottom"])
#turtle.setup(width=_CFG["width"], height=_CFG["height"], startx=_CFG["leftright"], starty=_CFG["topbottom"])

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

wn.textinput("NIM", "Name of first player:")
tid_i_sekunder = wn.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)
tid_i_sekunder = int(tid_i_sekunder)
tess.penup()                # This is new
tess.pendown()

print(turtle.turtles())
#turtle.screensize(canvwidth=None, canvheight=None, bg=None)
size = 1
turtle.colormode(255)
for i in range(tid_i_sekunder):
   print(i)
   turtle.delay(100)
   tess.stamp()             # Leave an impression on the canvas
   tess.pencolor(random.randint(0,255), 160, 80)
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(24)           #  ...  and turn her
   tess.shapesize(i*0.1+1,i*0.1+1)
   tess.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
#winsound.PlaySound("*", winsound.SND_ALIAS)
winsound.PlaySound("Bass_and_asdf.wav", winsound.SND_ALIAS)
turtle.turtles()
tess.clear()
wn.mainloop()
