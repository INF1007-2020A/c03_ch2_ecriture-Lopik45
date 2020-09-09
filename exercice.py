#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
            nombre = 0
            nombre = ord(lettre) - 32
            lettre = chr(nombre)
            resultat += lettre
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
