# 3.5 Tahvli juurde

from datetime import *
nimekiri = []
kuu = []
jnr = 1
nr = datetime.now().day

print('')

failinimi = input("Sisestage failinimi: ")
print("")

fail = open(failinimi, encoding='UTF-8')
for rida in fail:
    rida = rida.rstrip()
    nimekiri.append(rida)
    print(jnr,'. ',rida,sep='')
    kuu.append(jnr)
    jnr += 1
fail.close()
print(" ")

for i in range(len(kuu)):
    if nr == kuu[i]:
        print("Täna tuleb vastama:",nimekiri[i])
        