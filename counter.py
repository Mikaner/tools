from tkinter import *
from tkinter import ttk

root = Tk()
root.title('counter')
h = root.winfo_screenheight()
h = h-270
root.geometry("390x50+300+"+str(h))

success = 0
faild = 0
big_green = 0
red = 0
yellow = 0

def clicked_success():
    global root, success, faild
    success += 1
    label1.configure(text=f'Success:{success}')
    if (success+faild)==10:
        root.destroy()

def clicked_faild():
    global root, success, faild
    faild += 1
    label2.configure(text=f'Faild:{faild}')
    if (success+faild)==10:
        root.destroy()

def clicked_big_green():
    global root, success, faild, big_green
    success += 1
    big_green += 1
    label1.configure(text=f'Success:{success}')
    label3.configure(text=f'Big_green:{big_green}')
    if (success+faild)==10:
        root.destroy()

def clicked_red_food():
    global root, success, faild, red
    faild += 1
    red += 1
    label2.configure(text=f'Faild:{faild}')
    label4.configure(text=f'Red_food:{red}')
    if (success+faild)==10:
        root.destroy()

def clicked_yellow_food():
    global yellow
    yellow += 1
    label5.configure(text=f'Yellow_food:{yellow}')


label1 = ttk.Label(root, text=f"Success:{success}")
label1.grid(column=0, row=0)
label2 = ttk.Label(root, text=f"Faild:{faild}")
label2.grid(column=1, row=0)
label3 = ttk.Label(root, text=f'Big_green:{big_green}')
label3.grid(column=2, row=0)
label4 = ttk.Label(root, text=f'Red_food:{red}')
label4.grid(column=3, row=0)
label5 = ttk.Label(root, text=f'Yellow_food:{yellow}')
label5.grid(column=4, row=0)

success_button = ttk.Button(
    root,
    text='Success',
    command=clicked_success
)

faild_button = ttk.Button(
    root, 
    text='Faild',
    command=clicked_faild
)

big_green_button = ttk.Button(
    root, 
    text='Big_green',
    command=clicked_big_green
)

red_food_button = ttk.Button(
    root, 
    text='Red_food',
    command=clicked_red_food
)

yellow_food_button = ttk.Button(
    root, 
    text='Yellow_food',
    command=clicked_yellow_food
)

success_button.grid(column=0, row=1)
faild_button.grid(column=1, row=1)
big_green_button.grid(column=2, row=1)
red_food_button.grid(column=3, row=1)
yellow_food_button.grid(column=4, row=1)

root.mainloop()

print(f"Success:{success}", f"Faild:{faild}", f'Big_green:{big_green}', f'Red_food:{red}', f'Yellow_food:{yellow}', sep="\n")