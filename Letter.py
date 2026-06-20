import string
import random
import time
from mainandersrum.py import ausgabe

status = False

zufall = ''.join(random.choices(string.ascii_uppercase, k=1))

print(zufall)

start = time.time()

if ausgabe == zufall:
    status = True

if status == True:
    print("Richtig!")
else:
    print("Leider Falsch :(")
end = time.time()
print("In " + str(round(end - start, 0)) + " Sekunden")
