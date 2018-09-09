
print("Veuillez entrer plusieurs nombres séparés par des virgules : ")
ch = input()
t = list(eval(ch))  # equivaut à list((1, 2, 3, 4, ...)) 
                    # => (1, 2, 3, 4) est un tuple
print("Le nombre le plus grand dans",t,"est :",max(t))