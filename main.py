import time
t0 = time.time()
from math import sqrt
primtal = {2,3}
n=3
while n < 1000000:
  n+=2
  sqrtn = sqrt(n)
  for primnummer in primtal:
    if n % primnummer == 0:
      break
    if primnummer > sqrtn:
      primtal.add(n)
      break
t1 = time.time()


print("Time required :", t1 - t0)