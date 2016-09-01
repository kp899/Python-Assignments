
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
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  The Top Ten of Everything
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design to produce a useful
#  application for accessing online data.  See the instruction
#  sheet accompanying this template for full details.
#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
#  Import the modules needed for this assignment.  You may not import
#  any other modules or rely on any other files.  All data and images
#  needed for your solution must be sourced from the Internet.
#

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import the Tkinter functions
from Tkinter import *

# Import Python's HTML parser
from HTMLParser import *

#Import sql
from sqlite3 import *



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a GIF image, return a Tkinter
#  PhotoImage object suitable for use as the 'image' attribute
#  in a Tkinter Label widget or any other such widget that
#  can display images.
#
def gif_to_PhotoImage(gif_image):

    # Encode the byte stream as a base-64 character string
    # (MIME Base 64 format)
    characters = gif_image.encode('base64', 'strict')

    # Return the result as a Tkinter PhotoImage
    return PhotoImage(data = characters)



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a JPG or PNG image, return a
#  Tkinter PhotoImage object suitable for use as the 'image'
#  attribute in a Tkinter Label widget or any other such widget
#  that can display images.  If positive integers are supplied for
#  the width and height (in pixels) the image will be resized
#  accordingly.
#
def image_to_PhotoImage(image, width = None, height = None):

    # Import the Python Imaging Library, if it exists
    try:
        from PIL import Image, ImageTk
    except:
        raise Exception, 'Python Imaging Library has not been installed properly!'

    # Import StringIO for character conversions
    from StringIO import StringIO

    # Convert the raw bytes into characters
    image_chars = StringIO(image)

    # Open the character string as a PIL image, if possible
    try:
        pil_image = Image.open(image_chars)
    except:
        raise Exception, 'Cannot recognise image given to "image_to_Photoimage" function\n' + \
                         'Confirm that image was downloaded correctly'

    # Resize the image, if a new size has been provided
    if type(width) == int and type(height) == int and width > 0 and height > 0:
        pil_image = pil_image.resize((width, height), Image.ANTIALIAS)

    # Return the result as a Tkinter PhotoImage
    return ImageTk.PhotoImage(pil_image)



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by putting your solution below.
#


##### DEVELOP YOUR SOLUTION HERE #####
#Setting up the window
Top10 = Tk()
Top10.configure(bg ='black')
#Importing an image from imgur for the Splash Screen
#This image is designed by me in order to get a pretty and minimalist splash screen
mainscreen = 'http://i.imgur.com/ahN7hrx.jpg'
image1 = urlopen(mainscreen).read()
#Adjusting the height and width as the resolution of
#the image is high
Startscreen= image_to_PhotoImage(image1, width = 550,height = 700)
#Creating a label to show up at the splash screen
mainlabel = Label(Top10,image = Startscreen)

#Definig a function for the first button
#Getting a dynamically updated list of top 100 songs
#Extract the Top 10 from them
#A function to clean up irrelevant characters
def CleanUp(result_list):
    for each in range(len(result_list)):
        result_list[each] = result_list[each].replace("&#039;","'")
    return result_list
def CleanUpSpaces(result_list):
    for each in range(len(result_list)):
        result_list[each] = result_list[each].replace(" ","")

#Defining a function to display the top 10 songs
#when the button is pressed
def tensongs():
    top10songs = Toplevel()
    top10songs.title('Top Songs')
    top10songs.configure(bg = '#422C2F')
    songscreen = 'http://www.justinmaller.com/img/projects/wallpaper/WP_Portraits-2560x1440_00078.jpg'
    songimage = urlopen(songscreen).read()
    Topsongs = image_to_PhotoImage(songimage, width = 500, height = 300)
    songlabel = Label(top10songs,image = Topsongs)
    # Get the top 10 songs
    songslist_url = 'http://www.billboard.com/charts/hot-100'
    listurl_open = urlopen(songslist_url).read()
    songslist = findall('chart-row__song">([^<>]*)</h2>', listurl_open)
