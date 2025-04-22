# Rubrica file.py: gestione di una rubrica telefonica 
#   con gestione dei files
NOMEF="rubrica.dat"
import os

def menu():
    print()
    print("1: Crea File di testo")
    print("2: Aggiungi voce")    
    print("3: Ricerca voce")    
    print("4: Visualizza file")    
    print("5: Stampa elenco")    
    print("0: Esci")
    print()
    azione=int(input("Inserisci la scelta: "))
    while (azione not in [0,1,2,3,4,5]):
        print ("Valore non ammesso")
        azione=int(input("Inserisci la scelta: "))
    return azione

def crea():
    global NOMEF
    NOMEF=input("Inserisci un nome per il file (senza estensione): ").strip() + ".txt"
    archivio=open(NOMEF, 'w')
    nome=input("Inserisci un valore (* = FINE): ").strip()
    while(nome!='*'):
        archivio.write(nome + "\n")
        nome = input("Inserisci un altro valore (* = FINE): ").strip()
    archivio.close()

def aggiungi():
    if not os.path.exists(NOMEF):
        print("Errore: File non esiste")
    else:
        archivio=open(NOMEF, 'a')
        nome=input("Inserisci un nome (* = FINE): ").strip()
        archivio.write(nome + "\n")
        archivio.close()

def visualizza():
    if not os.path.exists(NOMEF):
        print("Errore: File non esiste")
    else:
        archivio=open(NOMEF, 'r')
        riga=archivio.readline()
        print("Valore")
        while(riga!=""):
            nome = riga
            print(nome, end = '')
            riga=archivio.readline()
        archivio.close()

def cerca():
    cercato = input("Inserisci un nome da cercare: ").strip()
    if not os.path.exists(NOMEF):
        print("Errore: File non esiste")
    else:
        archivio=open(NOMEF, 'r')
        trovato=False
        riga=archivio.readline().strip()
        while riga!="":
            nome = riga[0:riga.find(";")]
            if nome==cercato:
                print ("Valore trovato: ", nome)
                trovato=True
                break
            riga=archivio.readline().strip()
        if not trovato:
            print ("Il nome cercato non è in elenco!!!")
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

