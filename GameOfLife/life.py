#life
#game of life
import random
import numpy as np


def main():
    #Random initialization
    grid = init_grid(GRID_SIZE)
    
    for i in range(10):
        #print(count_neighbors(grid,i,2))
        grid = evolve(grid, GRID_SIZE)
        print(print_grid(grid), end='\r')
        print("--------------------------------")

def init_grid(GRID_SIZE):
    grid = np.ones((GRID_SIZE,GRID_SIZE))
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            grid[i][j]= random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    return grid

def count_neighbors(grid, i, j):
    counter=0
    lg = len(grid[0])-1
    if i==0:
        if j==0:
            for k in [lg,0,1]:
                for l in [lg,0,1]:
                    counter+=grid[i+k][j+l]
        elif j==lg:
            for k in [lg,0,1]:
                for l in [-1,0,-lg]:
                    counter+=grid[i+k][j+l]
        else:
            for k in [lg,0,1]:
                for l in [-1,0,1]:
                    counter+=grid[i+k][j+l]
    elif i==lg:
        if j==0:
            for k in [-lg,0,-1]:
                for l in [0,1,lg]:
                    counter+=grid[i+k][j+l]
        elif j==lg:
            for k in [-lg,0,-1]:
                for l in [-1,0,-lg]:
                    counter+=grid[i+k][j+l]
        else:
            for k in [-lg,0,-1]:
                for l in [-1,0,1]:
                    counter+=grid[i+k][j+l]
    else:
        if j==0:
            for k in [-1,0,1]:
                for l in [1,0,lg]:
                    counter+=grid[i+k][j+l]
        elif j==lg:
            for k in [-1,0,1]:
                for l in [-1,0,-lg]:
                    counter+=grid[i+k][j+l]
        else:
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    counter+=grid[i+k][j+l]
    return int(counter - grid[i][j])
#check count beighbor function
            
 

def evolve(grid, GRID_SIZE):
    new_grid = np.ones((GRID_SIZE,GRID_SIZE))
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            neigh = count_neighbors(grid, i, j)
            if grid[i][j]==1:
                #count neighbors
                if neigh != 2 and neigh !=3:
                    new_grid[i][j]=0
                else:
                    new_grid[i][j]=1
            else:#grid is 0
                if neigh == 3:
                    new_grid[i][j]=1
                else:
                    new_grid[i][j]=0
    return new_grid

def terminal(grid, GRID_SIZE):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 1:
                return False
    return True

def print_grid(grid):
    lg = len(grid[0])
    line = ''
    for i in range(lg):
        for j in range(lg):
            if grid[i][j]==1:
                line += "*"
            else:

                line += " "
        line += "\n"
    return line

if __name__ == "__main__":
    main()