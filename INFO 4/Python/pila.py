# pila.py: gestione di una pila

pila=[]
def menu():
    print()
    print("1: Aggiungi elemento")    
    print("2: Estrai elemento")    
    print("3: Svuota pila")    
    print("4: Esci")
    print()
    azione=int(input("Inserisci la scelta: "))
    while (azione not in [1,2,3,4]):
        print ("Valore non ammesso")
        azione=int(input("Inserisci la scelta: "))
    return azione

def aggiungi():
    dato=input("Dato da inserire: ")
    pila.append(dato)

def estrai():
    if(len(pila)==0):
        print("Pila vuota!!")
    else:
        dato=pila.pop()
        print("Estratto elemento con valore ", dato

def svuota():
    while (len(pila)!=0):
        dato=pila.pop()
        print("Estratto elemento con valore ", dato)
    print("Pila vuota!")

def main():
    while True:
        scelta=menu()
        if scelta==1: aggiungi()
        elif scelta==2: estrai()
        elif scelta==3: svuota()
        else: 
            print ("Fine programma.")
            break
#lancio del programma
main()

