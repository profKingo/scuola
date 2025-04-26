import threading
from threading import Thread
import time
import random

# Definiamo la classe Filosofo
class Filosofo(Thread):
    def __init__(self, name, fork_on_left, fork_on_right):
        Thread.__init__(self)
        self.nome = name
        self.fork_on_left = fork_on_left
        self.fork_on_right = fork_on_right
        self.left_fork = None
        self.right_fork = None

    # Metodo run per il thread del filosofo
    def run(self):
        while True:
            time.sleep(random.randint(1,5))
            print(f"{self.nome} è affamato")
            self.pick_up_forks()
            time.sleep(random.randint(1,3))
            self.put_down_forks()

    # Metodo per prendere le forchette
    def pick_up_forks(self):
        self.left_fork = self.fork_on_left
        self.right_fork = self.fork_on_right

        if self.left_fork and self.right_fork:
            print(f"{self.nome} ha preso entrambe le forchette")
        else:
            print(f"{self.nome} non può prendere le forchette")

    # Metodo per posare le forchette
    def put_down_forks(self):
        if self.left_fork and self.right_fork:
            print(f"{self.nome} ha posato entrambe le forchette")
            self.left_fork = None
            self.right_fork = None

# Creiamo i filosofi e le forchette
philosophers = ["Platone", "Aristotele", "Socrate", "Pitagora"]
forks = [threading.Lock() for _ in range(4)]

# Creiamo i thread per i filosofi
threads = []
for i, name in enumerate(philosophers):
    if i == len(philosophers) - 1:
        left_fork = forks[0]
        right_fork = forks[i]
    else:
        left_fork = forks[i + 1]
        right_fork = forks[i]
    threads.append(Filosofo(name, left_fork, right_fork))

# Avviamo i thread
for t in threads:
    t.start()

# Uniamo i thread
for t in threads:
    t.join()