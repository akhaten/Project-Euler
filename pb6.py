# https://projecteuler.net/problem=6

def sum_k(n):
  return (n*(n+1))//2

def sum_k2(n):
  return (n*(n+1)*(2*n+1))//6

def f(n):
  return (sum_k(n)**2)-sum_k2(n)

print(f(100))