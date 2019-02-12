"""Small example OSC server

This program listen one adresse on one port
and prints some information about received packets.
"""
from pythonosc import dispatcher, osc_server

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/sine", print)

server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 5005), dispatcher)
print("Listening on {}".format(server.server_address))
server.serve_forever()
