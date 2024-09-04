class File:
    def __init__(self, tete=None, queue=None):
        self.tete = tete
        self.queue = queue

    def vide(self):
        if self.tete == None and self.queue == None:
            return True
        else:
            return False

    def popleft(self):
        if self.vide():
            raise Exception("File vide")

        valeur = self.tete.valeur

        if self.tete.suivant != None:
            # del self.tete
            self.tete = self.tete.suivant
            self.tete.precedent = None
        else:
            self.tete = None
            self.queue = None

        return valeur


    def append(self, element):
        if self.vide():
            self.tete = element
            self.queue = element
        else:
            self.queue.suivant = element
            element.precedent = self.queue
            self.queue = element

class Maillon:
    def __init__(self, valeur, suivant=None, precedent=None):
        self.valeur = valeur
        self.suivant = suivant
        self.suivant = precedent


nb_distributeurs = int(input())
nb_operations = int(input())

files = [File() for i in range(nb_distributeurs+1)]

for i in range(nb_operations):
    num_distribteur, qtite, date = map(int, input().split())

    if qtite < 0:
        for j in range(-qtite):
            files[num_distribteur].popleft()
    else:
        for j in range(qtite):
            files[num_distribteur].append(Maillon(date))

for i in range(1, len(files)):
    minimum = 100000000
    #for j in range(len(files[i])):
    while not files[i].vide():
        a = files[i].popleft()
        if a < minimum and a > 0:
            minimum = a

    if minimum == 100000000:
        print(0)
    else:
        print(minimum)
