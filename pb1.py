limit = 1000
res = 0
for i in range(0, limit):
  if (i%3 == 0) or (i%5 == 0):
    res += i
print("res pb1 = ", res)