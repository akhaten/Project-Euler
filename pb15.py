import math

def coefBin(k,n):
  return int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))

def findNPaths(n):
  return coefBin(n, 2*n)

print(findNPaths(20))

