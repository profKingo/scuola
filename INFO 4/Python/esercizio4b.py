lista=["ciccio","pippo","rori","skimmy"]
print(len(lista))
print(len(lista[1]))

l=[]
n=int(input("inserisci n \n"))
print(n)
for i in range(n):
    val=int(input("inserisci valore: "))
    l.append(val)
print(l)
mi=min(l)
ma=max(l)
print(ma-mi)
posmin10=[]
for x in l:
    if x<10 and x>=0:
        posmin10.append(x)
print(posmin10)
posmin10bis=[x for x in l if x<10 and x>=0]
print(posmin10bis)
s=0
c=0
for x in l:
    if x>10:
        l.remove(x)
    else:
        s=s+x
        c=c+1
print(s/c)