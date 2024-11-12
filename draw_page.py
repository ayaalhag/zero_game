
# اسود حاجز 1 / 0 ابيض
#الهدف للون هو رقمه -1
#القسم العشري الاطار 
#القسم الصحيح للون
#  احمر 4 / 2 اخضر / 3 ازرق
# 

def draw_Squares(level, canvas):
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

