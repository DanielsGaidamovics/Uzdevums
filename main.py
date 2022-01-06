ter=float(input("Ievadi līguma termiņu: "))
skait1=int(input("Ievadi iepreikšējo skaitītāju rādījumu: "))
skait2=int(input("Ievadi esošo skaitītāju rādījumu: "))
kWh=skait2-skait1
def maksa(ter, kwh):
  summa = 0
  if ter==1:
    summa=0.20159*kWh
  elif ter==2:
    summa=0.16961*kWh
  elif ter==3:
    summa=0.16427*kWh
  elif ter==4:
    summa=0.15964*kWh
  else:
    print("Ir ievadīts nepareizs līguma termiņš")
  print(summa)
  
maksa(ter, kWh)