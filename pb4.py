def reverseNumber(n, acc=0):
  
  q = n//10
  r = n%10
  acc = acc*10+r
  
  if(n < 10):
    return acc
  
  return reverseNumber(q, acc)

def isNumberPalindromic(n):
  return n == reverseNumber(n)

def f(digit_number):
  
  inf = 10**(digit_number-1)
  sup = 10**digit_number
  res = 0

  for a in range(inf, sup):
    for b in range(a, sup):
      dot = a * b
      if(isNumberPalindromic(dot) and (res < dot)):
        res = dot

  return res

print(f(3))





