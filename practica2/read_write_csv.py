#!/usr/bin/env python3
import csv

### para escribir un archivo
data = [['luis yanez', 19245178],['yelimar marin',19494456]]

with open("test1.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data)

### para escribir un archivo
with open("test1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        name, ci = row
        print(f"Nombre: {name} CI: {ci}")


### para generar un archivo con diccionarios
keys = ['nombre', 'cedula']
data = [{'nombre':'Luis Yanez', 'cedula': 19245178}, {'nombre':'Yelimar Marin', 'cedula': 19195851}]
with open("test2.csv", 'w') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)

### para leer un archivo con diccionarios
with open("test2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['nombre']}  ID: {row['cedula']}")
