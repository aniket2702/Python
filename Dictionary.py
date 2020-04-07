#Aniket Sharma
#G-704

#Assignment 9

team={"P1":110,"P2":112,"P3":130,"P4":145,"P5":120,"P6":95,"P7":100,"P8":155,"P9":140,"P10":134,"P11":126}
l=0
for p,h in team.items():
    if int(h)>l:
        l=h
        cap=p
print("Captain is",cap,"and his height is",l)