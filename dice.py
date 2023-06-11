# Simulate a rolling die using the tkinter and random modules
import tkinter as tk
import random

def random_roll():
    num = random.randint(1,6) # endpoints included in range
    result_lbl["text"] = num

# window instantiation
window = tk.Tk()
window.geometry("300x200")


roll_frame = tk.Frame(
                    master = window, 
                    relief = tk.RAISED,
                    borderwidth = 1,
                    width=100,
                    height=100
                      )
roll_frame.pack()

roll_btn = tk.Button(master = roll_frame, text = "Roll", command =  random_roll)
roll_btn.pack()

result_lbl = tk.Label(master = window, text = 'Click "Roll" to begin!')
result_lbl.pack()

window.mainloop()
