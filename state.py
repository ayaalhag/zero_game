import copy
import heapq
from colorama import Fore,Back,Style,init
import logging
import time
import tracemalloc

logging.basicConfig(
    filename="solver.log", 
    level=logging.INFO,    
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class state:
    def __init__(self, level):
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
                elif int(level[i][j]) == 5:
                    color="pink"
                elif int(level[i][j]) == 6:
                    color="yellow"
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
                elif decimal_part==0.5:
                    border="pink"
                elif decimal_part==0.6:
                    border="yellow"
                elif decimal_part== 0.8:
                    border ="gray"
                else:
                    border = color
                border_arry[i][j] = border
        return color_arry, border_arry
       
    def draw_Squares(self, level, canvas):
        color_arry = self.represent_Squares(level)[0]
        border_arry = self.represent_Squares(level)[1]
        rows = len(level)
        cols = len(level[0])
        cell_size = 50
        for i in range(rows):
            for j in range(cols):
                x0 = j * cell_size
                y0 = i * cell_size
                x1 = (j + 1) * cell_size
                y1 = (i + 1) * cell_size
                
                # رسم المستطيل مع الإطار واللون الداخلي
                canvas.create_rectangle(
                    x0, y0, x1, y1,
                    outline=border_arry[i][j], fill=color_arry[i][j], width=3
                )
                
    def move_right(self):
        cost=0
        level = copy.deepcopy(self.now_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
        for r in range(Nrow_move):
                Ncols_level=len(level[0])
                col_level=move[r][1]
                row_level=move[r][0]
                new_col =col_level 
                old_cell = int(level[row_level][col_level])
                #هي بتمشي ع مصفوفة level
                for j in range(col_level+1 , Ncols_level):
                    if self.is_blok(level, row_level, j): 
                        break 
                    elif self.on_gool(level, row_level, j, old_cell):
                        level[row_level][j] = 0.0
                        level[row_level][col_level] =round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
                        cost+=abs(col_level-new_col)
                        object=state(level)
                        return object,cost
                    elif self.is_grey(level,row_level,j):
                        level[row_level][col_level]=round(level[row_level][col_level] - old_cell, 1)
                        level[row_level][j]=old_cell+(old_cell/10) 
                        cost+=abs(new_col-col_level)
                        object=state(level)
                        return object ,cost   
                    else:
                        new_col = j 
                level[row_level][col_level] = round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
                level[row_level][new_col] = level[row_level][new_col]+int(old_cell)
                cost+=abs(col_level-new_col)
        object=state(level)
        return object,cost
    
    def move_left(self):
        cost=0
        level = copy.deepcopy(self.now_level)
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
              elif self.on_gool(level, row_level, j, old_cell):
                level[row_level][j] = 0.0
                level[row_level][col_level] =round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
                cost+=abs(col_level-new_col)
                object=state(level)
                return object,cost
              elif self.is_grey(level,row_level,j):
                level[row_level][col_level]=round(level[row_level][col_level] - old_cell, 1)
                level[row_level][j]=old_cell+(old_cell/10) 
                cost+=abs(new_col-col_level)
                object=state(level)
                return object ,cost  
              else:
                new_col = j
            level[row_level][col_level] = round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
            level[row_level][new_col] = level[row_level][new_col]+int(old_cell)
            cost+=abs(col_level-new_col)
        object=state(level)
        return object,cost
    
    def move_up(self):
        cost=0
        level= copy.deepcopy(self.now_level)
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
                elif self.on_gool(level, i, col_level, old_cell):
                    level[i][col_level] = 0.0
                    level[row_level][col_level] =round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
                    cost+=abs(row_level-new_row)
                    object=state(level)
                    return object ,cost
                elif self.is_grey(level,i,col_level):
                    level[row_level][col_level]=round(level[row_level][col_level] - old_cell, 1)
                    level[i][col_level]=old_cell+(old_cell/10) 
                    cost+=abs(new_row-row_level)
                    object=state(level)
                    return object ,cost   
                else:
                  new_row = i
            level[row_level][col_level] = round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
            level[new_row][col_level] =  level[new_row][col_level]+int(old_cell)
            cost+=abs(row_level-new_row)
        object=state(level)
        return object ,cost
    
    def move_down(self):
        cost=0
        level = copy.deepcopy(self.now_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
        for r in range(Nrow_move):
            col_level=move[r][1]
            row_level=move[r][0]
            rows = len(level)
            new_row = row_level
            old_cell = int(level[row_level][col_level])
            for i in range(row_level + 1, rows):
            #   self.print_level(level)
              if self.is_blok(level, i, col_level):
                break
              elif self.on_gool(level, i, col_level, old_cell):
                level[i][col_level] = 0.0
                level[row_level][col_level] =round(level[row_level][col_level] - old_cell, 1)
                cost+=abs(new_row-row_level)
                object=state(level)
                return object ,cost
              elif self.is_grey(level,i,col_level):
                level[row_level][col_level]=round(level[row_level][col_level] - old_cell, 1)
                level[i][col_level]=old_cell+(old_cell/10) 
                cost+=abs(new_row-row_level)
                object=state(level)
                return object ,cost 
              else:
                new_row = i        
            level[row_level][col_level] = abs (round(level[row_level][col_level] - old_cell, 1))
            level[new_row][col_level] += old_cell
            cost+=abs(new_row-row_level)
        object=state(level)
        return object ,cost
      
    def Moving_stones(self, level):
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

    def get_possible_moves(self,level):
        moves =set()
        moveable_stones = self.Moving_stones(level)
        for stone in moveable_stones:
            row, col = stone
            if col + 1 < len(level[0]) and not self.is_blok(level, row, col + 1):
                moves.add(("right"))
            if col - 1 >= 0 and not self.is_blok(level, row, col - 1):
                moves.add(("left"))
            if row - 1 >= 0 and not self.is_blok(level, row - 1, col):
                moves.add(("up"))
            if row + 1 < len(level) and not self.is_blok(level, row + 1, col):
                moves.add(("down"))
        return list(moves)
  
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

    def is_grey(self,level, row , col):
        if ((level[row][col]) - int(level[row][col])==0.8):
            return True
        else:
            return False
            
    def print_level(self,level):
        rows = len(level)
        cols = len(level[0])
        for row in range(rows):
            for col in range(cols):
                if(level[row][col]==1.1):
                    print(f"{'⬛️':^3}",end="  ")
                elif(level[row][col]==0.0):
                    print(f"{'⬜️':^3}",end="  ")
                else:
                    print(f"{level[row][col]}",end="  ")
            print()
        print("-" * 20)
    
    # def is_deed(self ,level , row ,col):
        
    def direction(self,direction):
        # print(direction)
        if direction =='down':
          new_obj,cost= self.move_down()
        if direction =='up':
            new_obj,cost= self.move_up()
        if direction =='right':
            new_obj,cost= self.move_right()
        if direction =='left':
            new_obj,cost= self.move_left()        
        return(new_obj,cost)  
     
    def hirostic(self, level):
        stones=self.Moving_stones(level)  
        rows = len(level)
        cols = len(level[0])
        distans=0
        for stone in stones:
            s_row,s_col=stone
            for row in range(rows):
                for col in range(cols):
                    if (round((level[row][col]) - int(level[row][col]), 1) * 10 == int(level[s_row][s_col])):
                        distans+=abs(row-s_row)+ abs(col-s_col)
        return( distans)
    
    def path_f_cost(self,path):
        g_cost=0
        for level,cost in path:
            g_cost+=cost
        last_level=path[-1][0]
        last_ob=state(last_level)
        h_cost=last_ob.hirostic(last_level)
        # print("h",h_cost)
        f_cost=g_cost+h_cost
        return f_cost
    
    def path_g_cost(self,path):
        g_cost=0
        for level,cost in path:
            g_cost+=cost
        return g_cost
     
    def make_move(self, canvas, list_path, delay=500,i=0):
            if i >= len(list_path):
                print("Completed drawing all states!")
                return
            canvas.delete("all")
            canvas.after(delay, lambda: self.make_move(canvas, list_path,delay,i + 1))
 
    def solve(self, canvas, algorithm="bfs"):
        if algorithm.lower() == "bfs":
           return( self.bfs(canvas))
        elif algorithm.lower() == "dfs":
            return( self.dfs(canvas))
        elif algorithm=="UCS":
            return( self.UCS(canvas))
        elif algorithm=="A_star":
            return(self.A_star(canvas))
        else:
            print("خوارزمية غير مدعومة")
            
    def bfs(self,canvas):
        tracemalloc.start() 
        start_time = time.time() 
        queue = [[self.now_level]] 
        visited = [] 
        i=0           
        while queue:
            print(i)
            i+=1
            path=queue.pop(0)
            level=path[-1]
            if level in visited:
                continue
            visited.append(copy.deepcopy(level))
            currunt_obj=state(level)        
            if not self.Moving_stones(currunt_obj.now_level):
                end_time = time.time() 
                memory_used, _ = tracemalloc.get_traced_memory()
                for n in path:
                    self.print_level(n)
                logging.info(
                    f"Algorithm: BFS | Nodes Visited: {len(visited)} | Path Length: {len(path)} "
                    f"| Time: {end_time - start_time:.4f}s | Memory: {memory_used / 1024:.2f} KB"
                )
                
                tracemalloc.stop()
                return("done")
            else: 
                next_moves=currunt_obj.get_possible_moves(currunt_obj.now_level)
                for move in next_moves:
                    new_obj,_= currunt_obj.direction(move)
                    new_path=path.copy()
                    new_path.append(new_obj.now_level)
                    queue.append(new_path)
        end_time = time.time()
        memory_used, _ = tracemalloc.get_traced_memory()
        logging.info(
            f"Algorithm: BFS | Nodes Visited: {len(visited)} | Path Length: {len(queue)} "
            f"| Time: {end_time - start_time:.4f}s | Memory: {memory_used / 1024:.2f} KB"
        )
        tracemalloc.stop()
        return "not found solution"
                   
    def dfs(self,canvas):
        tracemalloc.start() 
        start_time = time.time() 
        stack = [[self.now_level]] 
        visited = []            
        while stack:
            path=stack.pop()
            level=path[-1]
            if level in visited:
                continue
            visited.append(copy.deepcopy(level))
            currunt_obj=state(level)        
            if not self.Moving_stones(currunt_obj.now_level):
                end_time = time.time() 
                memory_used, _ = tracemalloc.get_traced_memory()  
                for n in path:
                    self.print_level(n)
                logging.info(
                f"Algorithm: DFS | Nodes Visited: {len(visited)} | Path Length: {len(path)} "
                f"| Time: {end_time - start_time:.4f}s | Memory: {memory_used / 1024:.2f} KB"
                )
                tracemalloc.stop()
                return("done")
            else: 
                next_moves=currunt_obj.get_possible_moves(currunt_obj.now_level)
                for move in next_moves:
                    new_obj,_= currunt_obj.direction(move)
                    new_path=path.copy()
                    new_path.append(new_obj.now_level)
                    stack.append(new_path)
        end_time = time.time()
        memory_used, _ = tracemalloc.get_traced_memory()
        logging.info(
            f"Algorithm: DFS | Nodes Visited: {len(visited)} | Path Length: {len(stack)} "
            f"| Time: {end_time - start_time:.4f}s | Memory: {memory_used / 1024:.2f} KB"
        )
        tracemalloc.stop()
        return "not found solution"
    
    def UCS(self, canvas):
        tracemalloc.start() 
        start_time = time.time() 
        Pq = [[(self.now_level,0)]] 
        visited = [] 
        i=0 
        while Pq:
            Pq=sorted(Pq, key=lambda path_s:self.path_g_cost(path_s))
            print(i)
            i+=1
            # for n in Pq:
            #     for tu in n:
            #         print('cost=', tu[1])
            #         # self.print_level(tu[0])
            #         # print('visited',len(visited))
            #         # print('path',len(path))
            #     print('*'*20)
            path=Pq.pop(0)
            level=path[-1][0]
            self.cost=path[-1][1]
            if level in visited:
                continue 
            visited.append(copy.deepcopy(level))
            currunt_obj=state(level)
            if not currunt_obj.Moving_stones(currunt_obj.now_level):
                end_time = time.time() 
                memory_used, _ = tracemalloc.get_traced_memory()  
                for level,cost in path:
                    self.print_level(level)
                logging.info(
                f"Algorithm: UCS | Nodes Visited: {len(visited)} | Path Length: {len(path)} "
                f"| Time: {end_time - start_time:.4f}s | Memory: {memory_used / 1024:.2f} KB"
                )
                tracemalloc.stop()
                return "done"
            else:  
                next_moves=currunt_obj.get_possible_moves(currunt_obj.now_level)
                for move in next_moves:
                   new_obj,cost= currunt_obj.direction(move)
                   new_path=path.copy()
                   new_path.append((new_obj.now_level,cost))
                   Pq.append(new_path)
        end_time = time.time()
        memory_used, _ = tracemalloc.get_traced_memory()
        logging.info(
            f"Algorithm: UCS | Nodes Visited: {len(visited)} | Path Length: {len(stack)} "
            f"| Time: {end_time - start_time:.4f}s | Memory: {memory_used / 1024:.2f} KB"
        )
        tracemalloc.stop()
        return "not found solution"
            
    def A_star(self, canvas):
        tracemalloc.start() 
        start_time = time.time()  
        Pq = [[(self.now_level,0)]] 
        visited = [] 
        i=0 
        while Pq:
            print(i)
            Pq=sorted(Pq, key=lambda path_s:self.path_f_cost(path_s))
            path=Pq.pop(0)
            # for n in path:
            #   self.print_level(n[0])
            level=path[-1][0]
            self.cost=path[-1][1]
            if level in visited:
                continue 
            visited.append(copy.deepcopy(level))
            currunt_obj=state(level)
            if not currunt_obj.Moving_stones(currunt_obj.now_level):
                end_time = time.time() 
                memory_used, _ = tracemalloc.get_traced_memory()  
                for level,cost in path:
                    self.print_level(level)
                logging.info(
                f"Algorithm: A_star | Nodes Visited: {len(visited)} | Path Length: {len(path)} "
                f"| Time: {end_time - start_time:.4f}s | Memory: {memory_used / 1024:.2f} KB"
                )
                tracemalloc.stop()
                return "done"
            else:  
                next_moves=currunt_obj.get_possible_moves(currunt_obj.now_level)
                for move in next_moves:
                   new_obj,cost= currunt_obj.direction(move)
                   new_path=path.copy()
                   new_path.append((new_obj.now_level,cost))
                   Pq.append(new_path)
                # for n in path: 
                #     print('cost=', n[1])
                #     self.print_level(n[0])
                #     # print('visited',len(visited))
                #     # print('path',len(path))
                # print('*'*20)
            i+=1
        end_time = time.time()
        memory_used, _ = tracemalloc.get_traced_memory()
        logging.info(
            f"Algorithm: A_star | Nodes Visited: {len(visited)} | Path Length: {len(stack)} "
            f"| Time: {end_time - start_time:.4f}s | Memory: {memory_used / 1024:.2f} KB"
        )
        tracemalloc.stop()
        return "not found solution"
        
    # def hill_climbing(self,starting_point, step_size, max_iterations):
    #     now_object=self.now_level
    #     current_hirostic=0
    #     while :
    #     moves = self.get_possible_moves(now_object)
    #     for next in moves:
    #        new_obj,_ = self.direction(next)
    #        next_hirostic=self.hirostic(new_obj.now_level)
    #        if next_hirostic > current_hirostic:
    #             current_object = state(now_object)
    #             current_hirostic = next_hirostic

    #     for _ in range(max_iterations):
    #         neighbors = [current_point + step_size, current_point - step_size]            
    #         next_point = max(neighbors, key=objective_function)
    #         next_value = objective_function(next_point)
            
    #         if next_value > current_value:
    #             current_point = next_point
    #             current_value = next_value
    #         else:
    #             break  

    #     return current_point, current_value
                        

         