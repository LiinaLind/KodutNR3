# 3.1 Ülikooli vastuvõetud
print("Ülikooli vastuvõetud")
aastad = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
i = 0
vastuvoetud = []
fail = open('rebased.txt', encoding='UTF-8')
for rida in fail:    
    vastuvoetud.append(int(rida))
fail.close()
print("Ajavahemik 2011 - 2019")
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))    
for i in range(len(aastad)): 
    if aasta == aastad[i]: 
        print(aasta,". aastal oli vastuvõetuid ",vastuvoetud[i],sep='')