#!/usr/bin/env python3
"""
Simple inotify events reader

source : https://github.com/paul-nameless/pyfswatch
"""
from fswatch import Monitor

monitor = Monitor()
monitor.add_path('/Users/florian/Downloads/')


def callback(path, evt_time, flags, flags_num, event_num):
    print(path.decode(), evt_time, flags, flags_num, event_num)


monitor.set_callback(callback)
monitor.start()
