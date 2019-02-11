#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test de GUI Automation
pour la rédaction de tests et/ou de tâches automatisées

Sur MAC:
sudo pip3 install pyobjc-framework-Quartz
sudo pip3 install pyobjc-core
sudo pip3 install pyobjc
sudo pip3 install pyautogui

Sources :
- https://pypi.org/project/PyAutoGUI/
- https://automatetheboringstuff.com/chapter18/
"""
import pyautogui
print('Press Ctrl-C to quit.')

# les boîtes de dialogues
pyautogui.alert('This is an alert box.')
pyautogui.confirm('Shall I proceed?')
pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
pyautogui.prompt('What is your name?')
pyautogui.password('Enter password (text will be hidden)')

# Écrire du Texte
pyautogui.typewrite('Hello world!')
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

# Déplacer la souris
pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveTo(200, 100, duration=0.25)
pyautogui.moveTo(200, 200, duration=0.25)
pyautogui.moveTo(100, 200, duration=0.25)
pyautogui.click(500, 500)

# Faire des captures d'écran
im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')
