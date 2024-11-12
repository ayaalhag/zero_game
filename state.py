import chek
class state:
    def draw_Squares(self,level, canvas):
        rows = len(level)
        cols = len(level[0])
        cell_size = 50

        canvas.delete("all")   
        for i in range(rows):
            for j in range(cols):            
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
#border               
                if (round((level[i][j])-int(level[i][j]),1))== 0.1:
                    border="black"
                elif(round((level[i][j])-int(level[i][j]),1))== 0.2:
                    border="green"            
                elif(round((level[i][j])-int(level[i][j]),1))== 0.3:
                    border="blue"     
                elif(round((level[i][j])-int(level[i][j]),1))== 0.4:
                    border="red"             
                else:
                    border=color
                    
                canvas.create_rectangle(j * cell_size, i * cell_size,
                                        (j + 1) * cell_size, (i + 1) * cell_size,
                                        outline = border, fill=color, width=3)

        #قادرة على التنقل
    
    def move_right(level, canvas):
        move=chek.Moving_stones(level)
        Nrow_move = len(move)
        for r in range(Nrow_move):
                Ncols_level=len(level[0])
                col_level=move[r][1]
                row_level=move[r][0]
                new_col =col_level 
                old_cell = level[row_level][col_level]
                #هي بتمشي ع مصفوفة level
                for j in range(col_level + 1, Ncols_level):
                    if chek.is_blok(level, row_level, j): 
                        break 
                    else:
                        new_col = j 
                level[row_level][col_level] = 0  
                if(chek.gool(level,row_level,new_col,old_cell)):
                 level[row_level][new_col]=0.0
                else:
                 level[row_level][new_col] = old_cell
        level.draw_Squares(level, canvas)
