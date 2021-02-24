#3.4 Jukebox

palad = []
laulu_nr = []
jnr = 1

failinimi = input("Palun sisestage faili nimi: ")
print("")

print("Muusikapalade valik:")

fail = open(failinimi, encoding='UTF-8')

for rida in fail:
    rida = rida.rstrip()
    palad.append(rida)
    print(jnr,'. ',rida,sep='')
    laulu_nr.append(jnr) 
    jnr += 1
fail.close()

print("")
loo_nr = int(input("Palun sisestage laulu järjekorranumber: "))
for i in range(len(laulu_nr)):
    if loo_nr == laulu_nr[i]:
        print("Mängitav muusikapala on:",palad[i],)