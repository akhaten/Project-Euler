def collatzTerm(n):
  if(n%2 == 0):
    return int(n/2)
  return 3*n+1

def sizeCollatzSequence(n, acc):
  if(n == 1):
    return acc
  return sizeCollatzSequence(collatzTerm(n), acc+1)

def f(n):
  
  max = sizeCollatzSequence(1, 1)
  indice_max = 1
  i = 2

  while(i < n):
    tmp = sizeCollatzSequence(i, 1)
    if(max < tmp):
      max = tmp
      indice_max = i
    i+= 1
  
  return indice_max

print(f(1000000))

