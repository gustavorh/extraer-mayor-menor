# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:37:47 2021

Nombre: Gustavo Reyes Herrera
RUT: 21023531-0

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

# Este script determinará el menor valor dentro de una lista con una función y mostrará el resultado en pantalla.

def menor_valor(lista):
    menor = lista[0]
    for i in range(1, len(lista)): # lista[1:len(lista+1)]
        if lista[i] < menor:
            menor = lista[i]
            indice = i
    return menor, indice

lista = [5, 8, 3, 1, 9, 0, 3, 6, 1, 8]
menor, indice_en_lista = menor_valor(lista)

print(f"El menor valor de la lista es: {menor} y su índice en la lista es {indice_en_lista}")