from turtle import Turtle, Screen, textinput, numinput, time, bye
import random
import math

width = 1000
height = 800
screen = Screen()
screen.title("Python 1D Game")
screen.bgcolor("black")
screen.setup(width, height)
screen.tracer(3)

cannon = Turtle("circle")
cannon.fillcolor("yellow")
cannon.penup()
    
target = Turtle("square")
target.fillcolor("red")
target.penup()

text = Turtle("circle")
text.fillcolor("white")
text.color("white")
text.hideturtle()

stats = Turtle()
stats.fillcolor("white")
stats.color("white")
stats.hideturtle()
stats.penup()
stats.setpos(250, 350)

line = Turtle()
line.color('grey')
line.hideturtle()
line.penup()

star = Turtle()
star.color('yellow')
star.hideturtle()

objects = [star, line, stats, text, target, cannon]
   


####functions here lah deh


#   finding the closest distance
def closest_distance(x, y, x_point, y_point):
    return math.sqrt(((x - x_point)**2) + (y - y_point)**2)

#   drawing of yellow star
def draw_stars(x):
    #   set draw speed
    #screen.tracer(0)

    if x == 1:
        # draw first star
        star.penup()
        star.setpos(-30,100)
        star.pendown()
        star.begin_fill()
        for i in range(5):
            star.fd(60)
            star.right(144)
        star.end_fill()

    elif x == 2:
        # draw first star
        star.penup()
        star.setpos(-65,100)
        star.pendown()
        star.begin_fill()
        for i in range(5):
            star.fd(60)
            star.right(144)
        star.end_fill()

        # draw second star
        star.penup()
        star.setpos(5,100)
        star.pendown()
        star.begin_fill()
        for i in range(5):
            star.fd(60)
            star.right(144)
        star.end_fill()
        

    elif x == 3: 
        # draw first star
        star.penup()
        star.setpos(-100,100)
        star.pendown()
        star.begin_fill()
        for i in range(5):
            star.fd(60)
            star.right(144)
        star.end_fill()

        # draw second star
        star.penup()
        star.setpos(-30,100)
        star.pendown()
        star.begin_fill()
        for i in range(5):
            star.fd(60)
            star.right(144)
        star.end_fill()

        # draw third star
        star.penup()
        star.setpos(40,100)
        star.pendown()
        star.begin_fill()
        for i in range(5):
            star.fd(60)
            star.right(144)
        star.end_fill()
    else:
        text.penup()
        text.goto(0,100)
        text.pendown()
        text.write(f"You Suck!\nLOL\nWHAT A PROJECTILE MOTION NUBBB", align = "center",  font=("Cooper Black", 15, "italic"))

    #time.sleep(1)

#   num of stars to draw
def how_many_stars(dist):
    if dist < 50:
        draw_stars(3)
    elif dist < 120:
        draw_stars(2)
    elif dist < 300:
        draw_stars(1)
    else:
        draw_stars(0)

#   grid background
def draw_grid(x, y):
    #draw verticle lines
    for a in range(int(-x),int(x+1),50):
        line.setpos(a,-y)
        line.pendown()
        line.setpos(a,y)
        line.penup()

    for b in range(int(-y),int(y+1),50):
        line.setpos(-x,b)
        line.pendown()
        line.setpos(x,b)
        line.penup()

#   optimising projectile coordinates
def relative_coordinates(x,sx):
    output = sx - x
    return output

#   welcome prompt
def welcome_text():
    prompt_1 = 'Would you like to play?\nY/N'
    wanna_play = str.lower(textinput(title= "Welcome!",prompt = prompt_1 ))
    return wanna_play

#   main code
def run_game():
    
    
    #   setting of objects
    #   cannon
    x_startcannon = -450
    y_startcannon = random.randint(-390, 0)

    #   target
    x_target = 450
    y_target = random.randint(-390, 300)

    #   calculate distances
    x_distance = x_target - x_startcannon
    y_distance = abs(y_target - y_startcannon)

    #   draw grid
    draw_grid(width/2, height/2)

    #   Initialise cannon and target
    cannon.setpos(x_startcannon, y_startcannon)
    target.setpos(x_target, y_target)
    time.sleep(1)

    #Printing the instructions  
    #   def instructions(x,y):
    text.penup()
    text.setpos(-450, 300)
    text.write(f"The horizontal distance is {x_distance}m.\nThe vertical distance is {y_distance}m.", font=("Cooper Black", 15, "italic"))
    time.sleep(1)

    #Gather inputs on velocity and angle    def updated_instructions(x,y):

    u = int(numinput(":Launch velocity", "Velocity (m/s)\nEnter from 1 to 100"))
    u_angle = int(numinput("Launch angle relative to ground", "Angle (Degrees)" ))
    u_angle_radian = u_angle * math.pi / 180
    ux = u * math.cos(u_angle_radian)
    uy = u * math.sin(u_angle_radian)
    text.clear()
    text.setpos(-450, 250)
    text.write(f"The horizontal distance is {x_distance}m.\nThe vertical distance is {y_distance}m.\nInitial velocity: {u}m/s.\nLaunch angle: {u_angle} degrees.", move = False, align = "Left", font=("Cooper Black", 15, "italic"))
    
#def draw_path():
    #Drawing the trajectory path
    t = 0
    sx = 0
    sy = 0
    g = 9.81
    y = 0

    distance = []

        #equation of trajectory and calculation of closest distance
    while abs(sx) < 500 and -340 < sy < 500:
        sx = ux * t + x_startcannon
        sy = (uy * t) - ((g/2) * t**2) + y_startcannon
        t += 0.1
        y += 1

        #show coordinates of projectile
        stats.clear()
        stats.write(f"Projectile({int(sx)},{int(sy)})",font=("Cooper Black", 10, "italic"))

        close_dist = cannon.distance(target.pos())
        distance.append(close_dist)

#drawing of trajectory
#   def traj_tracer(y)
        if sx % 2 == 0:
            cannon.pendown()
            cannon.pencolor("white")
        else:
            cannon.penup()
    
        time.sleep(0.05)
        screen.update()
        
        cannon.goto(sx, sy)

        if sy < -400 or sx > 500 or sy> 430 or sx <-500:
            break

        minimum_distance = min(distance)
    cannon.penup()
    

    how_many_stars(minimum_distance)
    print('hi')
    time.sleep(2)
    end_screen_text()



#   def play_game():
    if welcome_text() == 'y':
        run_game()
        reply = end_screen_text()
        while reply == 'y':
            run_game()
            reply = end_screen_text()
    bye()

#   play again screen
def end_screen_text():
    print('dicks')
    x = 'Would you still like to play?\nY/N'
    play_again = str.lower(textinput(title= "Thanks for playing!",prompt = x ))
    if play_again == 'y':
        for i in objects:
            print(i)
            i.clear()
        
        run_game()
    else:
        bye()


def play_game():
    if welcome_text() == 'y':
        run_game()
    else:
        bye()
        
   




play_game()

