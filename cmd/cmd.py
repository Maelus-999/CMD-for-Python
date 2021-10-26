import config.version
import os

def version():
    print('Voici la version de cmd:' + config.version.version)

def no_shutdown():
    os.system("shutdown /a")

def new_txtFiles():
    name_of_file = input("quel nom voulez vous pour le fichier texte? : ")
    myFile = open(name_of_file+".txt", "w+")
    texte_file = input("que voulez vous marquer dedans? : ")
    myFile.write(texte_file)

    myFile.close()

def new_file():
    fichier_name = input("Nom du Fichier : ")
    os.system("mkdir " + fichier_name)
    print('le fichier a était installer dans vos document')


def pause():
    os.system("pause")

def echo():
    echo = input("que voulez vous ecrire? : ")
    os.system("echo "+echo)

def win():
    os.system("ver")

def cmd():
    os.system("start")
