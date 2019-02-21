#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Création d'un module PyoObject nommé 'RingMod'.

source : http://ajaxsoundstudio.com/pyodoc/tutorials/pyoobject1.html
"""
from pyo import *

class RingMod(PyoObject):
    """
    Modulateur en anneaux.

    La modulation en anneaux est un effet de traitement du signal en électronique
    effectuée en multipliant deux signaux, où l’un est typiquement une onde
    sinusoïdale ou une autre forme d'onde simple.

    :Parent: :py:class:`PyoObject`

    :Args:
        input : PyoObject
            Le signal d'entrée à traiter.
        freq : float ou PyoObject, optionnel
            Frequence, en cycles par secondes, du modulateur
            Par défaut à 100.

    >>> s = Server().boot()
    >>> s.start()
    >>> src = SfPlayer(SNDS_PATH+"/transparent.aif", loop=True, mul=.3)
    >>> lfo = Sine(.25, phase=[0,.5], mul=.5, add=.5)
    >>> ring = RingMod(src, freq=[800,1000], mul=lfo).out()

    """
    def __init__(self, input, freq=100, mul=1, add=0):
        # appel du constructeur parent
        PyoObject.__init__(self, mul, add)

        # Garder les références de tous les arguments
        self._input = input
        self._freq = freq

        # InputFader permet un fondu enchaîné lors du changement de source
        self._in_fader = InputFader(input)

        # Converti tous les arguments en listes pour le "multi-canal"
        in_fader,freq,mul,add,lmax = convertArgsToLists(self._in_fader,freq,mul,add)

        # Applique le traitement
        self._mod = Sine(freq=freq, mul=in_fader)

        # Utilisez Sig pour empêcher de modifier l'attribut "mul" de self._mod
        self._ring = Sig(self._mod, mul=mul, add=add)

        # self._base_objs est la sortie audio vue par le monde extérieur!
        # getBaseObjects() renvoie la liste des flux gérés par l'instance
        self._base_objs = self._ring.getBaseObjects()

    def setInput(self, x, fadetime=0.05):
        self._input = x
        self._in_fader.setInput(x, fadetime)

    def setFreq(self, x):
        self._freq = x
        self._mod.freq = x

    def play(self, dur=0, delay=0):
        self._mod.play(dur, delay)
        return PyoObject.play(self, dur, delay)

    def stop(self):
        self._mod.stop()
        return PyoObject.stop(self)

    def out(self, chnl=0, inc=1, dur=0, delay=0):
        self._mod.play(dur, delay)
        return PyoObject.out(self, chnl, inc, dur, delay)

    def ctrl(self, map_list=None, title=None, wxnoserver=False):
        self._map_list = [SLMap(10, 2000, "log", "freq", self._freq),
                          SLMapMul(self._mul)]
        PyoObject.ctrl(self, map_list, title, wxnoserver)

    # getter et setter
    @property
    def input(self):
        """PyoObject. Singal d'entrée à traiter."""
        return self._input
    @input.setter
    def input(self, x):
        self.setInput(x)

    @property
    def freq(self):
        """float or PyoObject. Fréquence du modulateur."""
        return self._freq
    @freq.setter
    def freq(self, x):
        self.setFreq(x)

# Execute le script pour tester l'objet RingMod.
if __name__ == "__main__":
    s = Server().boot().start()
    src = SfPlayer(SNDS_PATH+"/transparent.aif", loop=True, mul=.3)

    # Déphasage du canal gauche et droit
    lfo = Sine(.25, phase=[0,.5], mul=.5, add=.5)
    ring = RingMod(src, freq=[800,1000], mul=lfo).out()
    ring.ctrl()
    s.gui(locals())
