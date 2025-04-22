max=100

def carican():
    num=int(input("Inserisci la lunghezza della matrice:"))
    while num<1 or num>max:
        print("Valore non ammesso")
        num=int(input("Inserisci la lunghezza della matrice:"))
    return num

def caricam():
    num=int(input("Inserisci la larghezza della matrice:"))
    while num<1 or num>max:
        print("Valore non ammesso")
        num=int(input("Inserisci la larghezza della matrice:"))
    return num

def crea_mat(r,c):
    tab = []
    for i in range(r):
        riga=[0]*c #c=5 => [0,0,0,0,0] 
        tab.append(riga)
    print(tab)
    return tab

def carica_mat(tab):    
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tmp=input("Elemento alla riga " + str(i+1) + " colonna " + str(j+1) +": ")
            while(tmp==""):
                print("ERRORE INSERIMENTO!!!")
                tmp=input("Elemento alla riga " + str(i+1) + " colonna " + str(j+1) +": ")
            tab[i][j] = int(tmp)              
        print

def sommarig(tab):   
    for i in range(len(tab)):
        totr=0
        for j in range(len(tab[0])):
            totr = totr + tab[i][j]
            print(f'{tab[i][j]:5d}', end=' ')
        print(f'{totr:8d}')

def main():
    r = carican() 
    c = caricam()
    mat = crea_mat(r,c)
    print("carica gli elementi della matrice")
    carica_mat(mat)
    sommarig(mat)

#esegui programmi
main()
