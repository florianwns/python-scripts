#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Widget animation
================

Cet exemple montre comment créer et appliquer une animation complexe à un
composant de type boutonself. Vous devriez voir un bouton 'plop'
qui se déplacera quand on clique dessus.

Source : https://kivy.org/doc/stable/examples/gen__animation__animate__py.html
"""
import kivy
kivy.require('1.0.7')
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def animate(self, instance):
        """
        Fonction qui crée un objet Animationself. Cet objet peut être stocké,
        et réutilisé à chauqe appel ou réutilisé à travers différents objetsself.
        += est une étape séquentielle, alors &= se passe en parallèle
        """
        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(200, 100), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))

        # applique l'animation sur le bouton, en passant l'instance en argument
        # Notez que l'animation par défaut du click gauche
        # (changement de couleur) reste inchangé.
        animation.start(instance)

    def build(self):
        """
        Créer un bouton, et lui attribue la méthode 'animate'
        comme gestionnaire de l'événement 'on_press'
        """
        button = Button(size_hint=(None, None),
                        text='plop',
                        on_press=self.animate)
        return button

if __name__ == '__main__':
    TestApp().run()
