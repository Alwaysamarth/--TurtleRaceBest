from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color :")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
race_on=False

for turtle_index in range(0,6):
   new_turtle=Turtle(shape="turtle")
   new_turtle.penup()
   new_turtle.goto(x=-230,y=y_positions[turtle_index])
   new_turtle.color(colors[turtle_index])
   all_turtles.append(new_turtle)
  
if user_bet:
   race_on=True
while race_on:
  for turtle in all_turtles:
    if turtle.xcor()>230:
      winning = turtle.pencolor()
      if winning == user_bet:
        print(f"You've won! The {winning} turtle is the winner!")
        race_on=False
      else:
        print(f"You've lost. The {winning} turtle is the winner!")
        race_on=False
    random_distance=random.randint(0,10)
    turtle.forward(random_distance)
  
screen.exitonclick()