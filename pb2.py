def f(n):
  
  u0 = 1
  u1 = 2
  res = 2

  while(u1 <= n):
    u0, u1 = u1, u0 + u1 
    if u1%2 == 0:
      res = res + u1
  
  return res

print(f(4000000))