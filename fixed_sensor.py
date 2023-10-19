class Sensor:
    global r_grid
    def __init__(self, x,y, radius):
        self.core_x = x
        self.core_y = y
        self.radius = radius
         
        r_grid = self.radius // 5
        
    def make_coverage(grid):
        grid[x-2][y+2] == 1
        grid[x-1][y+2] == 1
        grid[x][y+2] == 1
        grid[x+1][y+2] == 1
        grid[x+2][y+2] == 1
         
        grid[x-2][y+1] == 1
        grid[x-1][y+1] == 1
        grid[x][y+1] == 1
        grid[x+1][y+1] == 1
        grid[x+2][y+1] == 1
        
        grid[x-2][y] == 1
        grid[x-1][y] == 1
        grid[x][y] == 1
        grid[x+1][y] == 1
        grid[x+2][y] == 1
         
        grid[x-2][y-1] == 1
        grid[x-1][y-1] == 1
        grid[x][y-1] == 1
        grid[x+1][y-1] == 1
        grid[x+2][y-1] == 1
        
        grid[x-2][y-2] == 1
        grid[x-1][y-2] == 1
        grid[x][y-2] == 1
        grid[x+1][y-2] == 1
        grid[x+2][y-2] == 1
        
        grid[x][y+3] == 1
        grid[x-3][y] == 1
        grid[x+3][y] == 1
        grid[x][y-3] == 1