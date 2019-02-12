"""
OSC example with python-OSC and PYO
"""
from pythonosc import dispatcher, osc_server
from pyo import *

s = Server().boot()
s.start()
a = Sine(440, mul = 0.1).out()

def updateFreq(addr, freq):
    print(addr, freq)
    a.setFreq(freq)

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/sine/freq", updateFreq)

server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 5005), dispatcher)
print("PYO Listening on {}".format(server.server_address))
server.serve_forever()
