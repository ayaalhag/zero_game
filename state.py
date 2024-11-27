import tkinter as tk
from collections import deque
import heapq
import copy

class state:
    def __init__(self, level):
        self.history = []
        self.now_level = copy.deepcopy(level)
  
    def represent_Squares(self, level):
        rows = len(level)
        cols = len(level[0])
        color_arry = [[None for _ in range(cols)] for _ in range(rows)]
        border_arry = [[None for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                # لون المربع
                if int(level[i][j]) == 0:
                    color = "white"
                elif int(level[i][j]) == 1:
                    color = "black"
                elif int(level[i][j]) == 2:
                    color = "green"
                elif int(level[i][j]) == 3:
                    color = "blue"
                elif int(level[i][j]) == 4:
                    color = "red"
                color_arry[i][j] = color
                # لون الهدف
                decimal_part = round((level[i][j] - int(level[i][j])), 1)
                if decimal_part == 0.1:
                    border = "black"
                elif decimal_part == 0.2:
                    border = "green"
                elif decimal_part == 0.3:
                    border = "blue"
                elif decimal_part == 0.4:
                    border = "red"
                else:
                    border = color
                border_arry[i][j] = border
        return color_arry, border_arry
    
    def update_and_store_level(self, level_copy):
        if level_copy is None:
            print("Cannot update with a None level_copy")
        self.now_level = level_copy
        self.history.append(copy.deepcopy(self.now_level))
        
    def draw_Squares(self, level, canvas):
        color_arry = self.represent_Squares(level)[0]
        border_arry = self.represent_Squares(level)[1]
        rows = len(level)
        cols = len(level[0])
        cell_size = 50
        for i in range(rows):
            for j in range(cols):
                canvas.create_rectangle(
                    j * cell_size, i * cell_size,
                    (j + 1) * cell_size, (i + 1) * cell_size,
                    outline=border_arry[i][j], fill=color_arry[i][j], width=3
                )        
  
    def Moving_stones(self, level):
        Moving = []
        rows = len(level)
        cols = len(level[0])
        for i in range(rows):
            for j in range(cols):  
                if int(level[i][j]) != 1 and int(level[i][j]) != 0:
                    Moving.append((i, j))
        return Moving
    
    def get_possible_moves(self):
        moves = []
        moveable_stones = self.Moving_stones(self.now_level)
        for stone in moveable_stones:
            row, col = stone
            if col + 1 < len(self.now_level[0]) and not self.is_blok(self.now_level, row, col + 1):
                moves.append(("right"))
            if col - 1 >= 0 and not self.is_blok(self.now_level, row, col - 1):
                moves.append(("left"))
            if row - 1 >= 0 and not self.is_blok(self.now_level, row - 1, col):
                moves.append(("up"))
            if row + 1 < len(self.now_level) and not self.is_blok(self.now_level, row + 1, col):
                moves.append(("down"))
        return moves
   
    def is_blok(self, level, row, col):
        if (round((level[row][col]) - int(level[row][col]), 1)) == 0.1: 
            return True
        elif int(level[row][col]) != 0: 
            return True
        return False
    
    def on_gool(self, level, rowG, colG, valu):
        if round((level[rowG][colG]) - int(level[rowG][colG]), 1) * 10 == valu:
            return True
        else:
            return False

    def move_right(self,canvas):
        level = copy.deepcopy(self.now_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
        total_weight = 0
        for r in range(Nrow_move):
                Ncols_level=len(level[0])
                col_level=move[r][1]
                row_level=move[r][0]
                new_col =col_level 
                old_cell = int(level[row_level][col_level])
                #هي بتمشي ع مصفوفة level
                for j in range(col_level + 1, Ncols_level):
                    if self.is_blok(level, row_level, j): 
                        break 
                    else:
                        new_col = j 
                total_weight += abs(new_col - col_level)
                level[row_level][col_level] = round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
                if(self.on_gool(level,row_level,new_col,old_cell)):
                 level[row_level][new_col]=0.0
                else:
                 level[row_level][new_col] = level[row_level][new_col]+int(old_cell)
        #self.update_and_store_level(level)
        return level,total_weight
    
    def move_left(self, canvas):
        level = copy.deepcopy(self.now_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
        total_weight =0
        for r in range(Nrow_move):
            row_level=move[r][0]
            col_level=move[r][1]
            new_col =col_level 
            old_cell =int(level[row_level][col_level])
            for j in range(col_level - 1, -1, -1):
              if self.is_blok(level, row_level, j):
                break
              else:
                new_col = j
            total_weight += abs(new_col - col_level)
            level[row_level][col_level] = round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
            if(self.on_gool(level,row_level,new_col,old_cell)):
                level[row_level][new_col]=0.0
            else:
                level[row_level][new_col] = level[row_level][new_col]+int(old_cell)
        # self.update_and_store_level(level)
        return level,total_weight
    
    def move_up(self, canvas):
        level= copy.deepcopy(self.now_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
        total_weight = 0
        for r in range(Nrow_move):
            col_level=move[r][1]
            row_level=move[r][0]
            new_row = row_level
            old_cell = int(level[row_level][col_level])
            for i in range(row_level - 1, -1, -1):
                if self.is_blok(level, i, col_level):
                  break
                else:
                  new_row = i
            total_weight += abs(row_level - new_row)
            level[row_level][col_level] = round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
            if(self.on_gool(level,new_row,col_level,old_cell)):
                level[new_row][col_level]=0.0
            else:
                level[new_row][col_level] =  level[new_row][col_level]+int(old_cell)
        # self.update_and_store_level(level)
        return level,total_weight
    
    def move_down(self, canvas):
        level = copy.deepcopy(self.now_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
        total_weight = 0
        for r in range(Nrow_move):
            col_level=move[r][1]
            row_level=move[r][0]
            rows = len(level)
            new_row = row_level
            old_cell = int(level[row_level][col_level])
            for i in range(row_level + 1, rows):
              if self.is_blok(level, i, col_level):
                break
              else:
                new_row = i
            total_weight += abs(row_level - new_row)
            level[row_level][col_level] =round(level[row_level][col_level]-int(level[row_level][col_level]),1)
            if(self.on_gool(level,new_row,col_level,old_cell)):
                level[new_row][col_level]=0.0
            else:
                level[new_row][col_level] =  level[new_row][col_level]+int(old_cell)
        # self.update_and_store_level(level)
        return level,total_weight
    
    def weight(self,canvas,Pq,old_weight):
        levels=[]
        moves=self.get_possible_moves()
        for move in moves:
            if move == "right":
                next_level, weight = self.move_right(canvas) 
            elif move == "left":
                next_level, weight = self.move_left(canvas)
            elif move == "up":
                next_level, weight = self.move_up(canvas)
            elif move == "down":
                next_level, weight = self.move_down(canvas)
            element_q=f"{move} {weight+ old_weight}"
            Pq.append(element_q)
            levels.append((element_q, next_level))
        
        return(Pq,levels)
    
    def make_move(self, canvas, list_path,visited, delay=500,i=0):
            if i >= len(visited):
                print("Completed drawing all states!")
                return
            canvas.delete("all")
            self.draw_Squares( visited[i],canvas)
            for row in visited[i]:
                print(row)
            print("-" * 20)
            canvas.after(delay, lambda: self.make_move(canvas, list_path, visited,delay,i + 1))
            
    def UCS(self, canvas): 
        Pq = [] 
        path=[]
        visited = [copy.deepcopy(self.now_level)]        
        weight=0   
        Pq,levels=self.weight(canvas,Pq,weight)
        list_opject=[state(self.now_level)]
        count=0
        while Pq:
            count+=1
            if not self.Moving_stones(self.now_level):
                return(path, self.make_move(canvas, path,visited, 1000))
            Pq=sorted(Pq, key=lambda x: int(x.split()[1]))
            pop=Pq.pop(0).split()
            weight=int(pop[1])          
            for move, level in levels:
                if move.split()[0] ==pop[0]:
                    next_level = level
                    break
            if next_level in visited:
                continue
            path.append(pop)
            self.update_and_store_level(next_level)                       
            visited.append(copy.deepcopy(self.now_level))
            opject=state(next_level)
            t,levels=opject.weight(canvas,Pq,weight)
        return "not found solution"
