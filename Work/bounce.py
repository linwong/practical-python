# bounce.py
#
# Exercise 1.5

height = 100
bounce = 3/5
n = 0

while n < 10:
  height *= bounce
  n += 1
  print(n, round(height, 4))

