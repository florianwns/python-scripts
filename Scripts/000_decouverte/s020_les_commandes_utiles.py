#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Les commandes utiles pour Python sur MacOS

Source : https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
"""
# Localiser sa version de python3 avec which
which -a python3

# changer les liens symboliques de Python vers Python3
ln -s /usr/local/bin/python3 /usr/local/bin/python
ln -s /usr/local/bin/pip3 /usr/local/bin/python

# Au lieu de changer les liens, mettre à jour le fichier ~/.bash_profile
# en principe, c'est mis à jour par à l'install de python
export PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"

# mettre à jour sa version de brew puis de python (ne supprime pas les deps)
brew update
brew uninstall --ignore-dependencies python3
brew install python3

# ou mettre à jour depuis le site "https://www.python.org/downloads/"

####################

# Liste les paquets installés pour le fichier "requirements.txt"
pip freeze > requirements.txt

####################
# créer un environnement virtuel
# Installer virtualenv, attention à la version de python
pip install virtualenv

# créer son répertoire de projet, le monter,
# et installer la version de python choisie en local
mkdir my_project_folder
cd my_project_folder
virtualenv -p /usr/local/bin/python venv

# commencer à utiliser l'environnement virtuel
source venv/bin/activate

# Installer les paquets nécessaires au projet via "requirements.txt"
pip install -r requirements.txt

# arrêter l'utilisation de l'environment virtuel
deactivate
