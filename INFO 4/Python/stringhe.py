parola=input("inserisci una parola:")
vocali=("a","e","i","o","u")
cont=0
for c in parola:
    if c in (vocali):
        cont+=1
print("le vocali in " + parola + " sono " + str(cont))
cerca=input("inserisci una stringa da cercare:")
pos=parola.find(cerca) #restituisce la posizione di cerca in parola se ci sta else -1
if pos>=0:
    print("la stringa " + cerca + " si trova in pos. " + str(pos))
else:
    print("la stringa non è stata trovata")
cerca=input("inserisci una stringa da contare:")
pos=parola.count(cerca)
if pos>=0:
    print("la stringa " + cerca + " si trova in" + str(pos) + " volte")
else:
    print("la stringa non è stata trovata")
res=parola.strip("pam")   
print(res)
l=[]
l=parola.split("xx")
print(l)
print("__".join(l))