'''
a=int(input("inserisci A "))
b=int(input("inserisci B "))

if a==0:
    print("indeterminato ")
    print('ciao')
else:
    if b==0:
        print("risultato è 0 ")
    else:
        print("x=-b/a")
        x=-b/a
        print("##############################")
        print("# il valore di x è: " + str(x) + "  #")
        print("##############################")

'''

     
def carican():
    maxv=100

    num=int(input("Inserisci la lunghezza del vettore:"))
    while num<1 or num>maxv:
        print("Valore non ammesso")
        num=int(input("Inserisci la lunghezza del vettore:"))
    print ("Dimensione: " + str(num)) 
    return num

def crea_vet(n):
    tab=[]
    riga = n * [0]  #[0,0,0,0,0,0,0,0,0]
    #tab.insert(0,2);
    #tab.append(3);
    tab=riga
    return tab

def carica_vet(tab):    
    for i in range(len(tab)): #for (int i=0;i<len(tab);i++)
        tmp=input("Elemento alla riga " + str(i+1) + ": ")
        while(tmp==""):
            print("ERRORE INSERIMENTO!!!")
            tmp=input("Elemento alla riga " + str(i+1)+": ")
        tab[i] = int(tmp) 
        print

def somma(tab):   
    totr=0
    for r in range(len(tab)):
        totr = totr + tab[r]
        print(f'{tab[r]:5d}', end=' ')
    print(f'{totr:8d}')

def main():
    n = carican() 
    vet = crea_vet(n)
    print("carica gli elementi del vettore")
    carica_vet(vet)
    print("Stampo la somma!")
    somma(vet)
    print("il vettore ha " + str(vet.count(1)) + " elementi = 1")
    print("il vettore ha " + str(max(vet)) + " come valore massimo")
    print("il vettore ha " + str(min(vet)) + " come valore minimo")
    print("il vettore ha " + str(sum(vet)) + " come somma")
    '''vet.append("ciao")
    print(vet)
    vet.insert(0, "inizio")
    print(vet)
    vet.insert(3, "inmezzo")    
    print(vet)'''

#esegui programmi
main()
