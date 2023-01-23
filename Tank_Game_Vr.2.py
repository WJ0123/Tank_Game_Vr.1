# production ver 2

from Tkinter import *
import time, math, random

win = Tk()
winX = 1000
winY = 500

groundlvl = 30
groundlvladj = groundlvl + 2
realgroundval = winY - groundlvladj

groundclr = 'brown'
groundwidth = 3
skyclr = 'light blue'

car1sizeX = 50
car1sizeY = 30
car1clr = 'red'
car1posX = 50
car1posY = 0

niddleLn = 30
gravity = .098
power = 5
ang = 130

car1dx = 0
car1dy = 0
niddle1ang = 0
carspeed = 2

inair = 0
bulletsize = 5
bulletclr = 'red'

canv = Canvas(win, height=winY, width=winX, bg=skyclr)
canv.pack()

# --------------------#
ground = canv.create_line(0, winY - groundlvl, winX, winY - groundlvl, \
                          fill=groundclr, width=groundwidth)
car1 = canv.create_rectangle(car1posX, winY - groundlvladj - car1posY, car1posX + \
                             car1sizeX, winY - groundlvladj - car1posY - car1sizeY, fill=car1clr, outline=car1clr,
                             tags='car1')


# --------------------#

def disp():
    global winX, winY, groundlvladj, car1dx, car1dy, inair, bulletdx, bulletdy, bulletX, bulletY, angADJ, bullet, aa, \
        car1sizeX, car1sizeY, car1clr, car1posX, car1posY, gravity, car1cntrX, car1cntrY, ang, car1, niddle1, niddle1ang
    while True:

        if inair == 1:

            if canv.coords(bullet)[3] < winY - groundlvladj:
                bulletdy = bulletdy - gravity
                canv.move(bullet, bulletdx, -bulletdy)

            else:

                if aa == 0:
                    impactpt = canv.coords(bullet)[0] + bulletsize

                    x1 = impactpt
                    y1 = realgroundval
                    x2 = impactpt
                    y2 = realgroundval

                elif aa < 70:
                    mm = 2
                    x1 -= .2 * mm
                    y1 -= .15 * mm
                    x2 += .2 * mm
                    y2 += .15 * mm

                    canv.create_arc(x1, y1, x2, y2, start=5, extent=170, outline=bulletclr, \
                                    fill=bulletclr, tags='arc')
                else:
                    inair = 0
                    canv.delete('bullet')
                aa += 1
                print aa

        if canv.coords(car1)[0] <= 0:
            canv.move(car1, 2, 0)
        elif canv.coords(car1)[2] >= winX:
            canv.move(car1, -2, 0)
        elif canv.coords(car1)[0] >= 2 and canv.coords(car1)[2] <= winX - 2:
            canv.move(car1, car1dx, 0)

        ang = ang + niddle1ang
        if ang < 0:
            ang = 0
        elif ang > 180:
            ang = 180

        car1cntrX, car1cntrY = canv.coords(car1)[0] + car1sizeX / 2, canv.coords(car1)[3] - car1sizeY / 2

        angADJ = ang - 90
        niddletipX = car1cntrX + niddleLn * math.sin(math.radians(angADJ))
        niddletipY = car1cntrY - niddleLn * math.cos(math.radians(angADJ))

        niddle1 = canv.create_line(car1cntrX, car1cntrY, niddletipX, niddletipY, width=3, tags='niddle1')

        canv.update()
        time.sleep(.01)
        canv.delete('niddle1', 'arc')


def car1mv(a):
    global car1dx
    car1dx = a


def niddle1mv(a):
    global niddle1ang
    niddle1ang = a


def fire(event):
    global inair, bulletdx, bulletdy, bulletX, bulletY, car1cntrX, car1cntrY, angADJ, bullet, aa
    bulletX = car1cntrX
    bulletY = car1cntrY
    canv.delete('bullet')
    bulletdx = power * math.sin(math.radians(angADJ))
    bulletdy = power * math.cos(math.radians(angADJ))

    bullet = canv.create_oval(bulletX - bulletsize, bulletY - bulletsize, \
                              bulletX + bulletsize, bulletY + bulletsize, \
                              tags='bullet', outline=bulletclr, fill=bulletclr)

    aa, inair = 0, 1


win.bind('<KeyPress-Left>', lambda x: car1mv(-carspeed))
win.bind('<KeyPress-Right>', lambda x: car1mv(carspeed))
win.bind('<KeyPress-w>', lambda x: niddle1mv(-carspeed))
win.bind('<KeyPress-e>', lambda x: niddle1mv(carspeed))
win.bind('<KeyRelease-e>', lambda x: niddle1mv(0))
win.bind('<KeyRelease-Right>', lambda x: car1mv(0))
win.bind('<KeyRelease-Left>', lambda x: car1mv(0))
win.bind('<KeyRelease-w>', lambda x: niddle1mv(0))
win.bind('<f>', fire)

disp()

win.mainloop()

'''		
def niddle1E(event):
	global winX, winY, groundlvl, groundlvladj, groundclr, groundwidth, skyclr, car1dx, car1dy, niddle1ang,\
			car1sizeX, car1sizeY, car1clr, car1posX, car1posY, gravity, car1cntrX, car1cntrY, ang, car1, niddle1
	niddle1ang = 1
	
def niddle1N(event):
	global winX, winY, groundlvl, groundlvladj, groundclr, groundwidth, skyclr, car1dx, car1dy, niddle1ang,\
			car1sizeX, car1sizeY, car1clr, car1posX, car1posY, gravity, car1cntrX, car1cntrY, ang, car1, niddle1
	niddle1ang = 0

def keys1(event):
	global winX, winY, groundlvl, groundlvladj, groundclr, groundwidth, skyclr, car1dx, car1dy,\
			car1sizeX, car1sizeY, car1clr, car1posX, car1posY, gravity, car1cntrX, car1cntrY, ang, car1, niddle1
	
	if canv.coords(car1)[0] > 0: car1dx = -1
	
	
def keys0(event):
	global winX, winY, groundlvl, groundlvladj, groundclr, groundwidth, skyclr, car1dx, car1dy,\
			car1sizeX, car1sizeY, car1clr, car1posX, car1posY, gravity, car1cntrX, car1cntrY, ang, car1, niddle1
	
	if canv.coords(car1)[0] > 0: car1dx = 0	
	
def keys2(event):
	global winX, winY, groundlvl, groundlvladj, groundclr, groundwidth, skyclr, car1dx, car1dy,\
			car1sizeX, car1sizeY, car1clr, car1posX, car1posY, gravity, car1cntrX, car1cntrY, ang, car1, niddle1
	
	if canv.coords(car1)[0] > 0: car1dx = 1
'''
'''
def click(event):
	canv.coords(car1,100,100,100 + car1sizeX, 50 + car1sizeY)
	canv.itemconfig(car1, fill = 'blue')

def left(event):
	global a 
	a = 1
	print 'left'
	#while a == 1:
	canv.move(car1, 2, 0)
	#time.sleep(.1)
	print 'here'
	
	
def stop(event):
	global a 
	a = 0
	print 'stop'
	#while a == 0:
	#while True:
	canv.move(car1, -1, 0)
		#time.sleep(1)
		#print 'not'
		
canv.bind('<Button-1>', click)
win.bind('<d>',left)
#win.bind('<KeyRelease-d>',stop)
'''
