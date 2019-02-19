"""
Enregistrement de son en direct dans la RAM.
En enregistrant un flux de son dans la RAM, il est possible de réutiliser
rapidement les échantillons dans le processus en cours.
Une combinaison des objets NewTable et TableRec est tout ce dont vous avez
besoin pour  enregistrer n’importe quel flux dans une table.

L'objet NewTable a un argument de feedback permettant l'overdub.
L'objet TableRec commence un nouvel enregistrement (enregistre jusqu'à ce que
la table soit pleine) chaque fois que sa méthode play() est appelée.
"""
from pyo import *

s = Server().boot().start()

# Crée une table vide stéréo de deux secondes. L'argument "feedback" est la
# quantité d'anciennes données à mélanger avec un nouvel enregistrement (overdub).
# overdub : mixe l'ancien flux avec le nouveau en fonction du feedback
t = NewTable(length=2, chnls=2, feedback=0.5)

# Récupère l'entrée stéréo
inp = Input([0,1])

# Enregistreur de table. Lancer rec.play() dans le terminal pour démarrer un
# enregistrement, il s’arrête quand la table est pleine.
# Appelez-le plusieurs fois pour créer une superposition.
rec = TableRec(inp, table=t, fadetime=0.05)

# Lit le contenu de la table en boucle
osc = Osc(table=t, freq=t.getRate(), mul=0.5).out()

s.gui(locals())
