settimana=('Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom')

def leggi_incassi():
    incassi=[]
    for giorno in settimana:
        valore=float(input("Incasso di " + giorno + ": "))
        incassi.append(valore)
    return incassi

def calcola_totale(dati):
    totale=0
    for i in range(len(dati)):
        totale=totale+dati[i]
    print(len(dati))
    print(30 * '-')
    print("Incasso totale:",totale)

def main():
    incassi=leggi_incassi()
    calcola_totale(incassi)

#esegui il main
main()