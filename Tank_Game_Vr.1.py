from Tkinter import *
import time, math, random, winsound



win = Tk()

XLimit = 1300
YLimit = 500

canv = Canvas(win, height = YLimit, width = XLimit, bg = 'light blue')
canv.pack()


BoxSize = 10
BoxColor = 'white'
GroundLevel = 30
inputGL = YLimit - GroundLevel 
speed = 3
fps = 15
Niddle = 30
ang = 120
Gforce = .0098
BoxFat = 5
FirePower = 2
BullSize = 5
BullColor = 'red'
BulletKind = 'cannon'

Bullet_X = 0
Bullet_Y = 0


RandomBox = []
RandPick = []

for i in range(0,80,5):
	RandomBox.append(i)
for i in range(-70,0,5):
	RandomBox.append(i)
print RandomBox


GroundLine = canv.create_line(0,inputGL, XLimit,inputGL, fill = 'brown', width = 2) 

# initial box loc
BoxLocX = 60
BoxLocY = 0

# Target Loc
targetX = 700
targetY = 0


NiddleOrigX, NiddleOrigY = BoxLocX , BoxLocY




def fire ():
	global FirePower, angADJ, AA, NiddleOrigX, NiddleOrigY, BullSize, BullColor, fps, BulletKind
	
	winsound.Beep(130,200)
	print FirePower, angADJ, FirePower
	
	
	
	
	if BulletKind == 'fireball': BullColor, BullSize = 'red', 5
	elif BulletKind == 'jagerbomb': BullColor, BullSize = 'green', 9
	elif BulletKind == 'b151': BullColor, BullSize = 'yellow', 14
	elif BulletKind == 'stella' : BullColor, BullSize = 'white', 5
	elif BulletKind == 'cannon': BullColor, BullSize = 'black', 5
	
	
	XForce =  FirePower * math.sin(math.radians(angADJ))
	YForce =  FirePower * math.cos(math.radians(angADJ))
	
	Bullet_X = NiddleOrigX
	Bullet_Y = NiddleOrigY
	print XForce, YForce
	
	illumi = 0
	AA = 0
	print Bullet_Y, inputGL
	
	while Bullet_Y <= inputGL:
		Bullet_X = Bullet_X + XForce
		YForce = YForce - Gforce
		Bullet_Y = Bullet_Y - YForce
		
		x1,y1,x2,y2 = Bullet_X - BullSize, Bullet_Y - BullSize, Bullet_X + BullSize, Bullet_Y + BullSize
		if BulletKind == 'stella': 
			if illumi < 10: BullSize, BullColor = 10, 'yellow'
			elif illumi >= 10 and illumi < 20: BullSize, BullColor = 5, 'white'
			elif illumi >= 20: illumi = 0
			illumi += 1
		canv.create_oval(x1,y1,x2,y2, fill = BullColor, outline = BullColor, tags = 'bullet')
		
		
		
		time.sleep(.005)
		canv.update()
		canv.delete('bullet')
		#print Bullet_X, Bullet_Y
	AA = 1
	explosion(Bullet_X, Bullet_Y)

	
def explosion (x,y):
	global BulletKind, BullColor
	mag = 0
	a = 0
	x1, y1, x2, y2 = x, y, x, y
	Leng = 1
	# qq =ww =ee =rr =tt =yy = 0
	# for II in qq,ww,ee,rr,tt,yy:
		# II = random.choice(RandomBox)
		
	print BulletKind
		
	if BulletKind == 'fireball': mag = 1
		#SparkThread = threading.Thread( target = winsound.Beep(120,2000))
		#SparkThread.start()	
	elif BulletKind == 'jagerbomb': mag = .9
	elif BulletKind == 'b151': mag = 2
	elif BulletKind == 'cannon': mag = .3
	elif BulletKind == 'stella': mag = 0
	
	
	while a <= 800: 
		a += 2
		if a < 400:
			
			x1 += .2* mag
			y1 += .15* mag
			x2 -= .2* mag
			y2 -= .15* mag
			Leng += .3* mag
			canv.delete('arc')		
			#for Leng in range(1,60,0.05):	
		else:
			
			x1 -= .2* mag
			y1 -= .15* mag
			x2 += .2* mag
			y2 += .15* mag
			Leng -= .3* mag
			canv.delete('arc', 'spark')
			
		Lx = x + Leng* math.sin(math.radians(random.choice(RandomBox)))
		Ly = y - Leng* math.cos(math.radians(random.choice(RandomBox)))
		
		canv.create_arc(x1, y1, x2, y2, start = 5, extent = 170, outline = BullColor, fill = BullColor, tags = 'arc')
		#FireBall Spark
		if BulletKind == 'fireball': 
			canv.create_line(x,y,Lx,Ly, fill = 'yellow', tags = 'spark', width = 1)
			
			#winsound.Beep(120,3)
		
		canv.update()
		time.sleep(.001)	
	canv.delete('arc', 'spark')
	



