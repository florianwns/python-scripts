#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créer une Table d'ondes personnalisée

Pour tester le script, taper dans l'interpreteur pyo :
    osc.type = 1
"""

from pyo import *
import numpy as np

class OscTable(PyoTableObject):
    """
    Waveforms generator.

    Generates basic waveforms.

    :Parent: :py:class:`PyoTableObject`

    :Args:
        type: int, optional
            Waveform type. eight possible values :
                0. Sine (default)
                1. Saw up
                2. Saw down
                3. Square
                4. Triangle

        size : int, optional
            Table size in samples. Defaults to 8192.

    >>> s = Server().boot()
    >>> s.start()
    >>> t = TriTable(type=1).normalize()
    >>> a = Osc(table=t, freq=[199,200], mul=.2).out()
    """
    def __init__(self, type=0, size=8192):
        PyoTableObject.__init__(self, size)
        self._data_table = DataTable(size=size)
        self._arr = np.asarray(self._data_table.getBuffer())
        self.setType(type)
        self._base_objs = self._data_table.getBaseObjects()

    def draw(self):
        "Internal method used to draw the waveform"
        s = self.getSize()
        # Sine
        if self._type == 0:
            self._arr[:] = np.sin(np.linspace(-np.pi, np.pi, s))
        # Sawtooth up
        elif self._type == 1:
            self._arr[:] = np.linspace(-1, 1, s)
        # Sawtooth Down
        elif self._type == 2:
            self._arr[:] = np.linspace(1, -1, s)
        # Square
        elif self._type == 3:
            self._arr[:] = [1 if i >= 0 else -1 for i in np.linspace(-1, 1, s)]
        # Triangle
        elif self._type == 4:
            self._arr[:] = np.roll(2 * np.abs(np.linspace(-1, 1, s)) - 1, s//2)

    def setType(self, type):
        """
        Change the `type` attribute and redraw the waveform.

        :Args:

            type : int
                New type of waveform
        """
        self._type = type
        self.draw()
        self.refreshView()

    @property
    def type(self):
        """int. Type of waveform."""
        return self._type
    @type.setter
    def type(self, type): self.setType(type)

# Run the script to test the OscTable object.
if __name__ == "__main__":
    s = Server().boot().start()

    # create a waveforms generator
    osc = OscTable().normalize()
    osc.view()

    # play the table
    a = Osc(osc, 500, mul=1).out()
    a.ctrl()

    # display
    sp = Spectrum(a)
    sc = Scope(a)

    s.gui(locals())
