class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.n = len(data)         
        self.r = int(self.n**0.5)
    def isSafe(self,x,y):
        print (self.data[x][y])
        if self.data[x][y] not in range(1,self.n + 1) or type(self.data[x][y]) == bool or  type(self.data[x][y]) == str:
            return False


        for row in range(self.n):
            if row != x and self.data[x][y] == self.data[row][y]:
                return False
        for col in range(self.n):
            if col != y and self.data[x][y] == self.data[x][col]:
                return False
        start_x = self.r * (x//self.r) 
        start_y = self.r *(y//self.r)
        
        for row in range(start_x,start_x + self.r):
            for col in range(start_y,start_y + self.r):
                if row != x and  col != y and self.data[x][y] == self.data[row][col]:
                    return False
        return True
        
        
    def is_valid(self):
        print (self.data)
        if not self.data and self.m != self.n :
            return False
        
        for row in  self.data:
            if len(row) != self.n:
                return False


        for row in range(self.n):
            for col in range(self.n):
                if not self.isSafe(row,col):
                    return False
                    
        return True