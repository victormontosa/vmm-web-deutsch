import csv
import os
import random


def cargar_frases_desde_csv(nombre_archivo):
    """
    Carga las frases desde un archivo CSV y las devuelve como listas separadas para frases en inglés y alemán.
    """
    frases_en, frases_de = [], []
    with open(nombre_archivo, newline='', encoding='utf-16') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter='\t')
        for fila in lector:
            frases_en.append(fila[0])
            frases_de.append(fila[1])
    return frases_en, frases_de

