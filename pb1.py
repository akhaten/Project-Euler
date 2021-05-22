
def f(n):
  
  res = 0

  for i in range(0, n):
    if (i%3 == 0) or (i%5 == 0):
      res += i
  
  return res
    

print(f(1000))