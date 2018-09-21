"""Les arguments d'applications

Petit programme qui lit les arguments passés en paramètre
"""

import sys

for i in range(len(sys.argv)):
    print("arg[{}] : {}".format(i,sys.argv[i]))
