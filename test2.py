import tkinter as tk
from collections import deque
import copy
class state:
    def __init__(self, level):
        self.history = [] 
        self.naw_level = copy.deepcopy(level)
    
    def update_and_store_level(self,level_copy, canvas,string,delay=5000):
        self.naw_level = level_copy 
        self.history.append(copy.deepcopy(self.naw_level))
  
    def represent_Squares(self, level):
        rows = len(level)
        cols = len(level[0])
        color_arry=[[None for _ in range(cols)] for _ in range(rows)]
        border_arry=[[None for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
#لون المربع
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
                color_arry[i][j]=color
#لون الهدف
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
                    border= color
                border_arry[i][j]=border
        return(color_arry,border_arry)
    
    def draw_Squares(self, level, canvas):
        color_arry=self.represent_Squares(level)[0]
        border_arry=self.represent_Squares(level)[1]
        rows = len(level)
        cols = len(level[0])
        cell_size=50
        for i in range(rows):
          for j in range(cols):
            canvas.create_rectangle(
                j * cell_size, i * cell_size,
                (j + 1) * cell_size, (i + 1) * cell_size,
                outline=border_arry[i][j], fill=color_arry[i][j], width=3
            )        

#/////////////////توابع التحقق/////////////////
    def on_gool(self,level,rowG,colG,valu):
        if round((level[rowG][colG])-int(level[rowG][colG]),1)*10==valu:
            return True
        else:
            return False
    
    def Moving_stones(self,level):
        Moving=[]
        rows = len(level)
        cols = len(level[0])
        for i in range(rows):
            for j in range(cols):  
                if int(level[i][j]) !=1 and int(level[i][j]) !=0:
                    Moving.append ((i,j))
        return Moving
    
    def is_blok(self,level, row, col):
        if (round((level[row][col])-int(level[row][col]),1))== 0.1: 
            return True
        elif int(level[row][col]) != 0: 
            return True
        return False
      
#////////////////توابع الحركة//////////////////////
    def move_right(self,canvas):
        print('rt')
        level = copy.deepcopy(self.naw_level)
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
        return total_weight,level
       # self.update_and_store_level(level,canvas,"right")

    def move_left(self, canvas):
        level = copy.deepcopy(self.naw_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
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
            level[row_level][col_level] = round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
            if(self.on_gool(level,row_level,new_col,old_cell)):
                level[row_level][new_col]=0.0
            else:
                level[row_level][new_col] = level[row_level][new_col]+int(old_cell)
        return level
        #self.update_and_store_level(level,canvas, "left")
  
    def move_up(self, canvas):
        level= copy.deepcopy(self.naw_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
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
            level[row_level][col_level] = round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
            if(self.on_gool(level,new_row,col_level,old_cell)):
                level[new_row][col_level]=0.0
            else:
                level[new_row][col_level] =  level[new_row][col_level]+int(old_cell)
        return level
        #self.update_and_store_level(level, canvas,"up")

    def move_down(self, canvas):
        level = copy.deepcopy(self.naw_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
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
            level[row_level][col_level] =round(level[row_level][col_level]-int(level[row_level][col_level]),1)
            if(self.on_gool(level,new_row,col_level,old_cell)):
                level[new_row][col_level]=0.0
            else:
                level[new_row][col_level] =  level[new_row][col_level]+int(old_cell)
        return level
        #self.update_and_store_level(level, canvas,"down")

    def get_possible_moves(self):
        moves = []
        moveable_stones = self.Moving_stones(self.naw_level)
        for stone in moveable_stones:
            row, col = stone
            if col + 1 < len(self.naw_level[0]) and not self.is_blok(self.naw_level, row, col + 1):
                moves.append(("right", row, col))
            if col - 1 >= 0 and not self.is_blok(self.naw_level, row, col - 1):
                moves.append(("left", row, col))
            if row - 1 >= 0 and not self.is_blok(self.naw_level, row - 1, col):
                moves.append(("up", row, col))
            if row + 1 < len(self.naw_level) and not self.is_blok(self.naw_level, row + 1, col):
                moves.append(("down", row, col))
        return moves
   
    def bfs(self,canvas):
        queue = [] 
        paths=[]
        list_paths=[copy.deepcopy(self.naw_level)]
        next_moves = self.get_possible_moves()
        grouped_moves = {"right": [], "left": [], "up": [], "down": []}        
        for move in next_moves:
            direction, row, col = move
            grouped_moves[direction].append((row, col))
        added_directions=[]            
        for direction, positions in grouped_moves.items():
            for position in positions:
                if direction not in added_directions:
                    queue.append(direction)
                    added_directions.append(direction)
        visited = []
        visited_count = 0             
        while queue:
            visited.append(copy.deepcopy(self.naw_level))        
            if not self.Moving_stones(self.naw_level):
                return(paths,self.make_move(canvas,list_paths,1000))
            else: 
                path = queue.pop(0)
                visited_count += 1 
                if path == "right":
                   nextlevel= self.move_right(canvas)
                if path == "left":
                    nextlevel=self.move_left(canvas)
                if path == "up":
                    nextlevel=self.move_up(canvas)
                if path == "down":
                    nextlevel=self.move_down(canvas)
                if nextlevel in visited:
                    continue
                else:
                    paths.append(path)
                    list_paths.append(copy.deepcopy(nextlevel))
                    self.update_and_store_level(nextlevel, canvas, "new_level", delay=5000)
                    next_moves = self.get_possible_moves()
                    grouped_moves = {"right": [], "left": [], "up": [], "down": []}        
                    for move in next_moves:
                        direction, row, col = move
                        grouped_moves[direction].append((row, col))
                    added_directions=[]            
                    for direction, positions in grouped_moves.items():
                        for position in positions:
                            if direction not in added_directions:
                                queue.append(direction)
                                added_directions.append(direction)

    def dfs(self,canvas):
        stack = [] 
        paths=[]
        list_paths=[copy.deepcopy(self.naw_level)]
        next_moves = self.get_possible_moves()
        grouped_moves = {"right": [], "left": [], "up": [], "down": []}        
        for move in next_moves:
            direction, row, col = move
            grouped_moves[direction].append((row, col))
        added_directions=[]            
        for direction, positions in grouped_moves.items():
            for position in positions:
                if direction not in added_directions:
                    stack.append(direction)
                    added_directions.append(direction)
        visited = []
        visited_count = 0             
        while stack:
            visited.append(copy.deepcopy(self.naw_level))        
            if not self.Moving_stones(self.naw_level):
                return(paths,self.make_move(canvas,list_paths,1000))
            else: 
                path = stack.pop(0)
                visited_count += 1 
                if path == "right":
                   nextlevel= self.move_right(canvas)
                if path == "left":
                    nextlevel=self.move_left(canvas)
                if path == "up":
                    nextlevel=self.move_up(canvas)
                if path == "down":
                    nextlevel=self.move_down(canvas)
                if nextlevel in visited:
                    continue
                else:
                    paths.append(path)
                    list_paths.append(copy.deepcopy(nextlevel))
                    self.update_and_store_level(nextlevel, canvas, "new_level", delay=5000)
                    next_moves = self.get_possible_moves()
                    grouped_moves = {"right": [], "left": [], "up": [], "down": []}        
                    for move in next_moves:
                        direction, row, col = move
                        grouped_moves[direction].append((row, col))
                    added_directions=[]            
                    for direction, positions in grouped_moves.items():
                        for position in positions:
                            if direction not in added_directions:
                                stack.append(direction)
                                added_directions.append(direction)

    def make_move(self, canvas, list_path, delay=500,i=0):
            if i >= len(list_path):
                print("Completed drawing all states!")
                return
            canvas.delete("all") 
            self.draw_Squares(list_path[i], canvas)
            for row in list_path[i]:
                print(row)
            print("-" * 20)
            canvas.after(delay, lambda: self.make_move(canvas, list_path, delay, i + 1))

    # def solve(self, canvas, algorithm="bfs"):
    #     if algorithm.lower() == "bfs":
    #        return( self.bfs(canvas))
    #     elif algorithm.lower() == "dfs":
    #         return( self.dfs(canvas))
    #     else:
    #         print("خوارزمية غير مدعومة")

    def solve_uniform_cost(self, canvas):
        queue = []
        paths = []
        list_opject = [copy.deepcopy(self.naw_level)]
        start_cost = 0
        next_moves = self.get_possible_moves()
        for move in next_moves:
            queue.append(move)

        visited = []
        visited_count = 0

        while queue:
            visited.append(copy.deepcopy(self.naw_level))
            if not self.Moving_stones(self.naw_level):
                return (paths, self.make_move(canvas, list_paths, 1000))
            else:
                queue.sort(key=lambda x: x[-1]) 
                print(queue)
                move = queue.pop(0)
                #current_cost = move[3]
                visited_count += 1
                print(move)
                direction, _, _ = move
                print(direction)
                if direction == "right":
                    next_level = self.move_right(canvas)
                elif direction == "left":
                    next_level = self.move_left(canvas)
                elif direction == "up":
                    next_level = self.move_up(canvas)
                elif direction == "down":
                    next_level = self.move_down(canvas)

                if next_level in visited:
                    continue
                else:
                    paths.append(direction)
                    start_cost =+1
                    list_paths.append(copy.deepcopy(next_level))
                    self.update_and_store_level(next_level, canvas, "new_level", delay=5000)
                    next_moves = self.get_possible_moves(current_cost)
                    for move in next_moves:
                        queue.append(move)