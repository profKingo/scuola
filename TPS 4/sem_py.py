from semaphore import semaphore
#La funzione safeprint serve per poter ricevere stampe leggibili perché la print stessa non è atomica. (usano una print al posto della safeprint si possono osservare le stampe dei diversi thread mischiate fra loro).

mutex = semaphore(1)
def safeprint(*args,**kwargs):
  mutex.P()
  print(*args,**kwargs)
  mutex.V()
#Le variabili condivise (globali) sono:

buf = []
full = semaphore(0)
empty = semaphore(1)
#La struttura del produttore e del consumatore è la seguente:

def producer():
  while True:
#   produce val
    empty.P()
    val = eval(input("inserisci un elemento: "))
    buf.append(val)
    full.V()

def consumer():
  while True:
    full.P()
    val = buf.pop(0)
    empty.V()
#   consume val