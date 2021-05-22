# https://projecteuler.net/problem=5

def checkDivs(inf, sup, n):
  
  check = True
  div = inf
  
  while( check and (div < (sup+1)) ):
    check = (n%div == 0)
    div += 1

  return check

def f():

  inf = 1
  sup = 20
  n = sup
  
  while(not checkDivs(inf, sup, n)):
    n += sup
  
  return n

print(f())
