# https://projecteuler.net/problem=7

import math

def isPrime(n):
  
  root_n = int(math.sqrt(n)) + 1
  check = (n != 1)
  div = 2

  while( check and (div < root_n) ):
    check = (n%div != 0)
    div += 1

  return check


def findNPrimeNumber(n):
  
  last = 2
  count = 1
  k = 1
  
  while(last != 104743):
    toAdd = 2*k+1
    if(isPrime(toAdd)):
      last = toAdd
      count += 1
    k += 1

  return last



print(findNPrimeNumber(10001))

  