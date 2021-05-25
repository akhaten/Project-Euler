def pow(x,n):
  if n == 1:
    return x
  if n%2 == 0:
    return pow(x * x, n/2)
  return x * pow(x * x, (n-1)/2)

def sumDigitN(n, acc):
  if n < 1 :
    return acc
  q = n//10
  r = n%10
  return sumDigitN(q, acc+r)

def f():
  return sumDigitN(pow(2,1000), 0)



print(f())