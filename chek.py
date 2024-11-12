#قادرة على التنقل
def Moving_stones(level):
    Moving=[]
    rows = len(level)
    cols = len(level[0])
    for i in range(rows):
        for j in range(cols):  
            if int(level[i][j]) !=1 and int(level[i][j]) !=0:
                 Moving.append ((i,j))
    return Moving

# الحواجز
def is_blok(level, row, col):
    if (round((level[row][col])-int(level[row][col]),1))== 0.1: 
        return True
    elif int(level[row][col]) != 0: 
        return True
    return False
  

#الهدف
def gool(level,rowG,colG,valu):
    if round((level[rowG][colG])-int(level[rowG][colG]),1)*10==valu:
        return True
    else:
     return False
