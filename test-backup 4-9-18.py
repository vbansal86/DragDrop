
import tkinter as tk

from tkinter import *  
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image
import os 


def OpenFile():
    global name 
    name = askopenfilename(initialdir="C:/",
                           filetypes =(("Images", "*.png"),("All Files","*.*")),
                           title = "Choose a file."
                      )
    #fileopen = True
    file = open('filename.txt', 'w')
    file.write(name)
    file.close()
    img = Image.open(name)
    tk_img = ImageTk.PhotoImage(img)  
    w.create_image(20, 20, anchor=NW, image=tk_img)  




def isAreaTooSmall (x1,y1,x2,y2) :
    if ((abs(x1-x2) * abs (y1-y2)) < 10) :
        return True
    else:
        return False
    
def isPointWithinCurrentSelection (point, currentSelection) :
    [x,y] = point
    [x1,y1,x2,y2] = currentSelection
    if (  ( (x > x1)  & (x < x2)) |  ( (x > x2)  & (x < x1) )) :
        if (  (( y > y1)  & (y < y2)) |  ( (y > y2)  & (y < y1) )) :
            return True
        else:
            return False
    else:
        return False
    
    
    
def trackButtonMotionEvent(event):
    global prepareToMove, moveRectangle
    #print("this is button move")
    if prepareToMove == True:
        #print("prepare to move")

        if moveRectangle is None:
           
            moveRectangle = w.create_rectangle(event.x, event.y, event.x+20, event.y+20)
        else:
           
            w.delete(moveRectangle)
            moveRectangle = w.create_rectangle(event.x, event.y, event.x+20, event.y+20)
            
    

def trackButtonPressedEvent (event):
    global fromX, fromY, prepareToMove, curRectangle
    print("Button press")

    if curRectangle is None:
        fromX = event.x
        fromY = event.y
        prepareToMove = False
    else:
        if prepareToMove == True:
            if isPointWithinCurrentSelection([event.x, event.y], w.coords(curRectangle)) == True:
                print("")
            else:
               
                w.delete(curRectangle)
                curRectangle = None
                prepareToMove = False
        else:
            if isPointWithinCurrentSelection([event.x, event.y], w.coords(curRectangle)) == True:
            
                prepareToMove = True
            else:
                
                fromX = event.x
                fromY = event.y

def trackButtonReleaseEvent (event):
    global fromX, fromY, toX, toY, curRectangle,prepareToMove, moveRectangle , dropbox , FirstTime
    
    print("Button release")
  

    if prepareToMove == True:
        if isPointWithinCurrentSelection([event.x, event.y], w.coords(dropbox)) == True:
            
            
            # crop the part of prescription form and send to deep learning model for prediction
            crop_img = img.crop((fromX-20,fromY-20,toX-20,toY-20))
            crop_img.save("crop.png")
            #crop_img.show()
            #tk_crop_img  = ImageTk.PhotoImage(crop_img)
            #w.create_image(800, 390, image=tk_crop_img)
            os.system('python text_recognition_demo.py ".\model" model_190000.npz crop.png ctc_char_map.json')
            file = open('prediction.txt', 'r')
            prediction  = file.readline()
            if FirstTime:
                FirstTime = False
                w.create_text(900,450,text="Prediction=" +  prediction,tag="DEL")
            else:
                w.delete("DEL")
                w.create_text(900,450,text="Prediction=" +  prediction,tag="DEL")

            script.delete(0,END)
            script.insert(0,prediction)
            
            
            
            
        else:
            print("")
    else:
        
        if curRectangle is None:
            if (isAreaTooSmall(event.x, event.y, fromX, fromY)):
                print("")
            else:
            
                toX = event.x
                toY = event.y
                curRectangle = w.create_rectangle(fromX, fromY, toX, toY)

                if moveRectangle is not None:
                    w.delete(moveRectangle)

        else :
            if (isAreaTooSmall(event.x, event.y, fromX, fromY)):
                w.delete(curRectangle)
               
                curRectangle = None
                if moveRectangle is not None:
                    w.delete(moveRectangle)

            else:
                w.delete(curRectangle)
                toX = event.x
                toY = event.y
                curRectangle = w.create_rectangle(fromX, fromY, toX, toY)
                if moveRectangle is not None:
                    w.delete(moveRectangle)


curRectangle=None
dropbox = None
moveRectangle = None
fromX, fromY, toX, toY = (None, None, None, None)
FirstTime = True
name = ""
prepareToMove = True
#fileopen= False
root = Tk()
root.title("Text Recognition Demo")
root.geometry("1200x1000")


canvas_width = 1200
canvas_height = 1000
w = Canvas(root, 
           width=canvas_width,
           height=canvas_height)
w.pack()
w.bind( "<ButtonPress-1>", trackButtonPressedEvent )
w.bind( "<ButtonRelease-1>", trackButtonReleaseEvent )
w.bind( "<B1-Motion>", trackButtonMotionEvent )

#label2 = tk.Label(w, text="DragNDrop Marked Prescription from the image -->")
#label2.place(x=800, y=500)


#w.create_rectangle(800, 500, 940, 640, fill="yellow")
menu = Menu(root)
root.config(menu=menu)
file = Menu(menu)
#file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())
menu.add_cascade(label = 'File', menu = file)

#print(fileopen)
#print(file)

#filename = askopenfilename()

script_txt = ""
script=Entry(w,textvariable=script_txt,width=50)

script.place(x=800, y=400)
y = int(canvas_height / 2)

w.create_rectangle(0, 0, canvas_width, canvas_height,fill="grey")
dropbox = w.create_rectangle(800, 300, 1100, 380, fill="yellow")
w.create_text(920,290,text= "Drop word here",font=("Times New Roman", 12, "bold"))

#filename = open('filename.txt', 'r')
#fname  = filename.readline()
#img = Image.open(fname)
img = Image.open("C:\\Users\\vbdon\\Documents\\Deep Learning\\handwriting-synthesis-master\\handwriting-synthesis-master\\output\\Prescription2206756.png")

tk_img = ImageTk.PhotoImage(img)  
w.create_image(20, 20, anchor=NW, image=tk_img)  

root.mainloop() 
