# اسود حاجز 1 / 0 ابيض
#الهدف للون هو رقمه -1
# الازرق  3/ 2 هدف الازرق
# الاحمر  5/ 4 هدف الاحمر

import draw_page
import chek

# يمين
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
       
    draw_page.draw_Squares(level, canvas)


# لليسار
def move_left(level, canvas):
    move=chek.Moving_stones(level)
    Nrow_move = len(move)
    for r in range(Nrow_move):
        row_level=move[r][0]
        col_level=move[r][1]
        new_col =col_level 
        old_cell = level[row_level][col_level]
        for j in range(col_level - 1, -1, -1):
          if chek.is_blok(level, row_level, j):
            break
          else:
            new_col = j
        level[row_level][col_level] = 0
        if(chek.gool(level,row_level,new_col,old_cell)):
              level[row_level][new_col]=0.0
        else:
             level[row_level][new_col] = old_cell
    draw_page.draw_Squares(level, canvas)

# للأعلى
def move_up(level, canvas):
    move=chek.Moving_stones(level)
    Nrow_move = len(move)
    for r in range(Nrow_move):
        col_level=move[r][1]
        row_level=move[r][0]
        new_row = row_level
        old_cell = level[row_level][col_level]
        for i in range(row_level - 1, -1, -1):
            if chek.is_blok(level, i, col_level):
              break
            else:
             new_row = i
        level[row_level][col_level] =round(level[row_level][col_level]-int(level[row_level][col_level]),2)
        print(round((level[new_row][col_level])-int(level[new_row][col_level]),1)*10)
        if(chek.gool(level,new_row,col_level,old_cell)):
            level[new_row][col_level]=0.0
        else:
            level[new_row][col_level] =  int(old_cell)
    draw_page.draw_Squares(level, canvas)

# للأسفل
def move_down(level, canvas):
    move=chek.Moving_stones(level)
    Nrow_move = len(move)
    for r in range(Nrow_move):
        col_level=move[r][1]
        row_level=move[r][0]
        rows = len(level)
        new_row = row_level
        old_cell = level[row_level][col_level]
        for i in range(row_level + 1, rows):
           if chek.is_blok(level, i, col_level):
            break
           else:
            new_row = i        
        level[row_level][col_level] =round(level[row_level][col_level]-int(level[row_level][col_level]),2)
        if(chek.gool(level,new_row,col_level,old_cell)):
            level[new_row][col_level]=0.0
        else:
            level[new_row][col_level] = int(old_cell)
    draw_page.draw_Squares(level, canvas)