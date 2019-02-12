"""
A pretty cool electronic piano sound

Source : https://groups.google.com/forum/#!searchin/pyo-discuss/gui|sort:date/pyo-discuss/y5gTsMmleeM/fNRpUNQGBAAJ
"""

from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=128, duplex=1).boot()

########## Piano ##############

####### piano class #########
class Piano:
    '''
    inputs: trig, pitch, dur, mul (pyo objects, polyphonic)
    '''
    def __init__(self, trig, pitch, dur, mul=.3):
        self.trig = trig
        self.pitch = pitch
        self.dur = dur
        self.mul = mul
        self.ta = ExpTable(list=[(0,0),(20,1),(8191,0)], exp=2)
        self.ex = TrigEnv(self.trig, self.ta, dur=self.dur, interp=1)
        self.f = SumOsc(freq=MToF(self.pitch), ratio=1.01, index=.7, mul=self.ex)
        self.ch = Chorus(self.f, depth=.5, feedback=0, bal=.25, mul=self.mul)
        self.rv = Freeverb(self.ch, size=.4, damp=.9, bal=.83, mul=1)
        self.ret = Mix(self.ch+self.rv,2)
    def output(self):
        return self.ret
    def setMul(self, mul):
        self.ch.setMul = mul
    def setDur(self, dur):
        self.ex.setDur = dur
    def setPitch(self, pitch):
        self.f.setFreq = pitch
###### end piano class ######

#### Demo:
tm =.25
mt = Metro([tm,tm*2], poly=10).play()
m = Percent(mt, 50)
pm2 = [33, 36, 38, 40, 43, 45, 48, 50, 52, 55, 57, 60, 62, 64, 67] # A pent min
tc = TrigChoice(m, pm2) # pitch: random notes of a scale
tl = TrigChoice(m, [1,1.5,2.5]) # random choice for note length
pa = Piano(m, tc, tl) # Piano(trig, midi pitch, dur, mul)
p = Pan(pa.output(), outs=2, pan=[.3,.7], spread=0).out()

zz= Scope(p)
#################
s.start()
s.gui(locals())
