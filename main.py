import tkinter as tk
from state import state
import levels

def main():
    level = levels.level6
    root = tk.Tk()
    root.title("Zero Squares Puzzle")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    
    stat = state(level)
    stat.draw_Squares(level, canvas)

    # algorithm_choice = tk.StringVar(value="BFS") 
    # tk.Radiobutton(root, text="BFS", variable=algorithm_choice, value="BFS").pack(side="left")
    # tk.Radiobutton(root, text="DFS", variable=algorithm_choice, value="DFS").pack(side="left")
    root.bind("<Left>", lambda event: print(stat.move_left( canvas)))
    root.bind("<Right>", lambda event: print(stat.move_right( canvas)))
    root.bind("<Up>", lambda event: print(stat.move_up(canvas)))
    root.bind("<Down>", lambda event: print(stat.move_down( canvas)))
    solve_button = tk.Button(root, text="حل تلقائي", command=lambda: print(stat.UCS(canvas)))
    solve_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
