import tkinter as tk
from state import state
import levels

def main():

    level = levels.level30
    root = tk.Tk()
    root.title("Zero Squares Puzzle")
    canvas = tk.Canvas(root, width=1000, height=550)
    canvas.pack()
    
    stat = state(level)
    stat.draw_Squares(level, canvas)

    root.bind("<Left>", lambda event: print(stat.move_left()))
    root.bind("<Right>", lambda event: print(stat.move_right()))
    root.bind("<Up>", lambda event: print(stat.move_up()))
    root.bind("<Down>", lambda event: print(stat.move_down( )))
    
    algorithm_choice = tk.StringVar(value="BFS") 
    tk.Radiobutton(root, text="BFS", variable=algorithm_choice, value="BFS").pack(side="left")
    tk.Radiobutton(root, text="DFS", variable=algorithm_choice, value="DFS").pack(side="left")
    tk.Radiobutton(root, text="UCS", variable=algorithm_choice, value="UCS").pack(side="left")
    tk.Radiobutton(root, text="A_star", variable=algorithm_choice, value="A_star").pack(side="left")

     
    solve_button = tk.Button(root, text="حل تلقائي", command=lambda: print(stat.solve(canvas, algorithm_choice.get())))
    solve_button.pack()


    root.mainloop()

if __name__ == "__main__":
    main()
