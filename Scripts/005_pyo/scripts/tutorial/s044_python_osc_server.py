"""
OSC example with python-OSC and PYO
"""
from pythonosc import dispatcher, osc_server
from pyo import *

# Démarrage du serveur audio
audio_server = Server().boot().start()

# Une simple sinusoïde de 440Hz
a = Sine(440, mul=0.1).out()

def set_freq(addr, freq):
    "Fonction qui met à jour la fréquence de la sinusoïde"
    a.setFreq(freq)

# Crée un répartiteur d'événement Open Sound Control
dispatcher = dispatcher.Dispatcher()
# Associe le message ''/sine/freq' à la méthode set_freq()
dispatcher.map("/sine/freq", set_freq)

# Active le serveur OSC
osc_server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 5005), dispatcher)
osc_server.serve_forever()

# Petit message d'accueil
print("PYO Listening on {}".format(server.server_address))
