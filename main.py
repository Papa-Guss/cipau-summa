teksts = input("cipari:")
def countNumbers(teksts):
  summa = 0
  for simbols in teksts:
    summa = summa + int(simbols)
  print (summa)
  return summa
countNumbers(teksts)    