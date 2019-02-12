"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
from pythonosc import osc_message_builder, udp_client
import time

client = udp_client.SimpleUDPClient("127.0.0.1", 5005)

for i in range(100):
    client.send_message("/sine/freq", 440 + 10 * i)
    time.sleep(0.1)
