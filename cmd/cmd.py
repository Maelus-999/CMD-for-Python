import config.version
from config import *
import os, sys


def cmd_version():
    print("the version of cmd is: "+ config.version.version)

def cmd_no_shutdown():
    os.system("shutdown /a")

def cmd_new_txtFiles():
    name_of_file = input("quel nom voulez vous pour le fichier? : ")
    myFile = open(name_of_file+".txt", "w+")
    texte_file = input("que voulez vous marquer dedans? : ")
    myFile.write(texte_file)

    myFile.close()

def cmd_new_file():
    fichier_name = input("Nom du Fichier : ")
    os.system("mkdir " + fichier_name)
    print("le fichier a était installer dans vos document")
