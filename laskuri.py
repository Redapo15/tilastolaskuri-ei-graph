i = 1

while i == 1:
    h = input()
    h = int(h)
  
    if h > 48:
        hinta = 3 + 2**(1/6.5*int(32))+2**(1/6*(int(48)-25)) + (h-48)
    elif h >=32:
        hinta = 3 + 2**(1/6.5*int(32))+2**(1/6*(int(h)-25))
    elif h >= 10:
        hinta = 4 + 2**(1/6.5*int(h))
    elif h < 10:
        hinta = 3 + 2**(1/6.5*int(h))
        
    print(hinta)