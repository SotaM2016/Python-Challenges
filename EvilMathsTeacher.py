#The first number had to be printed in manually
twob = 0
oneb = 1
amount = 2
current = 0
print(0)
print(1)
while amount <= 100:
  current = twob + oneb
  print(current)
  twob = oneb
  oneb = current
  amount += 1
