import tkinter as tk
from test2 import state
import levels

def main():
    level=levels.level4
    root = tk.Tk()
    root.title("Zero Squares Puzzle")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    
    stat = state(level)
    stat.draw_Squares(level,canvas)
    root.bind("<Left>", lambda event: stat.move_left( canvas))
    root.bind("<Right>", lambda event: stat.move_right( canvas))
    root.bind("<Up>", lambda event: stat.move_up(canvas))
    root.bind("<Down>", lambda event: stat.move_down( canvas))


    root.mainloop()
if __name__ == "__main__":
   main()