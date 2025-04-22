from threading import Thread, Lock

mutex=Lock()

class mutua:
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome=nome
    def run(self):
        mutex.acquire()
        print("Inizio Thread", self.nome)
        #svolgo l'attività
        print("Fine Thread", self.nome)
        mutex.release()

class Buffer:
    def __init__(self):
        self.valore=0
        self.p_lock=Lock()
        self.c_lock=Lock()
        self.c_lock.acquire()
    def getdato(self, nome):
        self.c_lock.acquire()
        dato=self.valore
        self.p_lock.release()
        return dato
    def setdato(self, nome, x):
        self.p_lock.acquire()
        self.valore=x
        self.c_lock.release()

buf=Buffer()
buf.setdato("dato1", 5)
print(buf.getdato("dato1"))
buf.setdato("dato2", 4)
print(buf.getdato("dato2"))
