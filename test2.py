import tkinter as tk
import copy
class state:
    def __init__(self,level):
        self.history = [] 
        self.naw_level=copy.deepcopy(level)
    
    def update_and_store_level(self,level_copy, canvas,string):
        self.naw_level = level_copy 
        self.history.append(copy.deepcopy(self.naw_level)) 
        self.draw_Squares(self.naw_level, canvas)
        print (string)
        for row in self.naw_level:
            print(row)
        print("-" * 20)  

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
    
    def chek_end(self,level):
       Moving_stones=self.Moving_stones(level)
       if not Moving_stones:
           print('the end')
    
    def is_blok(self,level, row, col):
        if (round((level[row][col])-int(level[row][col]),1))== 0.1: 
            return True
        elif int(level[row][col]) != 0: 
            return True
        return False
      
#////////////////توابع الحركة//////////////////////
    def move_right(self,canvas):
        level = copy.deepcopy(self.naw_level)
        move=self.Moving_stones(level)
        Nrow_move = len(move)
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
                level[row_level][col_level] = round(level[row_level][col_level] - int(level[row_level][col_level]), 1)
                if(self.on_gool(level,row_level,new_col,old_cell)):
                 level[row_level][new_col]=0.0
                else:
                 level[row_level][new_col] = level[row_level][new_col]+int(old_cell)
        self.update_and_store_level(level,canvas,"right")

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
        self.update_and_store_level(level,canvas, "left")

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
        self.update_and_store_level(level, canvas,"up")

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
        self.update_and_store_level(level, canvas,"down")
        
