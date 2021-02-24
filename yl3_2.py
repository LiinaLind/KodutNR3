#jänesevanemate mure
ring = int(input("Sisestage ringide arv: "))
porgand = 0
porgandeid = []

for i in range(0,int(ring/2)): 
    porgand += 2
    porgandeid.append(int(porgand))
print("Saadavate porgandite koguarv on " ,sum(porgandeid))