from tkinter import *
import paint_app as can
import segmentation_expo_position as segexp
import Model_Detection as dmodel
import plot
equation=""
def solvefun():
       global equation
       segexp.segstart()                           # Segment the image obtained after drawing and savein current directory
       equation,type, roots = str(dmodel.detect())          ### Call function detect from Detection_Model python file in same directory ###

       w = Label(root, text=type, height=1, font='Arial', justify='right', pady=1, bg='#AEE7FB')
       w.grid(row=6, column=0)
       w = Label(root, text=roots, height=1, font='Arial', bg='#AEE7FB')
       w.grid(row=8, column=0)


def graph():
   global equation
   plot.plotgraph(equation)                  ### Call plotgraph from plot.py

if __name__ == "__main__":
   # create a GUI window
   root = Tk()
   root.configure(background="white")

   # set the title of GUI window
   root.title("Equalogy")

   # set the configuration of GUI window
   root.geometry("490x390")
   C = Canvas(root, bg="blue", height=250, width=300)
   filename = PhotoImage(file="bgfinal1.png")
   background_label = Label(root, image=filename)
   background_label.place(x=0, y=0, relwidth=1, relheight=1)
   w = Label(root, text="      Mathematical  Equation  Detection  And  Solver        ",height=2,font='bold' ,padx=1,pady=1,bg='#AEE7FB')
   w.grid(row=0,column=0)
   w = Label(root, text="Draw the Equation on Canvas ", height=1, font='Arial', justify='right', pady=1,bg='white')
   w.grid(row=1,column=0)
   button1 = Button(root, text='  Click to Draw  ', fg='black', bg='#AEE7FB',font='System',
                    command=can.canvasbeg, height=2, width=16)          ### call the function vanvasbeg from paint_app.py ###
   button1.grid(row=2, column=0)
   w = Label(root, text="Press Solve to get Solution", height=1, font='Arial', justify='right', pady=1, bg='white')
   w.grid(row=3, column=0)
   button2 = Button(root, text=' Solve ', fg='black', bg='#AEE7FB',font='System',
                    command=solvefun, height=2, width=16)
   button2.grid(row=4, column=0)
   w = Label(root, text="Type of Equation ", height=1, font='Arial', justify='right', pady=1,bg='white')
   w.grid(row=5, column=0)
   equation1 = StringVar()
   w = Label(root, text="              ", height=1, font='Arial', justify='right', pady=1, bg='#AEE7FB')
   w.grid(row=6, column=0)

   w = Label(root, text="Roots of Equation are ", height=1, font='Arial', bg='white')
   w.grid(row=7, column=0)

   equation2 = StringVar()

   w = Label(root, text="            ", height=1, font='Arial', bg='#AEE7FB')
   w.grid(row=8, column=0)
   w = Label(root, text="Corresponding Graph  ", height=1, font='Arial', justify='right', pady=1,bg='white')
   w.grid(row=9, column=0)
   button3 = Button(root, text=' Graph ', fg='black', bg='#AEE7FB', font='System',
                    command=graph, height=2, width=16)
   button3.grid(row=11, column=0)
   root.mainloop()


