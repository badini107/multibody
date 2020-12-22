from tkinter import *
from joint import Joint
from link import Link
from repeatingtimer import RepeatingTimer

w = 500
h = 500

class Mouse():
    def __init__(self):
        self.is_clicked = 0
    
    def click(self):
        self.is_clicked = 1
    
    def release(self):
        self.is_clicked = 0

mouse = Mouse()

root = Tk()
canvas = Canvas(root,  width = w, height = h, bg = "gray")
link = Link(w/2, h/2, w/2 + 5, h-150, mass = 10)
print(link.angle)
link_img = canvas.create_line(link.x0, link.y0, link.x1,  link.y1, width = 5, fill = 'red')

def mouse_click(event):
    mouse.click()
    link.update_position(event.x, event.y)
    print(link.angle)
    canvas.coords(link_img, link.x0, link.y0, link.x1,  link.y1)

def mouse_released(event):
    mouse.release()

def update():
    if not mouse.is_clicked:
        link.update()   
        canvas.coords(link_img, link.x0, link.y0, link.x1,  link.y1)

canvas.bind('<B1-Motion>', mouse_click)
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<ButtonRelease-1>', mouse_released)

t = RepeatingTimer(0.01, update)
t.start()



canvas.grid(column = 0, row = 0)
root.mainloop();

