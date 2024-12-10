import tkinter as tk
import random


def draw_dice(dice, number):
    size = 8
    dice.create_rectangle(0, 0, 100, 100, fill="white", outline="black")
    positions = {
        1: [(50, 50)],
        2: [(30, 30), (70, 70)],
        3: [(30, 30), (50, 50), (70, 70)],
        4: [(30, 30), (70, 30), (30, 70), (70, 70)],
        5: [(30, 30), (70, 30), (50, 50), (30, 70), (70, 70)],
        6: [(30, 30), (70, 30), (30, 50), (70, 50), (30, 70), (70, 70)],
    }

    for x, y in positions[number]:
        dice.create_oval(x - size, y - size, x + size, y + size, fill="black")


root = tk.Tk()
root.title("Rzut kostka D6")
root.geometry("180x200")

dice = tk.Canvas(root, width=100, height=100)
dice.grid(pady=20, padx=40)

button = tk.Button(root, text="Rzuc kostka", command=lambda: draw_dice(dice, random.randint(1, 6)))
button.grid()

root.mainloop()
