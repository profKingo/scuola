class alunno:
    _nome=""
    _cognome=""
    _voto=0
    _assenze=0
    _voti=[]

    def __init__(self):
        self._nome="XXX"
        self._cognome=""
        self._voto=0
        self._assenze=0
    
    def __init__(self, n, c, v, a):
        self._nome=n
        self._cognome=c
        self._voto=v
        self._assenze=a
    
    def stampa(self):
        print("Nome:" + str(self._nome) + str(self._cognome))
        print("Voto:" + str(self._voto))
        print("Assenze:" + str(self._assenze))
    
    def inserisci(self, v):
        self._voto = v
        self._voti.append(v)
    
    def assente(self, gg):
        self._assenze += gg

c = alunno("Cicco","Cicco", 5, 3) 
c.stampa()
c.inserisci(9)
c.assente(3)
c.inserisci(3)
c.stampa()









'''
class Serbatoio:
    tipo
    qtamax
    qtapres

    carico()
    scarico()
    stamparesiduo()  '''