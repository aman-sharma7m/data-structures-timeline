import numpy as np

maze=np.array([ [1,0,1],
                [1,1,0],
                [0,1,1]])
sol=np.zeros((3,3))

def isSafe(i,j,maze):
  return (i<maze.shape[0] and j<maze.shape[1]
          and maze[i][j]==1)

def prg_1(maze,sol,i=0,j=0):
  '''
  backtracking maze puzzle soln

  '''
  if i==maze.shape[0]-1 and j==maze.shape[1]-1:
    sol[i][j]=1
    return True
  if isSafe(i,j,maze)==True:
    sol[i][j]=1
    if prg_1(maze,sol,i+1,j):
      return True
    elif prg_1(maze,sol,i,j+1):
      return True
    sol[i][j]=0
  return False


def solve_prg_1():
  '''
  program to solve the maze
  '''

  if prg_1(maze,sol,0,0)==False:
    return False
  else:
    print(sol)
    return True




def prg_2(maze,sol_mat,0):
  


def solve_prg_2(maze,n:int):
  '''
  program to solve the queen maze prob
  '''
  sol_mat=np.zeros((n,n))
  if prg_2(maze,sol_mat,0,0)==False:
    return False
  else:
    print(sol_mat)
    return True
  


    

if __name__=='__main__':
  maze=
  print(solve_prg_1(maze,3))
  

