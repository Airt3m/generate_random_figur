from tkinter import *
import random
listcvet = ["red",'yellow', 'blue', 'green', 'orange', 'purple', 'gray', 'plum', 'black', 'tan']
def generator():
    cvet = random.choice(listcvet)
    canvas.delete("all")
    d = round(random.uniform(0, 2), 0)
    print(cvet)
    if d == 0:
        canvas.create_oval(random.uniform(0, 1000), random.uniform(0, 500), random.uniform(0, 1000), random.uniform(0, 500), fill=cvet, outline="black")
    elif d == 1:
        canvas.create_rectangle(random.uniform(0, 1000), random.uniform(0, 500), random.uniform(0, 1000), random.uniform(0, 500), fill=cvet, outline="black")
    elif d == 2:
        canvas.create_polygon(random.uniform(0, 1000), random.uniform(0, 500), random.uniform(0, 1000), random.uniform(0, 500), random.uniform(0, 1000), random.uniform(0, 500), fill=cvet, outline="black")
root = Tk()

canvas = Canvas(root,width=1000,height=500,bg="white")
canvas.pack()
button = Button(
    text ="generate",
    width=5,
    height=5,
    bg="blue",
    command=generator
)
button.pack()
root.mainloop()






