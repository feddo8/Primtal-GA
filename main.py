import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))
from math import sqrt
primtal = [2,3]
n=3
while True:
  n+=2
  delbar = False
  sqrtn = sqrt(n)
  for nummer in primtal:
    if n % nummer == 0:
      delbar = True
    if nummer > sqrtn:
      break
  
  if delbar == False:
    primtal.append(n)
  if n > 2500000:
    break
now1 = datetime.datetime.now()
for nummer in primtal:
  print(nummer)

print (now.strftime("%Y-%m-%d %H:%M:%S"))
print (now1.strftime("%Y-%m-%d %H:%M:%S"))

