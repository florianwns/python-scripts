#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 011

Play with words

Source : https://www.hackerrank.com/challenges/strplay/problem

Note : une sous séquence palindromique , n'est pas forcement continue
Algorithme pour le moment trop lent.
Valide le test mais cause un timeout sur les chaines trop longues
"""
def lps(s):
    n = len(s)
    # initialise la diagonale des scores à 1
    l = [[0 for _ in range(n)] for _ in range(n)] # score
    for i in range(n):
        l[i][i] = 1

    # longueur pour i
    m = [[] for i in range(n)]

    # on parcours par la diagonale et on augmente le score
    # https://www.youtube.com/watch?v=TLaGwTnd3HY
    for k in range(1, n):
        for i in range(n-k):
            j = i + k
            if s[i] == s[j] and k == 1:
                l[i][j] = 2
                m[i].append((j, 2))
            elif s[i] == s[j]:
                l[i][j] = l[i+1][j-1] + 2
                m[i].append((j, l[i][j]))
            else:
                l[i][j] = max(l[i][j-1], l[i+1][j]);

    # cacule les combinaisons de longueurs max
    n = len(m)
    #print(m)
    score_max = 1
    for i1 in range(n-1):
        for t1 in m[i1]:
            for i2 in range(t1[0]+1, n):
                for t2 in m[i2]:
                    score = t1[1] * t2[1]
                    if score > score_max:
                        score_max = score

    return score_max

print(lps("geekgkeaa"))
# score max = 50 in 0.1s
print(lps("eeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeekseeegeeksforskeeggeeks"))
# score max = 12543 in 14s
