#!/usr/bin/env python3
## Practica 1 
with open("test2.txt") as file:
    for line in file:
        print(line.strip().upper())

## Colocar todas la lineas en una lista
file = open("test2.txt")
lines = file.readlines()
lines.sort()
for line in lines:
    print(line.strip())


## modos de apertuda de un archivo
file = open("test3.txt", "a")

with file as file:
    file.write("epales que los que")
    file.write("COÑO DE LA MADRE QUE LO QUE")