#Cleaning up the song list of any unwanted characters causing issues with the song name
#Apostrophe in this case
    CleanUp(songslist)
    #add each to label
    number1 = Label(top10songs,foreground = 'white', text = '1.' + str(songslist[0]),background = '#422C2F', font = ('Gotham',10))
    number2 = Label(top10songs,foreground = 'white', text = '2.' + str(songslist[1]),background = '#422C2F',font = ('Gotham',10))
    number3 = Label(top10songs,foreground = 'white', text = '3.' + str(songslist[2]),background = '#422C2F',font = ('Gotham',10))
    number4 = Label(top10songs,foreground = 'white', text = '4.' + str(songslist[3]),background = '#422C2F',font = ('Gotham',10))
    number5 = Label(top10songs,foreground = 'white', text = '5.' + str(songslist[4]),background = '#422C2F', font = ('Gotham',10))
    number6 = Label(top10songs,foreground = 'white', text = '6.' + str(songslist[5]),background = '#422C2F', font = ('Gotham',10))
    number7 = Label(top10songs,foreground = 'white', text = '7.' + str(songslist[6]),background = '#422C2F', font = ('Gotham',10))
    number8 = Label(top10songs,foreground = 'white', text = '8.' + str(songslist[7]),background = '#422C2F', font = ('Gotham',10))
    number9 = Label(top10songs,foreground = 'white', text = '9.' + str(songslist[8]),background = '#422C2F', font = ('Gotham',10))
    number10 = Label(top10songs,foreground = 'white', text = '10.' + str(songslist[9]),background = '#422C2F', font = ('Gotham',10))
    def save10songs():
        #Connect to a database
        connection = connect(database='top_ten.db')
        topsong_db = connection.cursor()
        #This line is to make sure we don't get Unicode error
        #while executing the program
        connection.text_factory = str
        #Delete the data from database
        #so that when the save button is pressed in another window
        #no error is caught
        topsong_db.execute("DELETE FROM Top_Ten")
        for rank in range(1, 10+1):
            topsong_db.execute("INSERT INTO Top_Ten (Rank, Description) VALUES(?,?)",(rank, songslist[rank - 1]))
        #  Commit connection
        connection.commit()
        #  Close the cursor
        topsong_db.close()
        #  Close the database connection
        connection.close()
    #Create a save button to save the top 10 list to a database
    save_button = Button(top10songs,text = 'Save list',command = save10songs,foreground = '#422C2F', background = 'white',font = ('Gotham',10))
    #Pack all the number labels using the
    #Grid layout
    number1.grid(row=1,column=0)
    number2.grid(row=2,column=0)
    number3.grid(row=3,column=0)
    number4.grid(row=4, column=0)
    number5.grid(row=5,column=0)
    number6.grid(row=1,column=1)
    number7.grid(row=2,column=1)
    number8.grid(row=3,column=1)
    number9.grid(row=4,column=1)
    number10.grid(row=5,column=1)
    #Pack the save button using grid layout
    save_button.grid(row = 6, column = 0, columnspan =2)
    #Pack the image
    songlabel.grid(row=0, column =0, columnspan = 2)
    top10songs.mainloop()
#Get a list of top 10 affordable phones from techradar.com
#This site updates the data pretty often
def toptencheapphones():
    top10cheapphones = Toplevel()
    top10cheapphones.title('Top 10 Cheap Phones')
    top10cheapphones.configure(bg = 'black')
    phonescreen = 'https://cnet2.cbsistatic.com/hub/i/r/2015/07/13/03356e88-7f09-4a8d-8e40-3e63930f9a24/resize/970xauto/ce1cb445e025b4d522d2b6e13754f094/pile-of-phones-3530-003.jpg'
    #Trick the url to thinking it's a browser
    import urllib
    urllib.URLopener.version = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; T312461)'
    raw_bytes = urllib.urlopen(phonescreen).read()
    Topphones = image_to_PhotoImage(raw_bytes,width = 500, height = 300 )
    Phonelabel = Label(top10cheapphones, image = Topphones)
    #Get the top 10 Affordable phone
    #from techradar.com
    top10phones_url = 'http://www.techradar.com/au/news/phone-and-communications/mobile-phones/best-cheap-smartphones-payg-mobiles-compared-961975'
    phone_urlopen = urlopen(top10phones_url).read()
    #Use regular expression to etract the nedded data
    phonelist = findall('</figure></p><h3>([^<>]*)',phone_urlopen)
    #Display each element in the list in the form of labels
    number1 = Label(top10cheapphones,text = str(phonelist[0]),background = 'black',foreground = 'white',font = ('Gotham',16))
    number2 = Label(top10cheapphones,text = str(phonelist[1]),background = 'black',foreground = 'white', font = ('Gotham',16))
    number3 = Label(top10cheapphones,text = str(phonelist[2]),background = 'black',foreground = 'white', font = ('Gotham',16))
    number4 = Label(top10cheapphones,text = str(phonelist[3]),background = 'black',foreground = 'white',font = ('Gotham',16))
    number5 = Label(top10cheapphones,text = str(phonelist[4]),background = 'black',foreground = 'white', font = ('Gotham',16))
    number6 = Label(top10cheapphones,text = str(phonelist[5]),background = 'black',foreground = 'white', font = ('Gotham',16))
    number7 = Label(top10cheapphones,text = str(phonelist[6]),background = 'black',foreground = 'white', font = ('Gotham',16))
    number8 = Label(top10cheapphones,text = str(phonelist[7]),background = 'black',foreground = 'white', font = ('Gotham',16))
    number9 = Label(top10cheapphones,text = str(phonelist[8]),background = 'black',foreground = 'white', font = ('Gotham',16))
    number10 = Label(top10cheapphones,text = str(phonelist[9]),background = 'black',foreground = 'white', font = ('Gotham',16))
    def save10phones():
        #Connect to a database
        connection = connect(database='top_ten.db')
        topphone_db = connection.cursor()
        #This line is to make sure we don't get Unicode error
        #while executing the program
        connection.text_factory = str
        #Delete the data from database
        #so that when the save button is pressed in another window
        #no error is caught
        #The following line is to delete any previous record
        topphone_db.execute("DELETE FROM Top_Ten")
        for rank in range(1, 10+1):
            topphone_db.execute("INSERT INTO Top_Ten (Rank, Description) VALUES(?,?)",(rank, phonelist[rank - 1]))
        #  Commit connection
        connection.commit()
        #  Close the cursor
        topphone_db.close()
        #  Close the database connection
        connection.close()
    #Create a save button to save the top 10 list to a database
    save_button = Button(top10cheapphones,text = 'Save list',command = save10phones,foreground = 'white', background = 'black',font = ('Gotham',10))
    #Pack the number labels using the grid layout
    number1.grid(row=1,column=0)
    number2.grid(row=2,column=0)
    number3.grid(row=3,column=0)
    number4.grid(row=4, column=0)
    number5.grid(row=5,column=0)
    number6.grid(row=1,column=1)
    number7.grid(row=2,column=1)
    number8.grid(row=3,column=1)
    number9.grid(row=4,column=1)
    number10.grid(row=5,column=1)
    #Pack the save button using grid layout
    save_button.grid(row = 6, column = 0, columnspan =2)
    #Pack the Label using the grid layout
    Phonelabel.grid(row=0,column =0, columnspan =2)
    top10cheapphones.mainloop()
