#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SuperSpace

Inspired by "How to Emulate the Super Saw"
Source : https://www.nada.kth.se/utbildning/grukth/exjobb/rapportlistor/2010/rapporter10/szabo_adam_10131.pdf
"""

from pyo import *

class SuperSpace(PyoObject):
    """
    Super Space Oscillator.

    :Parent: :py:class:`PyoObject`

    :Args:

        input : PyoObject
            Input signal to process.
        freq : float or PyoObject, optional
            Frequency, in cycles per second, of the modulator.
            Defaults to 100.

    >>> s = Server().boot()
    >>> s.start()
    >>> ss = SuperSpace(freq=[800,1000], mul=lfo).out()
    """
    def __init__(self, freq=100, mul=1, add=0):
        PyoObject.__init__(self, mul, add)
        self._freq, mul, add, lmax = convertArgsToLists(freq, mul, add)
        self._ratio = [0.88997686, 0.93711560, 0.98047643, 1.0, 1.01991221, 1.06216538 , 1.10745242]
        self._lfo_freq = [self._freq[i] * f for f in self._ratio for i in range(len(self._freq))]
        self._lfo = LFO(freq=self._lfo_freq, mul=mul, add=add, type=3)
        self._mix = self._lfo.mix(lmax)
        self._base_objs = self._mix.getBaseObjects()

if __name__ == "__main__":
    s = Server().boot().start()

    a = Sine(freq=0.2).range(400, 1000)
    b = SuperSpace(freq=a).out()

    sp = Spectrum(b)
    sc = Scope(b)

    s.gui(locals())
