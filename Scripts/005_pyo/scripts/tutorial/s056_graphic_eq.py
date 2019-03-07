#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Un équaliseur multibande

Auteur : Aaron Krister Johnson
source : https://groups.google.com/forum/#!searchin/pyo-discuss/SLMap|sort:date/pyo-discuss/XV4E9U9zoKs/C7VbKGByAwAJ
"""

from pyo import *

class GraphicEQ(PyoObject):
    """
    Graphical Equalizer

    """
    def __init__(self, input,
                 boost_16000=0, boost_8000=0, boost_4000=0, boost_2000=0,
                 boost_1000=0, boost_500=0, boost_250=0, boost_125=0,
                 boost_62=0, boost_31=0,
                 mul=1, add=0):
        PyoObject.__init__(self, mul, add)
        self._input = input
        self._in_fader = InputFader(input)
        in_fader, mul, add, lmax = convertArgsToLists(self._in_fader, mul, add)
        self._eq_16000 = EQ(self._input, freq=16000, boost=boost_16000)
        self._eq_8000 = EQ(self._eq_16000, freq=8000, boost=boost_8000)
        self._eq_4000 = EQ(self._eq_8000, freq=4000, boost=boost_4000)
        self._eq_2000 = EQ(self._eq_4000, freq=2000, boost=boost_2000)
        self._eq_1000 = EQ(self._eq_2000, freq=1000, boost=boost_1000)
        self._eq_500 = EQ(self._eq_1000, freq=500, boost=boost_500)
        self._eq_250 = EQ(self._eq_500, freq=250, boost=boost_250)
        self._eq_125 = EQ(self._eq_250, freq=125, boost=boost_125)
        self._eq_62 = EQ(self._eq_125, freq=62, boost=boost_62)
        self._eq_31 = EQ(self._eq_62, freq=31, boost=boost_31)
        self._base_objs = self._eq_31.getBaseObjects()

    def setInput(self, x, fadetime=0.05):
        """
        Replace the `input` attribute.

        :Args:

            x : PyoObject
                New signal to process.
            fadetime : float, optional
                Crossfade time between old and new input. Defaults to 0.05.

        """
        self._input = x
        self._in_fader.setInput(x, fadetime)


    def setBoost_16000(self, x):
        self._eq_16000.setBoost(x)
    @property
    def boost_16000(self):
        return self._eq_16000.boost
    @boost_16000.setter
    def boost_16000(self, x):
        self.setBoost_16000(x)

    def setBoost_8000(self, x):
        self._eq_8000.setBoost(x)
    @property
    def boost_8000(self):
        return self._eq_8000.boost
    @boost_8000.setter
    def boost_8000(self, x):
        self.setBoost_8000(x)

    def setBoost_4000(self, x):
        self._eq_4000.setBoost(x)
    @property
    def boost_4000(self):
        return self._eq_4000.boost
    @boost_4000.setter
    def boost_4000(self, x):
        self.setBoost_4000(x)

    def setBoost_2000(self, x):
        self._eq_2000.setBoost(x)
    @property
    def boost_2000(self):
        return self._eq_2000.boost
    @boost_2000.setter
    def boost_2000(self, x):
        self.setBoost_2000(x)

    def setBoost_1000(self, x):
        self._eq_1000.setBoost(x)
    @property
    def boost_1000(self):
        return self._eq_1000.boost
    @boost_1000.setter
    def boost_1000(self, x):
        self.setBoost_1000(x)

    def setBoost_500(self, x):
        self._eq_500.setBoost(x)
    @property
    def boost_500(self):
        return self._eq_500.boost
    @boost_500.setter
    def boost_500(self, x):
        self.setBoost_500(x)

    def setBoost_250(self, x):
        self._eq_250.setBoost(x)
    @property
    def boost_250(self):
        return self._eq_250.boost
    @boost_250.setter
    def boost_250(self, x):
        self.setBoost_250(x)

    def setBoost_125(self, x):
        self._eq_125.setBoost(x)
    @property
    def boost_125(self):
        return self._eq_125.boost
    @boost_125.setter
    def boost_125(self, x):
        self.setBoost_125(x)

    def setBoost_62(self, x):
        self._eq_62.setBoost(x)
    @property
    def boost_62(self):
        return self._eq_62.boost
    @boost_62.setter
    def boost_62(self, x):
        self.setBoost_62(x)

    def setBoost_31(self, x):
        self._eq_31.setBoost(x)
    @property
    def boost_31(self):
        return self._eq_31.boost
    @boost_31.setter
    def boost_31(self, x):
        self.setBoost_31(x)

    def out(self):
        return PyoObject.out(self)

    def ctrl(self, map_list=None, title='Graphic EQ', wxnoserver=False):
        self._map_list = [SLMap(-20, 20, "lin", "boost_16000", self._eq_16000.boost),
                          SLMap(-20, 20, "lin", "boost_8000", self._eq_8000.boost),
                          SLMap(-20, 20, "lin", "boost_4000", self._eq_4000.boost),
                          SLMap(-20, 20, "lin", "boost_2000", self._eq_2000.boost),
                          SLMap(-20, 20, "lin", "boost_1000", self._eq_1000.boost),
                          SLMap(-20, 20, "lin", "boost_500", self._eq_500.boost),
                          SLMap(-20, 20, "lin", "boost_250", self._eq_250.boost),
                          SLMap(-20, 20, "lin", "boost_125", self._eq_125.boost),
                          SLMap(-20, 20, "lin", "boost_62", self._eq_62.boost),
                          SLMap(-20, 20, "lin", "boost_31", self._eq_31.boost)]
        PyoObject.ctrl(self, map_list, title, wxnoserver)

    @property # getter
    def input(self):
        """PyoObject. Input signal to process."""
        return self._input
    @input.setter # setter
    def input(self, x):
        self.setInput(x)

if __name__ == "__main__":
    s = Server().boot()
    src = PinkNoise(0.3)
    eq_obj = GraphicEQ(src, boost_16000=5)
    mix = Mix(eq_obj, 2)
    fv = Freeverb(mix, size=0.9, damp=0.1, bal=0.9).out()
    spec = Spectrum(fv, size=1024)
    eq_obj.ctrl()
    s.gui(locals())