def toptenandroidapps():
    top10androidapps = Toplevel()
    background = ('black')
    top10androidapps.title('Top 10 Apps on the Play Store')
    top10androidapps.configure(bg='black')
    appscreen = 'http://neurogadget.com/wp-content/uploads/2015/11/Google-Play-Store-6.00-Google-Play-Store-Google.jpg'
    appimage = urlopen(appscreen).read()
    #Decrese the size of the image as the resolution is too high
    Topapps = image_to_PhotoImage(appimage, width = 500, height = 300)
    Applabel = Label(top10androidapps, image = Topapps)
    #Get the top 10 apps from Google play
    toptenappsurl = 'https://play.google.com/store/apps/top'
    appurlopen = urlopen(toptenappsurl).read()
    #Use regular expression to extract data
    applist = findall('aria-label=" ([^<>]*)">',appurlopen)
    #Display the top 10 of the list in the form of labels
    CleanUpSpaces(applist)
    number1 = Label(top10androidapps, text = str(applist[0]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    number2 = Label(top10androidapps, text = str(applist[1]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    number3 = Label(top10androidapps, text = str(applist[2]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    number4 = Label(top10androidapps, text = str(applist[3]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    number5 = Label(top10androidapps, text = str(applist[4]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    number6 = Label(top10androidapps, text = str(applist[5]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    number7 = Label(top10androidapps, text = str(applist[6]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    number8 = Label(top10androidapps, text = str(applist[7]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    number9 = Label(top10androidapps, text = str(applist[8]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    number10 = Label(top10androidapps, text = str(applist[9]), font = ('times new roman',15), foreground = 'dark green', background = 'black')
    def save10apps():
        #Connect to a database
        connection = connect(database='top_ten.db')
        topapps_db = connection.cursor()
        #This line is to make sure we don't get Unicode error
        #while executing the program
        connection.text_factory = str
        #Delete the data from database
        #so that when the save button is pressed in another window
        #no error is caught
        topapps_db.execute("DELETE FROM Top_Ten")
        for rank in range(1, 10+1):
            topapps_db.execute("INSERT INTO Top_Ten (Rank, Description) VALUES(?,?)",(rank, applist[rank - 1]))
        #  Commit connection
        connection.commit()
        #  Close the cursor
        topapps_db.close()
        #  Close the database connection
        connection.close()
    #Create a save button to save the top 10 list to a database
    save_button = Button(top10androidapps,text = 'Save list',command = save10apps,foreground = 'black', background = 'dark green',font = ('Gotham',10))
    #Pack all the number labels using grid layout
    number1.grid(row=1,column=0)
    number2.grid(row=2,column=0)
    number3.grid(row=3,column=0)
    number4.grid(row=4, column=0)
    number5.grid(row=5,column=0)
    number6.grid(row=1,column=1)
    number7.grid(row=2,column=1)
    number8.grid(row=3,column=1)
    number9.grid(row=4,column=1)
    number10.grid(row=5,column=1)
    #Pack the save button using grid layout
    save_button.grid(row = 6, column = 0, columnspan =2)
    #Pack the label in grid layout
    Applabel.grid(row = 0, column = 0, columnspan = 2)
    top10androidapps.mainloop()
#Setting Up buttons in the main window
#And pack them as well
#First Button
button1 = Button(Top10,text="Top 10 songs",bg = 'black', fg = 'white', command = tensongs)
button1.grid(row = 2,column = 0)

#Second Button
button2 = Button(Top10, text = "Top 10 Affordable Phones",bg = 'black', fg = 'white', command = toptencheapphones)
button2.grid(row = 2, column = 1)

#Third Button
button3 = Button(Top10, text = "Top 10 Android Apps",bg = 'black', fg = 'white', command = toptenandroidapps)
button3.grid(row= 2, column = 2)
#pack the label and intitiate the loop
mainlabel.grid(row = 0,column =0,columnspan = 3)
Top10.mainloop()
