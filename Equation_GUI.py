from tkinter import *
import paint_app as can
import segmentation_expo_position as segexp
import Model_Detection as dmodel
import plot
import solve
equation=""
def solvefun():
       global equation
       segexp.segstart()                           # Segment the image obtained after drawing and savein current directory
       equation = str(dmodel.detect())          ### Call function detect from Detection_Model python file in same directory ###
       roots = solve.solveIt(equation)
       w = Label(root, text=type, font=("times new roman", 16, "bold"), pady=1, bg='#AEE7FB')
       w.place(x=130, y=378, height=50, width=370)
       w = Label(root, text=roots, font=("times new roman", 16, "bold"), pady=1, bg='#AEE7FB')
       w.place(x=130, y=478, height=50, width=370)
       print(roots)


def graph():
   global equation
   plot.plotgraph(equation) 

if __name__ == "__main__":
   # create a GUI window
   root = Tk()
   root.configure(background="white")

   # set the title of GUI window
   root.title("Equalogy")

   # set the configuration of GUI window
   root.geometry("600x700")
   C = Canvas(root, bg="blue", height=250, width=300)
   filename = PhotoImage(file="equation_bg.png")
   background_label = Label(root, image=filename)
   background_label.place(x=0, y=0, relwidth=1, relheight=1)
   w = Label(root, text="      Mathematical  Equation  Detection  And  Solver        ",font=("times new roman",18, "bold") ,padx=1,pady=1,bg='#AEE7FB')
   w.place(x=0,y=0,height=70,width=600)

   button1 = Button(root, text='  Draw your Equation  ', fg='black', bg='#AEE7FB',font=("times new roman",16, "bold"),command=can.canvasbeg)          ### call the function vanvasbeg from paint_app.py ###
   button1.place(x=140,y=90,height=90,width=350)

   button2 = Button(root, text=' Get solution for equation ', fg='black', bg='#AEE7FB',font=("times new roman",16, "bold"),
                    command=solvefun)
   button2.place(x=140,y=230,height=90,width=350)
   w = LabelFrame(root, text="Type of Equation ", height=1, font=("times new roman",16, "bold"), pady=1,bg='#AEE7FB')
   w.place(x=120,y=350,height=80,width=390)
   
   
   w = LabelFrame(root, text="Roots of Equation are", height=1, font=("times new roman",16, "bold"), pady=1, bg='#AEE7FB')
   w.place(x=120,y=450,height=80,width=390)
  
   button3 = Button(root, text='Get the graph ', fg='black', bg='#AEE7FB', font=("times new roman",16, "bold"),
                    command=graph, height=2, width=16)
   button3.place(x=140,y=580,height=90,width=350)
   root.mainloop()
