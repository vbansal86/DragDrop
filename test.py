
import tkinter as tk

from tkinter import *  
from tkinter import filedialog
from PIL import ImageTk,Image
import os 




class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command= self.OpenFile)
        fileMenu.add_command(label = 'Exit', command = lambda:exit())
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)
    def OpenFile(self):
        
        global name
        print("hello")
        ftypes = [("Images", "*.png"), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        print("fl=",fl)
        if fl != '':
            return fl
        #fileopen = True
            #file = open(f1, 'r')
            
#            img = Image.open(fl)
#            tk_img = ImageTk.PhotoImage(img)  
#            w.create_image(20, 20, anchor=NW, image=tk_img)  
    
            
            


def isAreaTooSmall (x1,y1,x2,y2) :
    if ((abs(x1-x2) * abs (y1-y2)) < 10) :
        return True
    else:
        return False
    
def isPointWithinCurrentSelection (point, currentSelection) :
    [x,y] = point
    print("current",currentSelection)
    print("event",point)
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
    print("this is button move")
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
    global fromX, fromY, toX, toY, curRectangle,prepareToMove, moveRectangle , drugbox1 , FirstTime
    
    print("Button release")
    
  

    if prepareToMove == True:
        if isPointWithinCurrentSelection([event.x, event.y], drugbox1) == True:
            # crop the part of prescription form and send to deep learning model for prediction
            crop_img = img.crop((fromX-2,fromY-2,toX-2,toY-2))
            crop_img.save("crop.png")
            os.system('python text_recognition_demo.py ".\model" model_190000.npz crop.png ctc_char_map.json')
            file = open('prediction.txt', 'r')
            prediction  = file.readline()
            script1.delete(0,END)
            script1.insert(0,prediction)
        if isPointWithinCurrentSelection([event.x, event.y], drugbox2) == True:
            # crop the part of prescription form and send to deep learning model for prediction
            crop_img = img.crop((fromX-2,fromY-2,toX-2,toY-2))
            crop_img.save("crop.png")
            os.system('python text_recognition_demo.py ".\model" model_190000.npz crop.png ctc_char_map.json')
            file = open('prediction.txt', 'r')
            prediction  = file.readline()
            script2.delete(0,END)
            script2.insert(0,prediction)
        if isPointWithinCurrentSelection([event.x, event.y], drugbox3) == True:
            # crop the part of prescription form and send to deep learning model for prediction
            crop_img = img.crop((fromX-2,fromY-2,toX-2,toY-2))
            crop_img.save("crop.png")
            os.system('python text_recognition_demo.py ".\model" model_190000.npz crop.png ctc_char_map.json')
            file = open('prediction.txt', 'r')
            prediction  = file.readline()
            script3.delete(0,END)
            script3.insert(0,prediction)
        if isPointWithinCurrentSelection([event.x, event.y], namebox) == True:
            # crop the part of prescription form and send to deep learning model for prediction
            crop_img = img.crop((fromX-2,fromY-2,toX-2,toY-2))
            crop_img.save("crop.png")
            os.system('python text_recognition_demo.py ".\model" model_190000.npz crop.png ctc_char_map.json')
            file = open('prediction.txt', 'r')
            prediction  = file.readline()
            script4.delete(0,END)
            script4.insert(0,prediction)
        if isPointWithinCurrentSelection([event.x, event.y], addrbox) == True:
            # crop the part of prescription form and send to deep learning model for prediction
            crop_img = img.crop((fromX-2,fromY-2,toX-2,toY-2))
            crop_img.save("crop.png")
            os.system('python text_recognition_demo.py ".\model" model_190000.npz crop.png ctc_char_map.json')
            file = open('prediction.txt', 'r')
            prediction  = file.readline()
            script5.delete(0,END)
            script5.insert(0,prediction)
        if isPointWithinCurrentSelection([event.x, event.y], diagbox) == True:
            # crop the part of prescription form and send to deep learning model for prediction
            crop_img = img.crop((fromX-2,fromY-2,toX-2,toY-2))
            crop_img.save("crop.png")
            os.system('python text_recognition_demo.py ".\model" model_190000.npz crop.png ctc_char_map.json')
            file = open('prediction.txt', 'r')
            prediction  = file.readline()
            script6.delete(0,END)
            script6.insert(0,prediction)
            
            
            
            
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

def main():
    global curRectangle,dropbox,moveRectangle,fromX,fromY,toX,toY,name,prepareToMove , w , drugbox1,drugbox2,drugbox3, namebox,addrbox,diagbox , img, script1,script2,script3,script4,script5,script6
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
    root.geometry("1500x900")
    root.attributes('-fullscreen', True)

    canvas_width = 1500
    canvas_height = 900
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
    #menu = Menu(root)
    #root.config(menu=menu)
    #file = Menu(menu)
#file.add_command(label = 'Open', command = OpenFile)
    #file.add_command(label = 'Exit', command = lambda:exit())
    #menu.add_cascade(label = 'File', menu = file)

#print(fileopen)
#print(file)

#filename = askopenfilename()

#script_txt = ""
#script=Entry(w,textvariable=script_txt,width=50)

#script.place(x=800, y=400)
    y = int(canvas_height / 2)

    w.create_rectangle(0, 0, canvas_width, canvas_height,fill="grey")
    
#dropbox = w.create_rectangle(800, 300, 1100, 380, fill="yellow")
#w.create_text(920,290,text= "Drop word here",font=("Times New Roman", 12, "bold"))

#filename = open('filename.txt', 'r')
#fname  = filename.readline()
#img = Image.open(fname)
    imgnam = Example(root)
    print("imgnam =",imgnam)
    #img = Image.open("C:\\Users\\vbdon\\Documents\\Deep Learning\\handwriting-synthesis-master\\handwriting-synthesis-master\\output\\Prescription2206756.png")
    img = Image.open(imgnam)
    tk_img = ImageTk.PhotoImage(img)  
    w.create_image(2, 2, anchor=NW, image=tk_img) 
    
    img2 = Image.open("C:\\Users\\vbdon\Documents\\Deep Learning\\dragdrop\\templates\\form.jpg")
    tk_img2 = ImageTk.PhotoImage(img2)  
    w.create_image(670, 150, anchor=NW, image=tk_img2)  

    drugbox1 = [720,380,1320,400]
    script_txt = ""
    script1=Entry(w,textvariable=script_txt,width=65,bg="light blue",bd=4,justify = "center",font = "Arial")
    script1.place(x=720, y=380)
    
    drugbox2 = [720,430,1320,450]
    script2=Entry(w,textvariable=script_txt,width=65,bg="light blue",bd=4,justify = "center",font = "Arial")
    script2.place(x=720, y=430)
    
    drugbox3 = (720,480,1320,500)
    script3=Entry(w,textvariable=script_txt,width=65,bg="light blue",bd=4,justify = "center",font = "Arial")
    script3.place(x=720, y=480)

    namebox = (770,205,1074,224)
    script4=Entry(w,textvariable=script_txt,width=50,bg="light blue",bd=4)
    script4.place(x=770, y=205)
    
    addrbox = (770,245,1214,260)
    script5=Entry(w,textvariable=script_txt,width=80,bg="light blue",bd=4)
    script5.place(x=770, y=240)
    
    diagbox = (770,290,1350,310)
    script6=Entry(w,textvariable=script_txt,width=95,bg="light blue",bd=4)
    script6.place(x=770, y=290)
    

#dropbox = w.create_rectangle(800, 300, 1100, 380, fill="yellow")
#w.create_text(920,290,text= "Drop word here",font=("Times New Roman", 12, "bold"))

#w.create_image(700, 20, anchor=NW, image=tk_img)  

    root.mainloop() 


if __name__ == '__main__':
       main()  