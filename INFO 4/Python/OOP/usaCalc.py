from calcolatrice import *

def main():
    sc=" "
    calc = calcolatrice(0, 0, '')
    while sc.upper()!="x".upper():
        print("""#######################"
#  Gestione Oggetti   #
# & crea calcolatrice #
# + somma             #
#######################""")
        sc = input("INSERISCI LA SCELTA: ")
        if sc.upper() == "&":
            p = int(input("inserisci il primo valore: "))
            s = int(input("inserisci il secondo valore: "))
            calc.passavalori(p,s)
        elif sc == "+":
            print("Il risultato vale: " + calc.somma())

main()           

