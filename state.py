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
        if not isinstance(level, list) or not all(isinstance(row, list) for row in level):
            raise ValueError(f"Invalid level structure: {type(level)}")
        Moving = []
        rows = len(level)
        cols = len(level[0])
        for i in range(rows):
            for j in range(cols):
                cell = level[i][j]
                if isinstance(cell, list):
                    cell = cell[0] if len(cell) > 0 else 0  # إذا كانت قائمة، استخدم العنصر الأول
                if not isinstance(cell, (int, float)):
                    raise ValueError(f"Unexpected type in level[{i}][{j}]: {type(cell)}")
                if int(cell) != 1 and int(cell) != 0:
                    Moving.append((i, j))
        return Moving

    def get_possible_moves(self):
        moves = []
        moveable_stones = self.Moving_stones(self.now_level)
        for stone in moveable_stones:
            row, col = stone
            if col + 1 < len(self.now_level[0]) and not self.is_blok(self.now_level, row, col + 1):
                moves.append(("right", row, col))
            if col - 1 >= 0 and not self.is_blok(self.now_level, row, col - 1):
                moves.append(("left", row, col))
            if row - 1 >= 0 and not self.is_blok(self.now_level, row - 1, col):
                moves.append(("up", row, col))
            if row + 1 < len(self.now_level) and not self.is_blok(self.now_level, row + 1, col):
                moves.append(("down", row, col))
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
        return level
    
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
        return level
    
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
        return level
    
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
        return level
    
    def weight(self,canvas,old_weight):
        levels=[]
        next_moves=[]
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
            next_moves.append(element_q)
            levels.append((element_q, next_level))
        
        return(next_moves,levels)
    
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
    
    def path_cost(path):
        total_cost=0
        for(move,cost) in path :
            total_cost+=cost
        return total_cost
        
    def sort(self,Pq):
        sorted_list = []        
        for sublist in Pq:
            sum_value = sum(int(value) for direction, value in sublist)            
            sorted_list.append((sum_value, sublist))        
        for i in range(len(sorted_list)):
            for j in range(i + 1, len(sorted_list)):
                if sorted_list[i][0] > sorted_list[j][0]:
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]        
        return [sublist for _, sublist in sorted_list]
       
    def UCS(self, canvas): 
        visited = []
        visited.append(copy.deepcopy(self.now_level)) 
        Pq = [] 
        path=[]
        weight=0   
        Pq_start,levels=self.weight(canvas,weight)
        move_p=[]
        for start in Pq_start:
            move_start = start.split()[0]
            move_weight = start.split()[1]
            move_p = [(move_start, move_weight)]  
            Pq.append(move_p.copy())
        count=0
        while Pq:
            count+=1
            print(count)
            if not self.Moving_stones(self.now_level):
                return(path, self.make_move(canvas, path,visited, 1000))
            Pq = self.sort(Pq)           
            pop=Pq.pop(0)
            action, weight = pop[0]  
            weight = int(weight)   
            for move, level in levels:
                if move.split()[0] ==action:
                    next_level = level
                    break
            if next_level in visited:
                continue
            visited.append(copy.deepcopy(self.now_level))   
            path.append(pop[0])
            self.update_and_store_level(next_level) 
            next_moves,levels=self.weight(canvas,weight)
            print('pq b',Pq)
            for next_move in next_moves:
                new_path=path.copy()
                new_path.append((next_move.split()[0],next_move.split()[1]))
                Pq.append(new_path)
            print('pq a',Pq)
            print('-'*20)
        return "not found solution",path

    def dfs_recursive(self, canvas, paths=None, visited=None, list_paths=None):
        print('1')
        if paths is None:
            paths = []
        if visited is None:
            visited = [copy.deepcopy(self.now_level)]
        if list_paths is None:
            list_paths = [copy.deepcopy(self.now_level)] 
        print('2')
        print(self.Moving_stones(self.now_level))         
        if not self.Moving_stones(self.now_level):
            return paths, self.make_move(canvas, list_paths, 1000)
        print('3')
        if not self.Moving_stones(self.now_level):
            return paths, self.make_move(canvas, list_paths, 1000)
        print('4')
        next_moves = self.get_possible_moves()
        grouped_moves = {"right": [], "left": [], "up": [], "down": []}        
        for move in next_moves:
            direction, row, col = move  # الآن يتم فك القيم الثلاثة بشكل صحيح
            grouped_moves[direction].append((row, col))

        print('5')
        for direction, positions in grouped_moves.items():
            if direction in paths: 
                continue
 
            if direction == "right":
                next_level = self.move_right(canvas)
            elif direction == "left":
                next_level = self.move_left(canvas)
            elif direction == "up":
                next_level = self.move_up(canvas)
            elif direction == "down":
                next_level = self.move_down(canvas)
            else:
                continue
            print(f"Current level type: {type(self.now_level)}")
            if next_level in visited:
                continue
            
            paths.append(direction)
            list_paths.append(copy.deepcopy(next_level))
            visited.append(copy.deepcopy(next_level))
            
            self.update_and_store_level(next_level) 
            for n in self.now_level:
                print(n)
            print('-'*20)           
            result = self.dfs_recursive(canvas, paths, visited, next_level)
            if result: 
                return result
            paths.pop()
            list_paths.pop()
        
        return None
