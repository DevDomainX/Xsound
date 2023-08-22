#!/usr/bin/env python3

from gtts import gTTS
import os
from colorama import init, Fore, Style, Back
init()
from baner import ban
from time import sleep

title =Fore.GREEN+Style.BRIGHT+ """
Date :  Martes 22 de agosto 2023

Created by :  1LugarParaProgramar

Name :      Xsound

Motive :  Script para crear audios para videos etc

Author :  H.saldias

\n\n"""

def sound(texto, name):
    if os.path.exists("1LugarParaProgramar"):
        print("\nla carpeta existe")
    else:
        os.mkdir("1LugarParaProgramar")
        print("\nCarpeta creada")
    tts = gTTS(text=texto, lang = 'es')
    tts.save("1LugarParaProgramar/{}".format(name))
    print(f"{name} Guardado con exito ! \nEn carpeta 1LugarParaProgramar\n\n")
    os.system("ls")
    sleep(1)
    os.system("cd 1LugarParaProgramar")
    sleep(1)
    os.system("ls")
    
print(ban(),title)
texto = input("Ingrese el texto $  ")
name = input("Ingresa nombre archivo $  ")

sound(texto, name +".mp3")

pregunta = input("Desea volver a crear otro audio (s/n) $  ")
if pregunta == "s".lower():
    os.system("cd ..")
    os.system("python3 Xsound.py")
else:
    print(" *_- Gracias 1LigarParaProgramar")