def wherebox (x,y):
	global inputGL, BoxSize, BoxLocX, BoxLocY, AA
	
	while AA == 1:
	#while 1:
		boxX = BoxLocX
		boxY = inputGL - BoxSize - BoxLocY - 2
		
		boxdiaplay(boxX, boxY)
		time.sleep(float(1/fps))
		

def boxdiaplay (x,y):
	global BoxSize, BoxColor, ang, NiddleOrigX, NiddleOrigY, Niddle, BoxFat, angADJ

	BoxLeft, BoxRight = x - BoxSize - BoxFat, x + BoxSize + BoxFat
	BoxTop, BoxBottom =  y - BoxSize, y + BoxSize
	
	x1, y1, x2, y2 =  BoxLeft, BoxTop, BoxRight, BoxBottom
	canv.create_rectangle(x1,y1,x2,y2, fill = BoxColor, outline = BoxColor, tags = 'box')
	
	NiddleOrigX = x
	NiddleOrigY = y
	angADJ = ang - 90
	XNiddle = NiddleOrigX + Niddle * math.sin(math.radians(angADJ))
	YNiddle = NiddleOrigY - Niddle * math.cos(math.radians(angADJ))
	
	canv.create_line(NiddleOrigX, NiddleOrigY, XNiddle, YNiddle,  tags = 'niddle', fill = 'black', arrow = 'last')

	
	
	canv.update()
	canv.delete('box', 'niddle')
	
	#print XNiddle, YNiddle

def where(event):
	global BoxLocX, BoxLocY, BoxSize, speed, XLimit, YLimit, inputGL, ang, BulletKind, FirePower
	
	#print event.x, event.y
	if event.keysym == "Left":
		if BoxLocX >= BoxSize + 3:BoxLocX = float(BoxLocX - speed)
	elif event.keysym == 'Right':
		if BoxLocX <= XLimit - BoxSize - 2:BoxLocX = float(BoxLocX + speed)
	elif event.keysym == "Down":
		if BoxLocY >= 1: BoxLocY = float(BoxLocY - speed)
	elif event.keysym == 'Up':
		if BoxLocY <= inputGL - BoxSize *2 - 4: BoxLocY = float(BoxLocY + speed)
	elif event.keysym == 'E' or event.keysym =='e':
		if ang <= 179: ang += 2
	elif event.keysym == 'W' or event.keysym =='w':
		if ang >= 1: ang -= 2
	elif event.keysym == 's' or event.keysym =='S':
		if FirePower > .5: FirePower -= .1
	elif event.keysym == 'd' or event.keysym =='D':
		if FirePower < 3: FirePower += .1	
	elif event.keysym == 'F' or event.keysym =='f':fire()
	
	elif event.keysym == '1' : BulletKind = 'cannon'
	elif event.keysym == '2' : BulletKind = 'stella'
	elif event.keysym == '3' : BulletKind = 'jagerbomb'
	elif event.keysym == '4' : BulletKind = 'b151'
	elif event.keysym == '5' : BulletKind = 'fireball'
	
	
	
	#print BoxLocX, BoxLocY	
# explosionTH = threading.Thread( target = explosion(Bullet_X, Bullet_Y))
# sparkTH = threading.Thread( target = winsound.Beep(120,2000))
'''
def keypres (event):
	if event.chr = 'Left'
'''
	
win.bind("<Key>", where)

AA = 1
wherebox(BoxLocX, BoxLocY)
win.mainloop()
