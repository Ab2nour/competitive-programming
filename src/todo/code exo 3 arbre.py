class Noeud:
    def __init__(self, nom, pere=None, deja_visite=False):
        self.nom = nom
        self.pere = pere
        self.deja_visite = deja_visite

    def __repr__(self):
        #return "Noeud " + self.nom
        return str(self.nom)

    def to_the_top(self, autre_noeud):
        liste_noeuds_visites = []
        noeud_actuel = self

        while noeud_actuel != None:
            noeud_actuel.deja_visite = True
            liste_noeuds_visites.append(noeud_actuel)
            noeud_actuel = noeud_actuel.pere

        while autre_noeud.deja_visite == False:
            if autre_noeud.pere == None:
                autre_noeud = None
                break
            else:
                autre_noeud = autre_noeud.pere

        for noeud in liste_noeuds_visites:
            noeud.deja_visite = False

        return autre_noeud

N = int(input())
liste_pour_noeuds = list(map(int, "3 3 7 3 6 7 0 0".split()))
liste_pour_noeuds = list(map(int, input().split()))
#liste_pour_noeuds = [8, 8, 10, 1, 8, 2, 4, 10, 0, 9]

R = int(input())

## Création de l'arbre à partir des données
noeuds = [Noeud(i+1) for i in range(N)]

for i in range(N):
    indice = liste_pour_noeuds[i]-1

    if indice >= 0:
        noeuds[i].pere = noeuds[indice]
# --- Fin

for i in range(R):
    noeud1, noeud2 = map(int, input().split())
    noeud1, noeud2 = noeuds[noeud1-1], noeuds[noeud2-1]

    a = noeud1.to_the_top(noeud2)

    if a == None:
        print(0)
    else:
        print(a)