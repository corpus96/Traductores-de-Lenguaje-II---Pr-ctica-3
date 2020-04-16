#Practica 3
#Realizado por Emmanuel Corpus
#Asignatura: Traductores de Lenguaje II

#Espeificaciones
# => tomar el lenguaje hecho en la práctica 2 y hacer un Analizador sintáctico descendente recursivo que reconozca ese lenguaje.

#Documentación
# => Gramática realizada en la práctica 2

#Notas:
# => No utilizar parametros innecesarios.

#[Variables Globales]

import os
import time
from colorama import Fore

#Variable global
_GLOBFLAG = True
_VUELTAS = 0
_C = 0
_CADENA = ""
_CONTADOR = 0

def menu():
    global vueltas

    exitFlag = False

    while not exitFlag:
        os.system("cls")
        finalString = ""
        _VUELTAS = 0
        _C = 0

        print("\t ----------------------------------------------")
        print("\t|   ANALIZADOR SINTACTICO DECENDENTE RECURSIVO |")
        print("\t ----------------------------------------------")
        print("\n\t\t   (1) Ingresar cadena")
        print("\t\t   (0) Salir del programa")
        menuOption = input("\t\t   Ingrese opcion: ")

        if menuOption == "1":
            ASDR()
        elif menuOption == "0":
            print("Saliendo del programa...")
            exitFlag = True
        else:
            print("Esta opcion no esta disponible en el menu")

        input("\nPresione cualquier tecla para continuar")
                        
def ASDR():
    global _CADENA

    _CADENA = input("Ingresar la cadena: ")

    if _CADENA == "" or _CADENA == " ":
        print("\n\033[32m" + "Cadena aceptada")
        print("\033[39m")
    else:
        expr()

def expr():
    global _GLOBFLAG
    global _CONTADOR
    global _CADENA

    _CONTADOR = len(_CADENA)
    _C = 0
    _GLOBFLAG = True

    #Recorrer cada caracter de la cadena
    while(_C < _CONTADOR):
        _C = term()
        _C = resto()

        if _C != None:
            if _C >= _CONTADOR or _C == None:
                break
        else:
            break

    if _GLOBFLAG:
        print("\n\033[32m" + "Cadena aceptada")    
        print("\033[39m")

def term():
    global _GLOBFLAG
    global _C
    global _CADENA

    if _CADENA[_C].isdigit():
        t = _CADENA[_C]
        _C = coincidir()

        print(t, end='')
    else:
        print("\033[31m" + "\nERROR DE SINTAXIS")
        print("\033[39m")

        _GLOBFLAG = False

        exit()

    return _C  

def coincidir(oper):
    global _GLOBFLAG
    global _CADENA
    global _C

    line = "0123456789+-"
    f = False

    for l in line:
        if oper == l:
            res = _C + len(_CADENA[_C])
            f = True

    if not f:
        print("\033[31m" + "\nSimbolo no reconocido(1)")
        print("\033[39m")  

        _GLOBFLAG = False

        exit()

    return res      

def resto():
    global _GLOBFLAG
    global _C
    global _CONTADOR
    global _CADENA

    if _C < _CONTADOR:
        if _CADENA[_C] == '+':
            _C = coincidir('+')
            _C = term()

            print('+', end='')
            
            _C = resto()

            return _C
        elif _CADENA[_C] == '-':
            _C = coincidir('-')
            _C = term()

            print('-', end='')

            _C = resto()

            return _C
        else:
            _GLOBFLAG = False
            print("\033[31m" + "\nSimbolo no reconocido")
            print("\033[39m")

            exit()

menu()            