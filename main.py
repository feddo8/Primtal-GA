import time
t0 = time.time()
from math import sqrt
primtal = [2,3]
n=3
while n < 2500000:
  n+=2
  delbar = False
  sqrtn = sqrt(n)
  for nummer in primtal:
    if n % nummer == 0:
      delbar = True
      break
    if nummer > sqrtn:
      primtal.append(n)
      break
t1 = time.time()
for nummer in primtal:
  print(nummer)

print("Time required :", t1 - t0)