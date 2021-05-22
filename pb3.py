def f(n):
  res = 2
  div = 2
  while div <= n:
    if n%div == 0:
      if(div > res):
        res = div
      while(n%div == 0):
        n = n/div
    div += 1
  return res

print(f(600851475143))