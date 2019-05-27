# Maze Runner

##　Task
You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given. If you reach the end point before all your moves have gone, you should return Finish. If you hit any walls or go outside the maze border, you should return Dead. If you find yourself still in the maze after using all the moves, you should return Lost.</br>

The Maze array will look like</br>

```
maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]
```

..with the following key

```
 	0 = Safe place to walk
    1 = Wall
    2 = Start Point
    3 = Finish Point
```

```
    direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
```

##　Rules
```
1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.
2. The start and finish positions will change for the final tests.
3. The directions array will always be in upper case and will be in the format of N = North, E = East, W = West and S = South.
```  
## Solution

<sol>首先先找到出發點,接著跟著移動,撞牆會超出範圍就會死,步伐走完沒到出口就算Lost
```python
def maze_runner(maze, directions):
    dic_row={"N":-1,"S":1}
    dic_col={"E":1,"W":-1}
    max_row,max_col=len(maze),len(maze[0])   
    for i in range(max_row):        
        if 2 in maze[i]:            
            row,col=i,maze[i].index(2)
            break  

    for dire in directions:
        row+=dic_row.get(dire,0)
        col+=dic_col.get(dire,0)    
        if row < 0 or col <0 or max_row <=row or max_col<=col or maze[row][col]==1: 
            return "Dead"   
        if maze[row][col]==3:
            return "Finish"
    return "Lost"


```