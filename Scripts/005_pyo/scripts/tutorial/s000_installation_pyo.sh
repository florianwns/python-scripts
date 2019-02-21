# Installation de pyo

# Ressources :
# http://ajaxsoundstudio.com/pyodoc/compiling.html

brew install liblo libsndfile portaudio portmidi --universal
git clone https://github.com/belangeo/pyo.git
cd pyo
python setup.py install --use-coreaudio --use-double
