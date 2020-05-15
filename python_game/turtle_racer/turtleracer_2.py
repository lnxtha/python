import turtle
import time
import random
import os


screen = turtle.Screen()
screen.bgcolor('green')
screen.title('Turtle Racer')
screen.setup(width = 800,height = 600)

screen.tracer(0,10)


# For controlling dx in turtles and displaying result
flag1 = True
flag2 = True
flag3 = True
flag4 = True
flag5 = True

started = True


# For displaying result, (postion variable)
posn = 0

turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle1.penup()
turtle1.shapesize(stretch_wid = 1, stretch_len = 1)
turtle1.dx = 0

turtle1.shape("turtle")
turtle1.color("black")


turtle2 = turtle.Turtle()
turtle2.speed(0)
turtle2.penup()
turtle2.shapesize(stretch_wid = 1, stretch_len = 1)
turtle2.dx = 0

turtle2.shape("turtle")
turtle2.color("orange")


turtle3 = turtle.Turtle()
turtle3.speed(0)
turtle3.penup()
turtle3.shapesize(stretch_wid = 1, stretch_len = 1)
turtle3.dx = 0

turtle3.shape("turtle")
turtle3.color("red")


turtle4 = turtle.Turtle()
turtle4.speed(0)
turtle4.penup()
turtle4.shapesize(stretch_wid = 1, stretch_len = 1)
turtle4.dx = 0

turtle4.shape("turtle")
turtle4.color("pink")


turtle5 = turtle.Turtle()
turtle5.speed(0)
turtle5.penup()
turtle5.shapesize(stretch_wid = 1, stretch_len = 1)
turtle5.dx = 0

turtle5.shape("turtle")
turtle5.color("blue")


finish_line = turtle.Turtle()
finish_line.shape("square")
finish_line.penup()
finish_line.goto(300,100)
finish_line.shapesize(stretch_wid = 13, stretch_len = 1)

finish_line.color("white")


turtle1.goto(-300,200)
turtle2.goto(-300,150)
turtle3.goto(-300,100)
turtle4.goto(-300,50)
turtle5.goto(-300,0)

turtle1.pendown()
turtle2.pendown()
turtle3.pendown()
turtle4.pendown()
turtle5.pendown()



#score
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(340,250)

score.write("Position!!",align="center",font=("Courier",12,"normal"))		

score.hideturtle()


#score 1
score1 = turtle.Turtle()
score1.speed(0)
score1.penup()
score1.color("white")
score1.goto(340,200)

score1.write("0",align="center",font=("Courier",12,"normal"))

score1.hideturtle()		

#score 2


score2 = turtle.Turtle()
score2.speed(0)
score2.penup()
score2.color("white")
score2.goto(340,150)

score2.write("0",align="center",font=("Courier",12,"normal"))	

score2.hideturtle()	

# score 3
score3 = turtle.Turtle()
score3.speed(0)
score3.penup()
score3.color("white")
score3.goto(340,100)

score3.write("0",align="center",font=("Courier",12,"normal"))	

score3.hideturtle()	

# score 4
score4 = turtle.Turtle()
score4.speed(0)
score4.penup()
score4.color("white")
score4.goto(340,50)

score4.write("0",align="center",font=("Courier",12,"normal"))	

score4.hideturtle()

# score 5
score5 = turtle.Turtle()
score5.speed(0)
score5.penup()
score5.color("white")
score5.goto(340,0)

score5.write("0",align="center",font=("Courier",12,"normal"))	

score5.hideturtle()	


# dashboard

dashboard = turtle.Turtle()
dashboard.speed(0)
dashboard.penup()
dashboard.color("red")
dashboard.goto(0,-100)

dashboard.hideturtle()

# Setting Initial Position:
def reset():

	global flag1
	global flag2
	global flag3
	global flag4
	global flag5
	
	global posn
	
	global started

	# For controlling dx in turtles and displaying result
	flag1 = True
	flag2 = True
	flag3 = True
	flag4 = True
	flag5 = True

	# For displaying result, (postion variable)
	posn = 0

	# For ready, set, go
	started = True


	dashboard.clear()
	dashboard.color("white")
	dashboard.write("Resetting...",align="center",font=("Courier",20,"normal"))	
	time.sleep(1)

	turtle1.clear()
	turtle2.clear()
	turtle3.clear()
	turtle4.clear()
	turtle5.clear()		

	turtle1.penup()
	turtle2.penup()
	turtle3.penup()
	turtle4.penup()
	turtle5.penup()
	
	#Initial Postion
	turtle1.setx(-300)
	turtle2.setx(-300)
	turtle3.setx(-300)
	turtle4.setx(-300)
	turtle5.setx(-300)

	turtle1.pd()
	turtle2.pd()
	turtle3.pd()
	turtle4.pd()
	turtle5.pd()

	dashboard.clear()
	dashboard.color("white")
	dashboard.write("Turtles set to position...",align="center",font=("Courier",20,"normal"))	

	screen.update()	
	time.sleep(1.75)
		
	score1.clear()
	score2.clear()
	score3.clear()
	score4.clear()
	score5.clear()

	score1.pu()
	score2.pu()
	score3.pu()
	score4.pu()
	score5.pu()
	
	score1.write(str(posn),align="center",font=("Courier",12,"normal"))
	score2.write(str(posn),align="center",font=("Courier",12,"normal"))
	score3.write(str(posn),align="center",font=("Courier",12,"normal"))
	score4.write(str(posn),align="center",font=("Courier",12,"normal"))
	score5.write(str(posn),align="center",font=("Courier",12,"normal"))

	score1.pd()
	score2.pd()
	score3.pd()
	score4.pd()
	score5.pd()

	dashboard.clear()
	dashboard.color("white")
	dashboard.write("Scores Reset...",align="center",font=("Courier",20,"normal"))	

	screen.update()	
	time.sleep(1.75)

	# For ready, set, go
	dashboard.color("red")

	


