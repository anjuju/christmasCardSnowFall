from tkinter import *
from time import *

from random import sample, choice

class Christmas(Frame):
    def __init__(self, name):
        Frame.__init__(self)
        self.name = name

        self.myCanvas = Canvas(width=750, height=500, bg="navy")
        self.myCanvas.grid()


        # Moon

        self.myCanvas.create_oval(50, 50, 125, 125, outline="lemon chiffon", fill="lemon chiffon")
        self.myCanvas.create_oval(70, 70, 140, 140, outline="navy", fill="navy")

        

        # Tree

        self.myCanvas.create_polygon(600, 300, 700, 400, 500, 400, outline="forest green", fill="forest green")
        self.myCanvas.create_polygon(600, 250, 675, 350, 525, 350, outline="forest green", fill="forest green")
        self.myCanvas.create_polygon(600, 200, 650, 300, 550, 300, outline="forest green", fill="forest green")
        self.myCanvas.create_rectangle(590,400,610,450, outline="sienna4", fill="sienna4")

        # Star

        self.myCanvas.create_polygon(600,178, 604,188, 614,188, 606,194, 610,206, 600,200, 590,206, 594,194, 586,188, 596,188, outline="gold", fill="gold")


        # Message

        self.myCanvas.create_text(325, 200, text="I'm dreaming of \n       a white Christmas...", font=("Edwardian Script ITC", 40), fill="white")
        self.myCanvas.create_line(125, 125, 175, 125, fill="gold")
        self.myCanvas.create_line(125, 125, 125, 175, fill="gold")
        self.myCanvas.create_line(130, 130, 170, 130, fill="gold")
        self.myCanvas.create_line(130, 130, 130, 170, fill="gold")
        self.myCanvas.create_line(480, 275, 531, 275, fill="gold")
        self.myCanvas.create_line(530, 225, 530, 275, fill="gold")
        self.myCanvas.create_line(485, 270, 526, 270, fill="gold")
        self.myCanvas.create_line(525, 230, 525, 270, fill="gold")
        


        # Snowman

        self.myCanvas.create_oval(165,395,235,460,outline="white", fill="white")
        self.myCanvas.create_oval(175,355,225,405,outline="white", fill="white")
        self.myCanvas.create_oval(180,325,220,365,outline="white", fill="white")

        self.myCanvas.create_oval(200,340,202,342, fill="black") #eyes
        self.myCanvas.create_oval(212,339,214,341, fill="black")

        self.myCanvas.create_polygon(207,344, 225,348, 204,350, outline="orange", fill="orange") #nose

        self.myCanvas.create_oval(205,370,210,375, fill="black") #buttons
        self.myCanvas.create_oval(207,385,212,390, fill="black")
        self.myCanvas.create_oval(208,400,213,405, fill="black")
        self.myCanvas.create_oval(212,415,217,420, fill="black")

        self.myCanvas.create_rectangle(178,325,222,330, fill="black") #hat
        self.myCanvas.create_rectangle(185,305,215,325, fill="black")
           

        
        # Snow

        self.myCanvas.create_rectangle(0,450,800,550,outline="white", fill="white")


        self.myCanvas.update()
        sleep(5)

        a = 15

        for t in range(50):
            x = sample(range(800), a)
            y = sample(range(20), a)

            if t == 2:
                self.myCanvas.create_text(400, 50, text="Merry Christmas,", fill="red", font=("Algerian", 30))
                self.myCanvas.create_text(550, 100, text=(self.name,"!"), fill="red", font=("Algerian", 30))

            x2 = sample(range(-15,15),a)
            y2 = sample(range(20,35),a)
             
            for j in range(20):
                snow_list = []

                for i in range(a):
                    snowflake = self.myCanvas.create_oval(x[i], y[i], x[i]+5, y[i]+5, outline="white", fill="white")
                    snow_list.append(snowflake)
                    
                    self.myCanvas.coords(snow_list[i], x[i]+x2[i]*j, y[i]+y2[i]*j, x[i]+5+x2[i]*j, y[i]+5+y2[i]*j)
                
                self.myCanvas.update()
                sleep(0.1)

                for i in range(a):
                    self.myCanvas.delete(snow_list[i])
                    self.myCanvas.update()

            if t == 2:
                self.myCanvas.create_polygon(600, 200, 610, 220, 590, 220, outline="white", fill="white")
            elif t == 4:
                self.myCanvas.create_polygon(550, 300, 555, 290, 560, 300, outline="white", fill="white")
                self.myCanvas.create_polygon(650, 300, 645, 290, 640, 300, outline="white", fill="white")
            elif t == 6:
                self.myCanvas.create_polygon(525, 350, 532, 340, 540, 350, outline="white", fill="white")
                self.myCanvas.create_polygon(675, 350, 668, 340, 660, 350, outline="white", fill="white")

                self.myCanvas.create_rectangle(185,303,215,305, outline="white", fill="white")
            elif t == 7:
                self.myCanvas.create_polygon(500, 400, 510, 390, 520, 400, outline="white", fill="white")
                self.myCanvas.create_polygon(700, 400, 690, 390, 680, 400, outline="white", fill="white")
            elif t == 8:
                self.myCanvas.create_rectangle(178,323,222,325, outline="white", fill="white")
                
            elif t % 2 == 1:
            
                x3 = choice(range(560,640))
                y3 = choice(range(250,390))

                self.myCanvas.create_oval(x3, y3, x3+10, y3+5, outline="white", fill="white")
        


card01 = Christmas("Everyone")
card01.mainloop()
        
