# Rubrica file.py: gestione di una rubrica telefonica 
#   con gestione dei files
NOMEF="rubrica.dat"
import os

def menu():
    print()
    print("1: Crea Rubrica")
    print("2: Aggiungi nome")    
    print("3: Ricerca nome")    
    print("4: Visualizza coda")    
    print("5: Stampa rubrica")    
    print("0: Esci")
    print()
    azione=int(input("Inserisci la scelta: "))
    while (azione not in [0,1,2,3,4,5]):
        print ("Valore non ammesso")
        azione=int(input("Inserisci la scelta: "))
    return azione

def crea():
    archivio=open(NOMEF, 'w')
    nome=input("Inserisci un nome (* = FINE): ").strip()
    while(nome!='*'):
        telefono=input("Inserisci un telefono: ").strip()
        archivio.write(nome + "; " + telefono + "\n")
        nome = input("Inserisci un altro nome (* = FINE): ").strip()

def aggiungi():
    if not os.path.exists(NOMEF):
        print("Errore: File non esiste")
    else:
        archivio=open(NOMEF, 'a')
        nome=input("Inserisci un nome (* = FINE): ").strip()
        telefono=input("Inserisci un telefono: ").strip()
        archivio.write(nome + ";" + telefono + "\n")
        archivio.close()

def visualizza():
    if not os.path.exists(NOMEF):
        print("Errore: File non esiste")
    else:
        archivio=open(NOMEF, 'r')
        riga=archivio.readline()
        print("Nome  -  Telefono  ")
        while(riga!=""):
            nome, telefono = riga.split("; ")  
            print(nome + " - " + telefono, end = '')
            riga=archivio.readline()

def cerca():
    cercato = input("Inserisci un nome da cercare: ").strip()
    if not os.path.exists(NOMEF):
        print("Errore: File non esiste")
    else:
        archivio=open(NOMEF, 'r')
        trovato=False
        riga=archivio.readline().strip()
        while riga!="":
            nome, telefono = riga.split(";")
            if nome==cercato:
                print ("Telefono: ", telefono)
                trovato=True
                break
            riga=archivio.readline().strip()
        if not trovato:
            print ("Il nome cercato non è in rubrica!!!")
        archivio.close()

def stampa():
    comando = "notepad /p " + NOMEF
    os.system(comando)

def main():
    while True:
        scelta=menu()
        if scelta==1: crea()
        elif scelta==2: aggiungi()
        elif scelta==3: cerca()
        elif scelta==4: visualizza()
        elif scelta==5: stampa()
        else: 
            print ("Fine programma.")
            break

#lancio del programma
main()