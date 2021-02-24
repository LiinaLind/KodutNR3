# 3.3 Sissetulekud

#Muutujad
arvud = [] 

# Faili lugemine
fail = open('konto.txt','r')
for rida in fail:
    arvud.append(float(rida))
fail.close()

# Sissetulekud ehk positiivsed arvud
for arv in arvud:
    if arv > 0:
        print(arv)