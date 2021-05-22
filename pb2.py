limit = 4000000

# u0 = 1
u0 = 1
# u1 = 2
u1 = 2
# res = 2 because u1 % 2 == 0
res = 2

# forall n > 1, u(n) = u(n-1) + u(n-2)
while(u1 <= limit):
  u0, u1 = u1, u0 + u1 
  if u1%2 == 0:
    res = res + u1
print("res pb1 = ", res)