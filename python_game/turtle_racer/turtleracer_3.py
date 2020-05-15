import turtle
import time
import random
import os

screen = turtle.Screen()
screen.bgcolor('grey')
screen.title('Turtle Racer')
screen.bgpic("screenshot.png")
screen.setup(width = 900,height = 600)

screen.tracer(0,10)

no_of_turtle = 100
while (no_of_turtle > 10):
	no_of_turtle = int(raw_input('How many turtles?\n'))
	if no_of_turtle > 10:
		print('Ten is the limit. Please try again!!')
		no_of_turtle = int(raw_input('How many turtles?\n'))	
	

position = turtle.Turtle()
finish_line = turtle.Turtle()
dashboard = turtle.Turtle()


colors = ['coral','red','yellow','beige','orange','pink','green','black','teal','gold']
name_list = ['Franklin','Leonardo','Squirt','Michel-angelo','Bulldozer','Peek-a-boo','Donatello','Pokey','Shell-Shocker','Gamera']


# For controlling dx in turtles and displaying result

flags = []

for i in range(no_of_turtle):
	flags.append(True)

#Bool value
started = True


# For displaying result, (postion variable)
posn = 0

# Turtle Body


turtles = []
scores = []
names = []

for t in range(no_of_turtle):

	start_xvalue = -300
	start_yvalue = 200
	
	score_xvalue = 340
	score_yvalue = 200

	name_xvalue = -375
	name_yvalue = 200

	turtles = turtles + [turtle.Turtle()]
	scores = scores + [turtle.Turtle()]
	names = names + [turtle.Turtle()]
	
#chosen_color
chosen_color = []
chosen_name = []

for index, turtle in enumerate(turtles):

	color = random.choice(colors)
	colors.remove(color)
	chosen_color.append(color)

	name = random.choice(name_list)
	name_list.remove(name)
	chosen_name.append(name)

	turtle.speed(0)
	turtle.penup()
	turtle.shapesize(stretch_wid = 1, stretch_len = 1)
	turtle.dx = 0

	turtle.goto(start_xvalue,start_yvalue)
	turtle.pendown()

	turtle.shape("turtle")
	turtle.color(color)

	start_yvalue = start_yvalue - 50


#position = turtle.Turtle()

position.speed(0)
position.penup()
position.color("white")
position.goto(340,250)

position.write("Position!!",align="center",font=("Courier",12,"normal"))		

position.hideturtle()

	
#score

for index, score in enumerate(scores):
	
	score.speed(0)
	score.penup()	
	score.color(chosen_color[index])
	score.goto(score_xvalue,score_yvalue)
	score.write("0",align="center",font=("Courier",12,"normal"))
	score.hideturtle()

	score_yvalue = score_yvalue - 50

for index, name in enumerate(names):
	
	name.speed(0)
	name.penup()	
	name.color(chosen_color[index])
	name.goto(name_xvalue,name_yvalue)
	name.write(chosen_name[index],align="center",font=("Courier",12,"normal"))
	name.hideturtle()

	name_yvalue = name_yvalue - 50

		
#Finish Line


finish_line.shape("square")
finish_line.penup()
finish_line.goto(300,230)
finish_line.pd()
finish_line.width(10)

finish_line.color("white")


finish_line.right(90)
finish_line.forward(50*no_of_turtle)
finish_line.shapesize(stretch_len = 1)


finish_line.pu()
finish_line.hideturtle()


# dashboard


dashboard.speed(0)
dashboard.penup()
dashboard.color("red")
dashboard.goto(0,-100)

dashboard.hideturtle()


# Setting Initial Position:
def reset():

	global posn	
	global started

	# For displaying result, (postion variable)
	posn = 0

	# For ready, set, go
	started = True

	# For controlling dx in turtles and displaying result		
	
	for i in range(no_of_turtle):
		flags[i] = False

	dashboard.clear()
	dashboard.color("white")
	dashboard.write("Resetting...",align="center",font=("Courier",20,"normal"))	
	time.sleep(1)

	for i in range(no_of_turtle):
		turtles[i].clear()
		turtles[i].penup()

		#Initial Postion
		turtles[i].setx(-300)
		
		turtles[i].pd()
	
	dashboard.clear()
	dashboard.color("white")
	dashboard.write("Turtles set to position...",align="center",font=("Courier",20,"normal"))	

	screen.update()	
	time.sleep(1.75)
	

	for i in range(no_of_turtle):	
		scores[i].clear()
		scores[i].pu()
		scores[i].write(str(posn),align="center",font=("Courier",12,"normal"))
		scores[i].pd()
	
	dashboard.clear()
	dashboard.color("white")
	dashboard.write("Scores Reset...",align="center",font=("Courier",20,"normal"))	

	screen.update()	
	time.sleep(1.75)

	# For ready, set, go
	dashboard.color("red")

	
# Setting Turtle Speed:

def run():

	global posn

	for i in range(no_of_turtle):
		if turtles[i].xcor() >= 280 and flags[i]:
			posn += 1
			turtles[i].setx(280)
			
			scores[i].clear()
			scores[i].color(chosen_color[i])
			scores[i].write(str(posn),align="center",font=("Courier",20,"normal"))	
			scores[i].penup()
			flags[i] = False		
		
def speed():
	
	values = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,13]
	random.shuffle(values)	
	for i in range(no_of_turtle):
		turtles[i].dx = random.choice(values)
	
# Moving turtle
def move_turtle():
	for i in range(no_of_turtle):
		if flags[i]:	
			turtles[i].setx(turtles[i].xcor()+turtles[i].dx)

		turtles[i].pendown()
		turtles[i]

	dashboard.clear()

def ready_set_go():

	global started
	
	if (started):	

		dashboard.clear()
		dashboard.write("Ready? Press Enter...",align="center",font=("Courier",20,"normal"))
		
		

		screen.update()

		raw_input("Press enter to continue...")
	
		# Ready Set Go Sound		
		os.system("aplay ready_set_go.wav&")	

		started = False
		time.sleep(1)

		dashboard.clear()

		dashboard.color("yellow")
		dashboard.write("Set",align="center",font=("Courier",20,"normal"))

		screen.update()
		time.sleep(1.5)


		dashboard.clear()

		dashboard.color("green")
		dashboard.write("GO !!!",align="center",font=("Courier",20,"normal"))	

		screen.update()
		time.sleep(1.5)
		dashboard.clear()

		# Ready Set Go Sound		
		os.system("aplay racing_sound.wav&")
			

# Program starts here



#Main game
while True:
	ready_set_go()
	screen.tracer(0)		
	screen.update()	

	speed()
	
	move_turtle()	

	# Game speed
	time.sleep(.1)	

	

	#ready_set_go()
	run()

	program_end = False

	for i in range(no_of_turtle):
		
		if turtles[i].xcor() >= 280:
			flags[i] = False
		else:
			flags[i] = True
	
	if True in flags:
		program_end = False
	else:
		program_end = True

	if (program_end):

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

		dashboard.color("yellow")
		dashboard.write("Press 'y' to race again.",align="center",font=("Courier",20,"normal"))

		screen.update()
		time.sleep(1.5)

		dashboard.color("yellow")

		dashboard.clear()
		dashboard.write("Anything else to exit...",align="center",font=("Courier",20,"normal"))

		screen.update()


		
		race_again = raw_input("Press 'y' to race again\n")	
		if race_again == 'y':
			reset()
			screen.update()

			continue
		else:
			break	





		
			


	

