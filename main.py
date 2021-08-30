import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))
   
primtal = [2,3]
n=3
while True:
  n+=2
  delbar = False
  sqrt = n**(0.5)
  for nummer in primtal:
    if n % nummer == 0:
      delbar = True
    if nummer > sqrt:
      break
  
  if delbar == False:
    primtal.append(n)
  if n > 1000000:
    break

for nummer in primtal:
  print(nummer)

now1 = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print (now1.strftime("%Y-%m-%d %H:%M:%S"))

