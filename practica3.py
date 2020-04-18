#Practica 3
#Realizado por Emmanuel Corpus
#Asignatura: Traductores de Lenguaje II

#Especificaciones
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
_FILEPATH = "source.txt"

#Palabaras reservadas
reserved = [
 
    "begin",
    "end",
    "entero",
    "real",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T,"
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "if",
    "else",
    "while",
    "endwhile"
]

#Reglas de expresiones regulares (Lógicas)
MENORQUE = r'<'
MAYORQUE = r'>'
IGUAL = r'='
MENORIGUALQUE = r'<='
MAYORIGUALQUE = r'=>'
DIFERENTEQUE = r'<>'
PARIZQ = r'('
PARDER = r')'
COMA = r','
PUNTOYCOMA = r';'
PUNTO = r'.'
SUM = r'+'
SUB = r'-'
MUL = r'*'
DIV = r'/'

def menu():
    exitFlag = False

    while not exitFlag:
        os.system("cls")
        finalString = ""
        #_VUELTAS = 0
        #_C = 0

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

'''
**********************************************************************************
**********************************************************************************
'''        
                        
def ASDR():
    global _CADENA

    _CADENA = readFile()

    if _CADENA == "":
        print("\n\033[32m" + "Cadena aceptada")
        print("\033[39m")
    else:
        expr()

'''
**********************************************************************************
**********************************************************************************
'''        

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

        '''
        if _C != None:
            if _C >= _CONTADOR or _C == None:
                break
        else:
            break
        '''

    if _GLOBFLAG:
        print("\n\033[32m" + "Cadena aceptada")    
        print("\033[39m")

'''
**********************************************************************************
**********************************************************************************
'''        

def term():
    global _GLOBFLAG
    global _C
    global _CADENA
    global _FILEPATH

    with open(_FILEPATH) as fp:

        line = fp.readline()

        while line:
            #if _CADENA[_C].isdigit():
            if is_in_reserved(line):
                #t = _CADENA[_C]
                t = line
                #_C = coincidir(_CADENA[_C])
                _C = coincidir(line)

                print(t, end='')
            else:
                print("\033[31m" + "\nERROR DE SINTAXIS")
                print("\033[39m")

                _GLOBFLAG = False

                exit()

            line = fp.readline()

    return _C  

'''
**********************************************************************************
**********************************************************************************
'''        

def coincidir(oper):
    global _GLOBFLAG
    global _CADENA
    global _C

    f = False

    with open(_FILEPATH) as fp:

        line = fp.read()

        while line:
            #if line.find(oper):
            if any(line in s for s in reserved):
                #res = _C + len(_CADENA[_C])
                res = _C + len(line)
                f = True

            line = fp.read()

    if not f:
        print("\033[31m" + "\nSimbolo no reconocido(1)")
        print("\033[39m")  

        _GLOBFLAG = False

        exit()

    return res 

'''
**********************************************************************************
**********************************************************************************
'''             

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

'''
**********************************************************************************
**********************************************************************************
'''   

#Read content of source.txt and save it into variable
def readFile():
    f = open("source.txt", 'r')

    if f.mode == 'r':
        contents = f.read()

        print(contents)

    f.close()

    return contents

'''
**********************************************************************************
**********************************************************************************
'''   

def is_in_reserved(line):
    #Check if current line is in served
    global reserved
    
    f = False
    line_split = line.split()

    for l in line_split:
        if l in reserved:
            f = True

    return f

#menu()            
readFile()