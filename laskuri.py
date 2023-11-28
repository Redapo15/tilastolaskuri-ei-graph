i = 1

while i == 1:
    h = input()
    h = int(h)
  
    if h >=31:
        hinta = 3 + 2**(1/6.5*int(32)) + (h-32)
    elif h >= 10:
        hinta = 4 + 2**(1/6.5*int(h))
    elif h < 10:
        hinta = 3 + 2**(1/6.5*int(h))
        
    print(hinta)