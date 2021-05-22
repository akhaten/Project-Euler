# https://projecteuler.net/problem=9

def checkSumTriplet(a, b, c, n):
  return a+b+c == n

def checkDefTriplet(a, b, c):
  return (a < b < c) and (a**2 + b**2 == c**2)

def findPythagoreanTriplet(n):
  for c in range(3, n):
    for b in range(2, c):
      for a in range(1, b):
        if  checkDefTriplet(a, b, c) and checkSumTriplet(a, b, c, n) :
          return a*b*c


print(findPythagoreanTriplet(1000))
          
