
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N9643885
#    Student name: Komalpreet Singh
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  MY STRETCHY FAMILY
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_portrait".
#  You are required to complete this function so that when the
#  program is run it produces a portrait of a stick figure family in
#  the style of the car window stickers that have become popular in
#  recent years, using data stored in a list to determine the
#  locations and heights of the figures.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  only your final solution, whether or not you complete both
#  parts.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for drawing the background.  You should not change any
# of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to import any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

window_height = 550 # pixels
window_width = 900 # pixels
grass_height = 200 # pixels
grass_offset = -100 # pixels
location_width = 150 # pixels
num_locations = 5

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background and the locations where the individuals in the
# portrait are required to stand.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up.
#


# Draw the grass as a big green rectangle
def draw_grass():

    penup()
    goto(-window_width / 2, grass_offset) # start at the bottom-left
    setheading(90) # face north
    fillcolor('pale green')
    begin_fill()
    forward(grass_height)
    right(90) # face east
    forward(window_width)
    right(90) # face south
    forward(grass_height)
    right(90) # face west
    forward(window_width)
    end_fill()


# Draw the locations where the individuals must stand
def draw_locations(locations_on = True):

    # Only draw the locations if the argument is True
    if locations_on:

        # Define a small gap at each end of each location
        gap_size = 5 # pixels
        location_width_less_gaps = location_width - (gap_size * 2) # pixels

        # Start at the far left, facing east
        penup()
        goto(-num_locations * location_width / 2, 0)
        setheading(0)

        # Draw each location as a thick line with a gap at each end
        color('dark khaki')
        for location in range(num_locations):
            penup()
            forward(gap_size)
            pendown()
            width(5) # draw a thick line
            forward(location_width_less_gaps)
            width(1)
            penup()
            forward(gap_size)


# Draw the numeric labels on the locations
def draw_labels(labels_on = True):

    # Only draw the labels if the argument is True
    if labels_on:

        font_size = 16 # size of characters for the labels

        # Start in the middle of the left-hand location, facing east
        penup()
        goto(-((num_locations - 1) * location_width) / 2,
             -font_size * 2)
        setheading(0)

        # Walk to the right, print the labels as we go
        color('dark khaki')
        for label in range(num_locations):
            write(label, font = ('Arial', font_size, 'bold'))
            forward(location_width)


# As a debugging aid, mark certain absolute coordinates on the canvas
def mark_coords(marks_on = True):

    # Only mark the coordinates if the argument is True
    if marks_on:

        # Mark the "home" coordinate
        home()
        width(1)
        color('black')
        dot(3)
        write('0, 0', font = ('Arial', 10, 'normal'))

        # Mark the centre point of each individual's location
        max_x = (num_locations - 1) * location_width / 2
        penup()
        for x_coord in range(-max_x, max_x + location_width, location_width):
            for y_coord in [0, 400]:
                goto(x_coord, y_coord)
                dot(3)
                write(str(x_coord) + ', ' + str(y_coord),
                      font = ('Arial', 10, 'normal'))

#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the positions for
# the people in the portrait:
#
# 1. The name of the individual, from 'Person A' to 'Person D' or 'Pet'
# 2. The place where that person/pet must stand, from location 0 to 4
# 3. How much to stretch the person/pet vertically, from 0.5 to 1.5
#    times their normal height
# 4. A mystery value, either '*' or '-', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily include all people and sometimes
# they require the same person to be drawn more than once.  You
# can assume, however, that they never put more than one person in
# the same location.
#
# You may add additional data sets but you may not change any of the
# given data sets below.
#

# The following data set doesn't require drawing any people at
# all.  You may find it useful as a dummy argument when you
# first start developing your "draw_portrait" function.



# The following data sets each draw just one of the individuals
# at their default height.

portrait_01 = [['Person A', 2, 1.0, '-']]

portrait_02 = [['Person B', 3, 1.0, '-']]

