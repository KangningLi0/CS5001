"""
Kangning Li
CS 5001 2024 Spring
Programming problem #1
"""

import turtle
import math

  
class PositionService:
    singleton = None
    
    def __init__(self): 
        self.x = 0
        self.y = 0
        self.visible = True
  
    # a class method to create a Person object by birth year. 
    @classmethod
    def get_instance(cls):
        if PositionService.singleton == None:
            PositionService.singleton = PositionService()
        return PositionService.singleton

# non OO service api

def set_position_x( x ):
    instance = PositionService.get_instance()
    instance.x = x

def set_position_y( y ):
    instance = PositionService.get_instance()
    instance.y = y

def set_position(x, y):
    instance = PositionService.get_instance()
    instance.x = x
    instance.y = y
    
def get_position_x():
    instance = PositionService.get_instance()
    return instance.x

def get_position_y():
    instance = PositionService.get_instance()
    return instance.y

def is_visible():
    instance = PositionService.get_instance()
    return instance.visible

def set_visible( visibility ):
    instance = PositionService.get_instance()
    instance.visible = visibility

# the function to draw circle at position (x,y)
def draw_circle(x, y):
    global last_draw_x, last_draw_y
    turtle.penup()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor("green")
    turtle.circle(80)
    turtle.penup()
    turtle.home()
    last_draw_x = x
    last_draw_y = y
    
# the global variables to help save the last_drawing data
last_draw_x = 0
last_draw_y = 0
is_draw = True;

# the function logic to finish the process
def hello_world(x, y):
    global is_draw
    if (math.sqrt((last_draw_x - x) ** 2 +
                  (last_draw_y - y) ** 2) < 80
        and is_draw):
        is_draw = False;
        turtle.clear()
    elif (not is_draw):
        is_draw = True;
        draw_circle(x, y)
        

def main():
    screen = turtle.Screen()
    turtle.screensize(968, 638)
    turtle.bgpic("shape_window.png")
    draw_circle(0, 0)
    screen.onclick(hello_world)

if __name__ == "__main__":
    main()
    
