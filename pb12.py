# https://projecteuler.net/problem=12

import math

def computeTriangleNumber(n):
  return int(n*(n+1)/2)

def countDivs(n):

  
  div_down = n
  div_up = 1
  count = 0

  if n == 1:
    return 1

  while(div_up < div_down):
    if(n%div_up == 0):
      div_down = int(n/div_up)
      count += 2
    div_up += 1

  return count


def findFirstNDivs(n):
  
  
  nbDivs = 1
  i = 1

  while(nbDivs < n):
    number = computeTriangleNumber(i)
    nbDivs = countDivs(number)
    i += 1
  
  return number



print(findFirstNDivs(500))