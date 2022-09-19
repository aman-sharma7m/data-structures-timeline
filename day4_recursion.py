#from icecream import ic


def prg_1(st,start,end):
  '''
  pallingdrome check 
  recursive-solution
  '''
  if st[start]!=st[end]:
    return False
  elif st[start]==st[end] and end-start<=1:
    return True
  return prg_1(st,start+1,end-1)

def prg_2(n,s=0):
  '''
  sum of digits 
  tail recursive-solution
  '''
  if n==0:
    return s
  
  s+=n%10  
  return prg_2(n//10,s)

def prg_3(inp_st,out_st=''):
  '''
  string subset generate 
  non-tail recursive-solution
  '''
  if inp_st=='':
    print(out_st)
    return
  
  prg_3(inp_st[1:],out_st)
  prg_3(inp_st[1:],out_st+inp_st[0])

def prg_4(inp,n,sum):
  '''
   subset sum problem generate 
  tail recursive-solution
  '''
  if n==0:
    return 1 if(sum==0) else 0
  return prg_4(inp,n-1,sum)+prg_4(inp,n-1,sum-inp[n-1])

def prg_5(s,i=0):
  '''
  all permutation printing generate 
  tail recursive-solution
  '''
  if i==len(s)-1:
    print(s,end=' ')
    return
  for j in range(i,len(s)):
    s=list(s)
    s[i],s[j]=s[j],s[i]
    s=''.join(s)
    prg_5(s,i+1)
    s=list(s)
    s[i],s[j]=s[j],s[i]
    s=''.join(s)
  

if __name__=='__main__':
  print(prg_5('abc'))
  print()
