# https://projecteuler.net/problem=10

import math

def isPrime(n):
  
  root_n = int(math.sqrt(n)) + 1
  check = (n != 1)
  div = 2

  while( check and (div < root_n) ):
    check = (n%div != 0)
    div += 1

  return check

def sumPrimeNumberBelow(n):

  toAdd = 2
  sum = 2
  k = 1

  while(toAdd < n-1):
    toAdd = 2*k+1
    if(isPrime(toAdd)):
      sum += toAdd
    k += 1

  return sum



print(sumPrimeNumberBelow(2000000))

  
