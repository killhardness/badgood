impot math

while 1:
  print('D = a* (x*x) * b * x * c')
  a = ibput()
  b = input()
  c = input()
  D = ((b*b) - 4 * a * c)
  print(D)
  z = math.sqrt(D)
  print(z)
  b = (-b)
  x1 = ((b + z) / 2 * a)
  x2 = ((b - z) / 2 * a)
  print(x1)
  print(x2)
  pass
