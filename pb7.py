# https://projecteuler.net/problem=7

def isPrime(liste, n):
  
  check = True
  size = len(liste)
  i = 0
  while( check and (i < size) ):
    check = (n%liste[i] != 0)
    i += 1

  return check

def findNPrimeNumber(n):
  
  liste = [2]
  k = 1
  
  while(len(liste) < n):
    toAdd = 2*k+1
    if(isPrime(liste, toAdd)):
      liste.append(toAdd)
    k += 1

  return liste[n-1]



print(findNPrimeNumber(10001))

  