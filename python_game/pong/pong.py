import turtle
import time
import random
import os


print('Hello');

we = turtle.Screen()
we.bgcolor('black')
we.title('Pong')
we.setup(width = 800,height = 600)
we.tracer(0)


player1_score = 0
player2_score = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)

#Ball
ball = turtle.Turtle()
ball.goto(0,0)
ball.penup()
ball.shapesize(stretch_wid = 1, stretch_len = 1)
ball.color("white")
ball.shape("circle")
ball.speed(0)
ball.dx = 20
ball.dy = 20

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.goto(0,260)
pen.hideturtle()

#score
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(0,0)

score.hideturtle()



#Function

def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

def reset():
	paddle_a.sety(0)
	paddle_b.sety(0)
	
	ball.setx(0)
	ball.sety(0)
	
	#Change direction of ball with each reset.
	values = [1,-1]
		
	ball.dx*= random.choice(values)
	ball.dy*= random.choice(values)

	ball.clear()

	#speed = [0.1, 0.15, 0.2, 0.25, 0.3]	



#Keyboard binding
we.listen()
we.onkey(paddle_a_up, 'w')
we.onkey(paddle_a_down, 's')
we.onkey(paddle_b_up, 'Up')
we.onkey(paddle_b_down, 'Down')

#Main game
while True:
	
	
	we.update()
	
	time.sleep(0.2)	

	pen.write("Scores:: Player 1 -> {0} Player 2 -> {1}".format(player1_score,player2_score),align="center",font=("Courier",24,"normal"))

#Move the ball
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)
	
	
	# Case of ball bouncing in upper or lower surface
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy*=-1
		os.system("aplay bounce.wav&")
		#os.system("aplay baseball-hitting-bat.wav&")

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy*=-1
		os.system("aplay bounce.wav&")
		
	# Case of ball bouncing in upper or lower surface


#Player 2 border (RIGHT SIDE)	
	if ball.xcor() > 390:
		ball.setx(390)
		ball.goto(0,0)
		
		time.sleep(1)
			
		score.clear()
		score.write("Ball moves out of court.",align="center",font=("Courier",12,"normal"))
		time.sleep(1)

		print('Ball moves out of the court!!')		

		score.goto(0,-30)
		score.write("Player 1 scores!!",align="center",font=("Courier",12,"normal"))
		score.goto(0,0)
		
		player1_score += 1

		pen.clear()
		pen.write("Scores:: Player 1 -> {0} Player 2 -> {1}".format(player1_score,player2_score),align="center",font=("Courier",24,"normal"))
		time.sleep(1)
		
		score.clear()
		
		reset()
		
		score.clear()
		score.write("Ready? ",align="center",font=("Courier",24,"normal"))
		time.sleep(1)		
		
		score.clear()
		score.write("Go! ",align="center",font=("Courier",24,"normal"))
		time.sleep(1)
		score.clear()

#Player 1 border (LEFT SIDE)
	if ball.xcor() < -390:
		ball.setx(-390)
		ball.dx*=-1
		ball.goto(0,0)
		
		time.sleep(1)
		
		score.clear()
		score.write("Ball moves out of court.",align="center",font=("Courier",12,"normal"))

		print('Ball moves out of the court!!')		

		time.sleep(1)

		score.goto(0,-30)
		score.write("Player 2 scores!!",align="center",font=("Courier",12,"normal"))
		score.goto(0,0)		

		player2_score += 1

		pen.clear()
		pen.write("Scores:: Player 1 -> {0} Player 2 -> {1}".format(player1_score,player2_score),align="center",font=("Courier",24,"normal"))
		time.sleep(1)
		
		
		reset()
		ball.goto(0,0)
		
		score.clear()
		score.write("Ready? ",align="center",font=("Courier",24,"normal"))
		time.sleep(1)		
		
		score.clear()
		score.write("Go! ",align="center",font=("Courier",24,"normal"))
		score.clear()	

		time.sleep(1)
	


	if (ball.xcor() > 340 and ball.ycor() <= paddle_b.ycor()+40 and ball.ycor() >= paddle_b.ycor()-40):
		ball.setx(340)
		ball.sety(ball.ycor())
		ball.dx*=-1
		print('ball hit the pad')
		os.system("aplay bounce.wav&")
		
		
	
	if (ball.xcor() < -340 and ball.ycor() <= paddle_a.ycor()+40 and ball.ycor() >= paddle_a.ycor()-40):
		ball.setx(-340)
		ball.sety(ball.ycor())
		ball.dx*=-1	
		print('ball hit the pad')
		os.system("aplay bounce.wav&")

		
	print('Ball (x,y): '+str(ball.xcor())+ ',' + str(ball.ycor()))	
	print('Paddle_B (x,y): '+str(paddle_a.xcor())+ ',' + str(paddle_a.ycor()))	
	
	
	
	
