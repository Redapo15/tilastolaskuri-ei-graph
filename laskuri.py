i = 1

while i == 1:
    h = input()
    h = int(h)
  
    if h > 38:
        hinta = 3 + 2**(1/6.5*38) + (h-38)
        print("test")
    elif h >=32:
        hinta = 3 + 2**(1/6.5*int(h))-2**(1/6*(int(h)-30))
    elif h >= 10:
        hinta = 4 + 2**(1/6.5*int(h))
    elif h < 10:
        hinta = 3 + 2**(1/6.5*int(h))
        
    print(hinta)