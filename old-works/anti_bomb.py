import tkinter as tk

bomb = 100
score = 0
press_return = True

root = tk.Tk()
root.title("AntiBomb")
root.iconbitmap("user.ico")
root.geometry("600x700+500+300")

label = tk.Label(text="Press [Return] to start the game.", font=('Comic Sans MS', 14))
label.pack()

fuse_label = tk.Label(text=f"Fuse: {bomb}", font=('Comic Sans MS', 14), foreground="red")
fuse_label.pack()

score_label = tk.Label(text=f"Score: {score}", font=('Comic Sans MS', 14), foreground="green")
score_label.pack()

img_1 = tk.PhotoImage(file="1.png")
img_2 = tk.PhotoImage(file="2.png")
img_3 = tk.PhotoImage(file="3.png")
img_4 = tk.PhotoImage(file="4.png")

img_label = tk.Label(image=img_1)
img_label.pack()

def start(event):
    global press_return
    if not press_return:
        pass
    else:
        update_display()
        update_bomb()
        update_score()
        label.config(text='')
        press_return = False

def update_display():
    global bomb
    global score

    if bomb >= 80:
        img_label.config(image=img_1)
    elif 50 <= bomb < 80:
        img_label.config(image=img_2)
    elif 0 < bomb < 50:
        img_label.config(image=img_3)
    else:
        img_label.config(image=img_4)

    fuse_label.config(text=f'Fuse: {str(bomb)}')
    score_label.config(text=f'Score: {str(score)}')
    fuse_label.after(100, update_display)

def is_alive():
    global bomb
    global press_return

    if bomb <= 0:
        bomb = 0
        label.config(text='Game Over.')
        press_return = True
        return False
    else:
        return True

def update_bomb():
    global bomb
    bomb -= 3
    if is_alive():
        fuse_label.after(400, update_bomb)

def update_score():
    global score
    if is_alive():
        score += 1
        score_label.after(3000, update_score)


def click():
    global bomb
    if is_alive():
        bomb+=1

button = tk.Button(root, text='Click me!', background="black", foreground="white", width=25, font=('Comic Sans MS', 14), command=click)
button.pack()

root.bind('<Return>', start)
root.mainloop()