portrait_03 = [['Person C', 1, 1.0, '-']]

portrait_04 = [['Person D', 0, 1.0, '-']]

portrait_05 = [['Pet', 4, 1.0, '-']]

# The following data sets each draw just one of the individuals
# but multiple times and at different sizes.

portrait_06 = [['Person A', 3, 1.0, '-'],
               ['Person A', 1, 0.75, '-'],
               ['Person A', 2, 0.5, '-'],
               ['Person A', 4, 1.4, '-']]

portrait_07 = [['Person B', 0, 0.5, '-'],
               ['Person B', 2, 1.0, '-'],
               ['Person B', 3, 1.5, '-']]

portrait_08 = [['Person C', 0, 0.5, '-'],
               ['Person C', 1, 0.75, '-'],
               ['Person C', 2, 1.0, '-'],
               ['Person C', 3, 1.25, '-'],
               ['Person C', 4, 1.5, '-']]

portrait_09 = [['Person D', 3, 1.25, '-'],
               ['Person D', 1, 0.8, '-'],
               ['Person D', 0, 1.0, '-']]

portrait_10 = [['Pet', 1, 1.3, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Pet', 3, 0.7, '-']]

# The following data sets each draw a family portrait with all
# individuals at their default sizes.  These data sets create
# "natural" looking portraits.  Notably, the first two both
# show the full family.

portrait_11 = [['Person A', 0, 1.0, '-'],
               ['Person B', 1, 1.0, '-'],
               ['Person C', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Pet', 4, 1.0, '-']]

portrait_12 = [['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*'],
               ['Person C', 1, 1.0, '-'],
               ['Person D', 4, 1.0, '-'],
               ['Pet', 0, 1.0, '-']]

portrait_13 = [['Person B', 1, 1.0, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Person C', 3, 1.0, '*']]

portrait_14 = [['Person C', 0, 1.0, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Person B', 4, 1.0, '-']]

portrait_15 = [['Person D', 4, 1.0, '*'],
               ['Person A', 3, 1.0, '-'],
               ['Person B', 2, 1.0, '-']]

portrait_16 = [['Person D', 1, 1.0, '-'],
               ['Person C', 0, 1.0, '-'],
               ['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*']]

# The following data sets draw all five individuals at their
# minimum and maximum heights.

portrait_17 = [['Person A', 0, 0.5, '-'],
               ['Person B', 1, 0.5, '-'],
               ['Person C', 2, 0.5, '*'],
               ['Person D', 3, 0.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_18 = [['Person A', 4, 1.5, '-'],
               ['Person B', 3, 1.5, '*'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 1, 1.5, '-'],
               ['Pet', 0, 1.5, '-']]

# The following data sets each draw a family portrait with
# various individuals at varying sizes.

portrait_19 = [['Person A', 0, 0.5, '*'],
               ['Person B', 1, 0.8, '-'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_20 = [['Person B', 1, 0.8, '*'],
               ['Pet', 2, 1.4, '-'],
               ['Person C', 3, 0.7, '-']]

portrait_21 = [['Person C', 0, 1.5, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '*'],
               ['Person B', 4, 1.5, '-']]

portrait_22 = [['Person D', 4, 1.2, '-'],
               ['Person A', 3, 1.0, '*'],
               ['Person B', 2, 0.8, '-']]

portrait_23 = [['Person D', 1, 1.1, '-'],
               ['Person C', 2, 0.9, '-'],
               ['Person A', 0, 1.1, '*'],
               ['Person B', 3, 0.9, '-']]

# ***** If you want to create your own data sets you can add them here
# ***** (but your code must still work with all the data sets above plus
# ***** any other data sets in this style).

#
#--------------------------------------------------------------------#

#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_portrait" function.

def draw_portrait(value):
    for each in value:
        def moveanddraw (seth, forw):
            setheading(seth)
            forward(forw+forw * each[2])
        def draw_stretchable_circles(colorr,verticle_stretch,horizontal_stretch,pen_width):
            fillcolor(colorr)
            shape('circle')
            width(pen_width)
            shapesize(horizontal_stretch*each[2]-(each[2]*0.10), verticle_stretch*each[2],pen_width)
            stamp()
            shape('classic')
            shapesize(1,1,1)
            #putting an if statement for debugging purposes and to make the figures with smaller sizes more legible
            if each[2] <= 0.5:
                fillcolor(colorr)
                shape('circle')
                width(pen_width)
                shapesize(horizontal_stretch*(each[2] + 0.20), verticle_stretch*(each[2] + 0.20),pen_width)
                stamp()
                shape('classic')
                shapesize(1,1,1)
                    
        #Define a location function which accepts the data in the portrait list
        def location(pos):
            if pos == 0:
                goto(-300,0)
            elif pos == 1:
                goto(-150,0)
            elif pos == 2:
                goto(0,0)
            elif pos == 3:
                goto(150,0)
            elif pos == 4:
                goto(300,0)
        if each[0] == 'Person A':
            #Draw_Dad
            location(each[1])
            moveanddraw(90,40)
            width(2)
            pendown()
            color('black','blue')
            begin_fill()
            moveanddraw(-75,28)
            moveanddraw(0,10)
            moveanddraw(100,40)
            moveanddraw(180,20)
            moveanddraw(-100,40)
            moveanddraw(0,10)
            moveanddraw(75,28)
            end_fill()
            penup()
            #Torso
            moveanddraw(90,12)
            moveanddraw(0,10)
            #Belt
            pendown()
            moveanddraw(90,5)
            width(2)
            color('black','yellow')
            begin_fill()
            moveanddraw(180,20)
            moveanddraw(-90,5)
            moveanddraw(0,20)
            end_fill()
            #Shirt
            pendown()
            color('black','green')
            begin_fill()
            moveanddraw(90,25)
            moveanddraw(300,10)
            moveanddraw(45,10)
            moveanddraw(120,15)
            moveanddraw(180,30)
            moveanddraw(-120,15)
            moveanddraw(-45,10)
            moveanddraw(60,10)
            moveanddraw(-90,20)
            moveanddraw(0,20)
            end_fill()
            #Head
            moveanddraw(180,9)
            width(4)
            moveanddraw(90,45)
            #Using a previously created function to create the head and the eyes
            draw_stretchable_circles('light pink',2,2,3)
            penup()
            moveanddraw(0,5)
            draw_stretchable_circles('brown',0.25,0.25,2)
            penup()
            #Creating a spereation between the eyes
            moveanddraw(180,10)
            draw_stretchable_circles('brown',0.25,0.25,2)
            penup()
            #Eyes and smile
            moveanddraw(0,4)
            moveanddraw(-90,7.5)
            #using the classic turtle shape and multiplying the verticle dimension
            #with the stretch factor then stamping it produce the smile instead of
            #using curved lines
            shapesize(1.5,0.75* each[2],1.5)
            fillcolor('red')
            stamp()
            #Reverting the turtle back to it's original shape and dimensions
            shape('classic')
            shapesize(1,1,1)
            penup()
            #Drawing the arms
            moveanddraw(-90,6)
            moveanddraw(0,15)
            moveanddraw(300,15)
            moveanddraw(-135,5)
            pendown()
            #Setting the pen width to 4 to make arms
            width(4)
            moveanddraw(-35,8)
            draw_stretchable_circles('light pink',0.5,0.5,2)
            penup()
            #Now Going to the other shoulder to make the other arm
            moveanddraw(145,8)
            moveanddraw(55,5)
            moveanddraw(60,15)
            moveanddraw(180,45)
            moveanddraw(-120,15)
            moveanddraw(315,5)
            width(4)
            pendown()
            moveanddraw(-90,8)
            draw_stretchable_circles('light pink',0.5,0.5,2)
            penup()
            #Draw Shoes
            moveanddraw(-90,55)
            moveanddraw(0,6.5)
            draw_stretchable_circles('yellow',1.4,0.6,2)
            moveanddraw(0,27)
            draw_stretchable_circles('yellow',1.4,0.6,2)
            #Draw Dad's hair
            location(each[0])
            penup()
            moveanddraw(180,22.5)
            #Using an if statement to fix the larger figure's hair
            if each[2]>1.25:
                moveanddraw(90,95)
            else:
               moveanddraw(90,92)
            pendown()
            color('black')
            begin_fill()
            moveanddraw(75,12.5)
            moveanddraw(-60,5)
            end_fill()
            begin_fill()
            moveanddraw(95,7)
            moveanddraw(0,7)
            moveanddraw(-35,8)
            moveanddraw(-80,8)
            end_fill()
            penup()
            location(each[1])
            #Draw Crown
            if each[3] == '*':
                moveanddraw(180,10)
                moveanddraw(90,105)
                color('black','yellow')
                begin_fill()
                pendown()
                moveanddraw(90,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-60,10)
                moveanddraw(80,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,15)
                moveanddraw(80,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,15)
                moveanddraw(60,10)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-85,12.5)
                moveanddraw(180,22)
                end_fill()
                penup()
        #Draw Mom
        #Drawing Mom's Shoes
        if each[0] == 'Person B':
            location(each[1])
            penup()
            moveanddraw(90,10)
            moveanddraw(180,15)
            draw_stretchable_circles('purple',1.4,0.6,2)
            moveanddraw(0,30)
            draw_stretchable_circles('purple',1.4,0.6,2)
            #Draw Legs
            #Right Leg
            penup()
            width(5)
            moveanddraw(100,3)
            pendown()
            moveanddraw(100,15)
            #Go Back
            penup()
            moveanddraw(-80,18)
            moveanddraw(180, 32)
            moveanddraw(80,3)
            pendown()
            #Right Leg
            color('black','crimson')
            begin_fill()
            moveanddraw(80,15)
            #Start Drawing the Skirt
            width(2)
            moveanddraw(180,10)
            moveanddraw(80,30)
            moveanddraw(0,35)
            moveanddraw(-80,30)
            moveanddraw(180,35)
            end_fill()
            #Draw Torso
            #Cursor Setup
            penup()
            moveanddraw(90,30)
            begin_fill()
            moveanddraw(180,5)
            #Put the pendown to start drawing
            pendown()
            moveanddraw(90,20)
            moveanddraw(-120,10)
            moveanddraw(120,5)
            width(3)
            moveanddraw(250,10)
            draw_stretchable_circles('light pink',0.5,0.5,2)
            width(2)
            moveanddraw(70,10)
            moveanddraw(110,8)
            moveanddraw(60,12)
            moveanddraw(0,22.5)
            #Turn and Draw head
            moveanddraw(90,15)
            draw_stretchable_circles('light pink',2,2,2)
            draw_stretchable_circles('light pink',2,2,3)
            penup()
            #Right Eye
            moveanddraw(0,5)
            draw_stretchable_circles('blue',0.25,0.25,2)
            penup()
            #Creating a spereation between the eyes
            moveanddraw(180,10)
            #Left Eye
            draw_stretchable_circles('blue',0.25,0.25,2)
            penup()
            #Smile
            moveanddraw(0,5)
            moveanddraw(-90,7)
            #using the classic turtle shape and multiplying the verticle dimension
            #with the stretch factor then stamping it produce the smile instead of
            #using curved lines
            shapesize(1.75,0.75* each[2],1)
            fillcolor('red')
            stamp()
            #Returning the cursor to classic shape
            shape('classic')
            shapesize(1,1,1)
            penup()
            moveanddraw(270,7.5)
            pendown()
            moveanddraw(0,22.5)
            moveanddraw(-70,12)
            moveanddraw(-120,5)
            width(3)
            moveanddraw(-70,8)
            draw_stretchable_circles('light pink',0.5,0.5,2)
            color('black','purple')
            moveanddraw(110,8)
            moveanddraw(-120,8)
            moveanddraw(110,10)
            moveanddraw(-90,21)
            moveanddraw(180,32.5)
            end_fill()
            penup()
            #Draw hair
            #Short strand
            moveanddraw(0,5)
            moveanddraw(90,48)
            pendown()
            begin_fill()
            color('black')
            moveanddraw(-90,8)
            moveanddraw(-135,7)
            moveanddraw(80,7)
            moveanddraw(100,7)
            moveanddraw(70,7)
            moveanddraw(60,7)
            moveanddraw(-80,8)
            end_fill()
            #Other Strand
            begin_fill()
            moveanddraw(85,12.5)
            moveanddraw(0,7)
            moveanddraw(330,7)
            moveanddraw(320,10)
            moveanddraw(-90,5)
            moveanddraw(-80,5)
            moveanddraw(-60,5)
            moveanddraw(-45,3)
            moveanddraw(160,10)
            moveanddraw(80,7)
            moveanddraw(120,7)
            moveanddraw(170,10)
            moveanddraw(200,7)
            end_fill()
            penup()
            location(each[1])
            #Draw Crown
            #For Mom's head we have to design a different crown
            if each[3] == '*':
                moveanddraw(180,15)
                moveanddraw(90,110)
                color('black','yellow')
                begin_fill()
                pendown()
                moveanddraw(90,17)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-60,10)
                moveanddraw(80,17)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,17)
                moveanddraw(80,17)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,17)
                moveanddraw(80,17)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                #Last strand
                moveanddraw(-80,17)
                moveanddraw(60,12.5)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-90,18)
                moveanddraw(180,32.5)
                end_fill()
                penup()
        #Draw little sister
        #Now Go to another location to draw lil sis
        #Add an if statement afterwards and change location
        if each[0] == 'Person C':
            location(each[1])
            penup()
            moveanddraw(90,10)
            moveanddraw(180,15)
            draw_stretchable_circles('red',1.4,0.5,2)
            moveanddraw(0,30)
            draw_stretchable_circles('red',1.4,0.5,2)
            #Draw Legs
            #Right Leg
            penup()
            width(3)
            moveanddraw(180,4)
            moveanddraw(100,2)
            pendown()
            moveanddraw(100,15)
            #Go Back
            penup()
            moveanddraw(-80,18)
            moveanddraw(180, 32)
            moveanddraw(70,3)
            moveanddraw(0,8)
            moveanddraw(80,1)
            pendown()
            moveanddraw(80,15)
            #penup and move to the middle of the body to draw torso
            penup()
            moveanddraw(0,8)
            shape('triangle')
            moveanddraw(90,10)
            shapesize(2.6,4.5 *each[2],2)
            fillcolor('yellow')
            stamp()
                
            #Return to classic shape with original dimensions
            shape('classic')
            shapesize(1,1,1)
            penup()
            color('black')
            #Putting some if and elif sttement to get the neck size right
            #for each size
            if each[2] <= 0.5:
                moveanddraw(90,16)
            elif 0.5 <=each[2]<= 0.75 :
                moveanddraw(90,19)
            elif 0.75 <=each[2]<=1.0 :
                moveanddraw(90,22)
            elif 1.0<= each[2]<=1.25:
                moveanddraw(90,25)
            elif 1.25<= each[2]<= 1.5:
                moveanddraw(90,28)
            pendown()
            width(2)
            if each[2] <= 0.5:
                moveanddraw(90,14)
            elif 0.5 <=each[2]<= 0.75 :
                moveanddraw(90,16)
            elif 0.75<= each[2] <=1.0:
                moveanddraw(90,18)
            elif 1.0<= each[2]<=1.25:
                moveanddraw(90,20)
            elif 1.25<= each[2]<= 1.5:
                moveanddraw(90,22)
            #Draw Sis's Head
            draw_stretchable_circles('light pink',2,2,2)
            #Draw Sis's eyes
            moveanddraw(0,5)
            draw_stretchable_circles('blue',0.25,0.25,2)
            penup()
            #Creating a spereation between the eyes
            moveanddraw(180,10)
            #Left Eye
            draw_stretchable_circles('blue',0.25,0.25,2)
            penup()
            #Smile
            moveanddraw(0,5)
            moveanddraw(-90,7.5)
            #using the classic turtle shape and multiplying the verticle dimension
            #with the stretch factor then stamping it produce the smile instead of
            #using curved lines
            shapesize(1.5,0.5*each[2],1)
            fillcolor('red')
            stamp()
            shape('classic')
            shapesize(1,1,1)
            penup()
            moveanddraw(-90,6)
            #Using some if and elif statements yo get the arms position right
            if each[2] <= 0.5:
                moveanddraw(-60,10)
            elif 0.5 <=each[2]<= 0.75 :
                moveanddraw(-60,12.5)
            elif 0.75<= each[2] <=1.0:
                moveanddraw(-70,17.5)
            elif 1.0<= each[2]<=1.25:
                moveanddraw(-75,22.5)
            elif 1.25<= each[2]<= 1.5:
                moveanddraw(-80,25)
            #Draw Arms
            width(3)
            pendown()
            moveanddraw(0,10)
            draw_stretchable_circles('light pink',0.5,0.5,2)
            penup()
            if 1<= each[2]<=1.25:
                moveanddraw(180,21)
            elif 1.25<= each[2]<=1.5:
                moveanddraw(180,19)
            else:
                moveanddraw(180,22.5)
            width(3)
            pendown()
            moveanddraw(180,10)
            draw_stretchable_circles('light pink',0.5,0.5,2)
            penup()
            #Draw Sis's hair
            moveanddraw(70,25)
            pendown()
            begin_fill()
            color('black')
            #Using some if statement to manage the hair
            if each[2] <= 0.5:
                moveanddraw(-90,11)
            elif 0.5<each [2]<= 0.75:
                moveanddraw(-90,10)
            elif 0.75<each[2]<= 1.0:
                moveanddraw(180,1)
                moveanddraw(-90,5)
            elif 1.25<each[2]<=1.5:
                moveanddraw(180,1)
                moveanddraw(90,6)
            moveanddraw(180,3)
            moveanddraw(-135,7)
            moveanddraw(80,10)
            moveanddraw(100,7)
            moveanddraw(70,7)
            moveanddraw(60,7)
            moveanddraw(-80,8)
            end_fill()
            #Draw the other strand
            begin_fill()
            moveanddraw(85,10)
            moveanddraw(0,7)
            moveanddraw(330,7)
            moveanddraw(320,8)
            moveanddraw(-90,5)
            moveanddraw(-80,8)
            moveanddraw(-60,5)
            moveanddraw(-45,4)
            moveanddraw(160,10)
            moveanddraw(90,7)
            moveanddraw(120,7)
            moveanddraw(170,10)
            moveanddraw(200,7)
            end_fill()
            penup()
            location(each[1])
            #Draw Crown
            if each[3] == '*':
                moveanddraw(180,12.5)
                moveanddraw(90,80)
                color('black','yellow')
                begin_fill()
                pendown()
                moveanddraw(90,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-60,10)
                moveanddraw(80,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,15)
                moveanddraw(80,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,15)
                moveanddraw(60,10)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-85,12.5)
                moveanddraw(180,22)
                end_fill()
                penup()
        #Draw Me(lol)
        if each[0] == 'Person D':
            location(each[1])
            color('black')#Change the color to black for further drawing
            penup()
            moveanddraw(90,10)
            moveanddraw(180,15)
            draw_stretchable_circles('green',1.4,0.5,2)
            moveanddraw(0,30)
            draw_stretchable_circles('green',1.4,0.5,2)
            #Draw Legs
            #Right Leg
            penup()
            color('black')
            width(3)
            moveanddraw(180,4)
            moveanddraw(100,2)
            pendown()
            moveanddraw(100,15)
            #Go Back 
            penup()
            moveanddraw(-80,18)
            moveanddraw(180, 32)
            moveanddraw(70,3)
            moveanddraw(0,8)
            moveanddraw(80,1)
            pendown()
            moveanddraw(80,15)
            width(2)
            #Draw Shorts
            begin_fill()
            color('black','white')
            moveanddraw(0,3)
            moveanddraw(80,25)
            moveanddraw(-80,25)
            moveanddraw(0,10)
            moveanddraw(100,30)
            moveanddraw(180,17.5)
            moveanddraw(-100,30)
            moveanddraw(0,10)
            end_fill()
            penup()
            #Move up to draw the torso
            #move towards the centre
            moveanddraw(0,4)
            moveanddraw(90,29)
            pendown()
            #Draw Shirt
            begin_fill()
            color('black','red')
            moveanddraw(180,10)
            moveanddraw(90,15)
            moveanddraw(-120,7.5)
            moveanddraw(120,5)
            width(3)
            moveanddraw(250,7.5)
            draw_stretchable_circles('light pink',0.5,0.5,2)
            width(2)
            moveanddraw(70,7.5)
            moveanddraw(110,6)
            moveanddraw(45,7.5)
            moveanddraw(0,15)
            #Turn and Draw head
            moveanddraw(90,15)
            draw_stretchable_circles('light pink',1.75,1.75,2)
            draw_stretchable_circles('light pink',1.75,1.75,3)
            penup()
            #Right Eye
            moveanddraw(0,5)
            draw_stretchable_circles('blue',0.25,0.25,2)
            penup()
            #Creating a spereation between the eyes
            moveanddraw(180,10)
            #Left Eye
            draw_stretchable_circles('blue',0.25,0.25,2)
            penup()
            #Face Emotion
            moveanddraw(0,5)
            moveanddraw(-90,5)
            pendown()
            moveanddraw(0,4)
            moveanddraw(180,4)
            penup()
            moveanddraw(-90,10)
            #Continue and draw arms
            pendown()
            moveanddraw(0,15)
            moveanddraw(-60,5)
            moveanddraw(-70,6)
            moveanddraw(-135,4)
            width(3)
            moveanddraw(-60,7.5)
            draw_stretchable_circles('light pink',0.5,0.5,2)
            color('black','blue')
            width(2)
            moveanddraw(120,7.5)
            moveanddraw(-135,3.5)
            moveanddraw(130,9)
            moveanddraw(-90,15)
            moveanddraw(180,13)
            end_fill()
            penup()
            #Draw hair
            moveanddraw(90,45)
            pendown()
            moveanddraw(100,8)
            penup()
            moveanddraw(-45,9)
            pendown()
            moveanddraw(100,7)
            penup()
            moveanddraw(-50,9)
            pendown()
            moveanddraw(100,7)
            penup()
            moveanddraw(-70,12)
            pendown()
            moveanddraw(90,10)
            moveanddraw(-90,10)
            penup()
            moveanddraw(180,15)
            pendown()
            moveanddraw(110,10)
            penup()
            location(each[1])
            #Draw Crown
            if each[3] == '*':
                moveanddraw(180,10)
                moveanddraw(90,100)
                color('black','yellow')
                begin_fill()
                pendown()
                moveanddraw(90,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-60,10)
                moveanddraw(80,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,15)
                moveanddraw(80,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,15)
                moveanddraw(60,10)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-85,15)
                moveanddraw(180,22)
                end_fill()
                penup()
        if each[0] == 'Pet':
            #Draw Pig
            #Remember to add if function
            location(each[1])
            #Drawing the Pig
            penup()
            moveanddraw(90,32.5)
            setheading(180)
            draw_stretchable_circles('light pink',5.2,2.5,2)
            penup()
            moveanddraw(160,20)
            draw_stretchable_circles('light pink',2.5,2,2)
            penup()
            #Eyes
            moveanddraw(0,5)
            draw_stretchable_circles('black',0.25,0.25,2)
            penup()
            #Creating a spereation between the eyes
            moveanddraw(180,10)
            #Left Eye
            draw_stretchable_circles('black',0.25,0.25,2)
            penup()
            #Nose
            moveanddraw(0,5)
            moveanddraw(-90,4)
            draw_stretchable_circles('pink',0.40,0.6,2)
            #Draw ears
            penup()
            moveanddraw(135,12.5)
            pendown()
            moveanddraw(135,2.5)
            draw_stretchable_circles('light pink',0.50,0.40,2)
            penup()
            moveanddraw(0,20)
            draw_stretchable_circles('light pink',0.50,0.40,2)
            penup()
            #Draw Tail
            moveanddraw(335,32.5)
            pendown()
            moveanddraw(60,3)
            moveanddraw(90,4.5)
            moveanddraw(45,5)
            #Draw Legs
            penup()
            moveanddraw(240,22)
            pendown()
            moveanddraw(-80,15)
            moveanddraw(180,2)
            draw_stretchable_circles('black',0.40,0.6,2)
            #draw the other leg
            penup()
            moveanddraw(130,16)
            pendown()
            moveanddraw(-90,13)
            moveanddraw(180,2)
            draw_stretchable_circles('black',0.40,0.6,2)
            #continue drawing other legs
            penup()
            moveanddraw(180,10)
            moveanddraw(105,15)
            pendown()
            moveanddraw(-90,15)
            moveanddraw(180,2)
            draw_stretchable_circles('black',0.40,0.6,2)
            #Last Leg
            penup()
            moveanddraw(90,16)
            pendown()
            moveanddraw(-120,16)
            moveanddraw(180,2)
            draw_stretchable_circles('black',0.40,0.6,2)
            penup()
            location(each[1])
            #Draw Crown
            if each[3] == '*':
                moveanddraw(180,30)
                moveanddraw(90,45)
                color('black','yellow')
                begin_fill()
                pendown()
                moveanddraw(90,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-60,10)
                moveanddraw(80,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,15)
                moveanddraw(80,15)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-80,15)
                moveanddraw(60,10)
                draw_stretchable_circles('yellow',0.3,0.3,2)
                moveanddraw(-85,15)
                moveanddraw(180,22)
                end_fill()
                penup()
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your stick figures.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing window with a blue background representing
# the sky, and with the "home" coordinate set to the middle of the
# area where the stick figures will stand
setup(window_width, window_height)
setworldcoordinates(-window_width / 2, grass_offset,
                    window_width / 2, window_height + grass_offset)
bgcolor('sky blue')

# Draw the grass (with animation turned off to make it faster)
tracer(False)
draw_grass()

# Give the window a title
# ***** Replace this title with one that describes your choice
# ***** of individuals
title('My Stretchy Family (Describe your theme and the individuals here)')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Draw the locations to stand, their labels and selected coordinates
# ***** If you don't want to display these background elements,
# ***** to make your portrait look nicer, change the corresponding
# ***** argument(s) below to False
draw_locations(True)
draw_labels(True)
mark_coords(True)
# Call the student's function to display the stick figures
# ***** If you want to turn off animation while drawing your
# ***** stick figures, to make your program draw faster, change
# ***** the following argument to False
tracer(True)
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_portrait(portrait_23)
# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
##hideturtle()
done()
#
#--------------------------------------------------------------------#

