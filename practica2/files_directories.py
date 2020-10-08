#!/usr/bin/env python3

import os

"""os.remove("testa.txt")
os.rename("testa.txt","testa2.txt")
os.path.exists("users_lists.txt")

os.path.isfile("test.txt")
 
## Listar todos los elementos dentro de un directorio
os.mkdir("directorio_practica")
os.path.chdir("directorio_practica")"""
dir = "hola"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{fullname} es una carpeta tamaño {'{:.4f}'.format(os.path.getsize(fullname)/1000)} KB")
    else:
        print(f"{fullname} es un archivo {'{:.4f}'.format(os.path.getsize(fullname)/1000)} KB")


import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  file = open(filename,"w")
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  timestamp = "{:%Y-%m-%d}".format(datetime.datetime.fromtimestamp(timestamp))
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return (timestamp)

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd


import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))