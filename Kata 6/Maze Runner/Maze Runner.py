def maze_runner(maze, directions):
    dic_row={"N":-1,"S":1}
    dic_col={"E":1,"W":-1}
    max_row,max_col=len(maze),len(maze[0])   
    for i in range(max_row):        
        for j in range(max_col):
            if maze[i][j]==2:
                row,col=i,j
                break  

    for dire in directions:
        row+=dic_row.get(dire,0)
        col+=dic_col.get(dire,0)    
        if row < 0 or col <0 or max_row <=row or max_col<=col or maze[row][col]==1: 
            return "Dead"   
        if maze[row][col]==3:
            return "Finish"
    return "Lost"