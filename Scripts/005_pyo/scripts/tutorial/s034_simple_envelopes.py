#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enveloppes ASR et ADSR

Le Fader est un moyen simple de configurer une enveloppe Attack/Sustain/Release.
Cette enveloppe vous permet d'appliquer un 'fadein' et un 'fadeout' aux
flux audio.

Si l'argument 'dur' du fader est défini sur 0 (valeur par défaut), l'objet
attend une commande stop() avant d'activer la partie libération de l'enveloppe.
Dans le cas où 'dur' n'est pas nul, la somme de fadein et de fadeout doit être
inférieure ou égale à la valeur de 'dur' et l'enveloppe va jusqu'au bout de la
méthode play().

L'objet Adsr (Attack/Decay/Sustain/Release) agit exactement comme l'objet Fader,
avec un type d'enveloppe plus flexible.
"""
from pyo import *
import random

s = Server().boot().start()

# Sustain infini, fadein avec play(), a besoin d'un appel à la méthode stop
# pour lancer le fadeout
fade = Fader(fadein=2, fadeout=2, dur=0).play()

# Enveloppe avec une attaque rapide, un sustain discret et un long relachement
adsr = Adsr(attack=0.01, decay=0.1, sustain=0.5, release=1.5, dur=2, mul=0.5)

# la méthode setExp peut être utile pour créer des enveloppes exponentielles
# ou logarithmiques
adsr.setExp(0.75)

# Met les 2 enveloppes en série, fade et adsr reste autonomes.
# amp est un Dummy Object et n'a donc pas de contrôles.
amp = adsr * fade

# Applique les 2 enveloppes sur un simple synthé en stéréo
sig = SuperSaw(freq=[100,101], detune=0.6, bal=0.8, mul=amp).out()

def play_note():
    "Joue une note avec une fréquence alétoire et une enveloppe scintillante."
    freq = random.choice(midiToHz([36, 38, 41, 43, 45]))
    sig.freq = [freq, freq*1.01]
    adsr.attack = random.uniform(0.002, 0.01)
    adsr.decay = random.uniform(0.1, 0.5)
    adsr.sustain = random.uniform(0.3, 0.6)
    adsr.release = random.uniform(0.8, 1.4)

    # relance l'enveloppe à son début
    adsr.play()

# Appel périodique de la fonction play_note() toutes les 2 secondes
pat = Pattern(play_note, time=2).play()

# Affichage
sc = Scope(sig)
sp = Spectrum(sig)

s.gui(locals())