# Setting Turtle Speed:

def run():

	global flag1
	global flag2
	global flag3
	global flag4
	global flag5

	global posn


	if turtle1.xcor() >= 270 and flag1:
		posn += 1
		turtle1.setx(270)
		
		score1.clear()
		score1.color("black")
		score1.write(str(posn),align="center",font=("Courier",20,"normal"))	
		score1.penup()
		flag1 = False		
	
	if turtle2.xcor() >= 270 and flag2:
		posn += 1
		turtle2.setx(270)
		
		score2.clear()
		score2.color("orange")
		score2.write(str(posn),align="center",font=("Courier",20,"normal"))
		
		flag2 = False	

	if turtle3.xcor() >= 270 and flag3:

		posn += 1
		turtle3.setx(270)

		score3.clear()
		score3.color("red")
		score3.write(str(posn),align="center",font=("Courier",20,"normal"))
		
		flag3 = False	

	if turtle4.xcor() >= 270 and flag4:

		posn += 1
		turtle4.setx(270)

		score4.clear()
		score4.color("pink")
		score4.write(str(posn),align="center",font=("Courier",20,"normal"))

		flag4 = False	


	if turtle5.xcor() >= 270 and flag5:

		posn += 1
		turtle5.setx(270)

		score5.clear()
		score5.color("blue")
		score5.write(str(posn),align="center",font=("Courier",20,"normal"))	

		flag5 = False

def speed():
	
	values = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,13]
	random.shuffle(values)	
	
	turtle1.dx = random.choice(values)
	turtle2.dx = random.choice(values)
	turtle3.dx = random.choice(values)
	turtle4.dx = random.choice(values)
	turtle5.dx = random.choice(values)

# Moving turtle
def move_turtle():
	if flag1:	
		turtle1.setx(turtle1.xcor()+turtle1.dx)
	if flag2:
		turtle2.setx(turtle2.xcor()+turtle2.dx)
	if flag3:
		turtle3.setx(turtle3.xcor()+turtle3.dx)
	if flag4:	
		turtle4.setx(turtle4.xcor()+turtle4.dx)
	if flag5:	
		turtle5.setx(turtle5.xcor()+turtle5.dx)

	turtle1.pendown()
	turtle2.pendown()
	turtle3.pendown()
	turtle4.pendown()
	turtle5.pendown()

	dashboard.clear()

def ready_set_go():

	

	global started
	
	if (started):	

		dashboard.clear()
		dashboard.write("Ready? Press Enter...",align="center",font=("Courier",20,"normal"))	

		screen.update()

		raw_input("Press enter to continue...")
		started = False
		time.sleep(1)

		dashboard.clear()

		dashboard.color("yellow")
		dashboard.write("Set",align="center",font=("Courier",20,"normal"))

		screen.update()
		time.sleep(1.5)


		dashboard.clear()

		dashboard.color("purple")
		dashboard.write("Go !!!",align="center",font=("Courier",20,"normal"))	

		screen.update()
		time.sleep(1.5)
		dashboard.clear()
			

# Program starts here


#Main game
while True:
	ready_set_go()
	screen.tracer(0)		
	screen.update()	

	speed()
	
	move_turtle()	

	time.sleep(.15)	

	#ready_set_go()
	run()
	
	if turtle1.xcor() >= 270 and turtle2.xcor() >= 270 and turtle3.xcor() >= 270 and turtle4.xcor() >= 270 and turtle5.xcor() >= 270 :


		dashboard.clear()

		dashboard.color("yellow")
		dashboard.write("Race concluded !!",align="center",font=("Courier",20,"normal"))

		screen.update()
		time.sleep(1.5)

		dashboard.clear()

		dashboard.color("yellow")
		dashboard.write("Want to Race again...?",align="center",font=("Courier",20,"normal"))

		screen.update()
		time.sleep(1.5)

		dashboard.clear()

		dashboard.color("blue")
		dashboard.write("Press 'y' to race again.",align="center",font=("Courier",20,"normal"))

		screen.update()
		time.sleep(1.5)

		dashboard.color("blue")

		dashboard.clear()
		dashboard.write("Anything else to exit...",align="center",font=("Courier",20,"normal"))

		screen.update()
		time.sleep(1)

		
		race_again = raw_input("Press 'y' to race again\n")	
		if race_again == 'y':
			reset()
			screen.update()

			continue
		else:
			break	
	

	


	
		


	

