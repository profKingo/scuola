import os

def stampalista(l):
    nome=l[0]+(20-len(l[0]))*" "
    cognome=l[1]+(20-len(l[1]))*" "
    eta=l[2].strip()+(4-len(l[2].strip()))*" "
    eta=eta[0:3]
    print("|"+nome+"|"+cognome+"|"+eta+"|")

def crealista():
    lista=[]
    if not os.path.exists(NOMEF):
        print("Errore: File non esiste")
    else:
        archivio=open(NOMEF, 'r')
        riga=archivio.readline()
        while(riga!=""):
            nome, cognome, eta = riga.split(",")  
            l=[nome,cognome,eta]
            lista.append(l)
            riga=archivio.readline()
    return lista

def visualizza():
    if not os.path.exists(NOMEF):
        print("Errore: File non esiste")
    else:
        archivio=open(NOMEF, 'r')
        lista=[]
        riga=archivio.readline()
        print("-----------------------------------------------")
        print("|Nome                |Cognome             |Età|")
        while(riga!=""):
            nome, cognome, eta = riga.split(",")  
            l=[nome,cognome,eta]
            lista.append(l)
            stampalista(l)
            riga=archivio.readline()
        print("-----------------------------------------------")

def copiagiovani(l):
    archivio=open("copia.txt", 'w')
    for x in l:
        if int(x[2])<25:
            n=x[0]
            c=x[1]
            e=x[2]
            archivio.write(n+","+c+","+e)
    archivio.close()
    
def aggiungi():
    if not os.path.exists(NOMEF):
        print("Errore: File non esiste")
    else:
        archivio=open(NOMEF, 'a')
        nome=input("Inserisci un nome (* = FINE): ").strip()
        while(nome!='*'):
            cognome=input("Inserisci un cognome: ").strip()
            eta=input("Inserisci un'età: ").strip().replace("\n","")
            archivio.write(nome + "," + cognome + "," + eta + "\n")
            nome=input("Inserisci un nome (* = FINE): ").strip()
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
            nome, cognome, eta = riga.split(",")
            if nome==cercato:
                print ("Eta: ", eta)
                trovato=True
                break
            riga=archivio.readline().strip()
        if not trovato:
            print ("Il nome cercato non è in rubrica!!!")
        archivio.close()

NOMEF="lista.txt"
lista=crealista()
visualizza()
copiagiovani(lista)
aggiungi()
visualizza()
cerca()
