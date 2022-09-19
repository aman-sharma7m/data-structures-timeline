
def prg_1(n:int):
  '''
  program-1:
  input - n | output - n n-1 n-2 ..... 1,n-2,n-1,n 
  ex: n=3 | op: 3,2,1,1,2,3
  '''
  if n==0:
    return 
  print(n,end=',')
  prg_1(n-1)
  print(n,end=',')

def prg_2(n:int):
  '''
  ip: n
  op: n n-1 n-2 ... 1
  '''
  if n==0:
    return 
  print(n,end=' ')
  prg_2(n-1)

def prg_3(n:int):
  '''
  ip: n
  op: 1 2 3 ... n
  Tail-recursive solution
  '''
  if n==0:
    return 
  prg_3(n-1)
  print(n,end=' ')

def prg_4(n:int,k=1):
  '''
  ip: n
  op: 1 2 3 ... n
  Non-Tail-recursive-solution
  '''
  if n==0:
    return 
  print(k,end=' ')
  prg_4(n-1,k+1)


def prg_5(n:int,k=1):
  '''
  factorial
  Non-Tail-recursive-solution
  '''
  if n==0 or n==1:
    return k
  return prg_5(n-1,k*n)

def prg_6(n:int,k=1):
  '''
  n natural number sum
  Non-Tail-recursive-solution
  '''
  if n<1:
    return 0
  if n==1:
    return k
  return prg_6(n-1,k+n)

  



if __name__=='__main__':
  print(prg_6(0))
  print()

