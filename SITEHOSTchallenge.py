for x in range(1,101): 
  if x % 15 == 0:
   print("SiteHost")
  elif x % 5 == 0:
    print("Host")
  elif x % 3 == 0: 
    print("Site")
  else:
    print(x)