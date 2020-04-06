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

$CADENA = 0 #Valor que recibirá el programa para validar, se ingresará al ASD

def menu()
  exitFlag = false

  while(!exitFlag)
    #Limpiar pantalla y reinicio de variables
    system "cls"
    finalString = ""
    turns = 0
    c = 0

    #Menú del programa
    puts "\t ------------------------------------"
    puts "\t|             PRACTICA 3             |"
    puts "\t ------------------------------------"
    puts "(1) Ingresar cadena"
    puts "(2) Salir del programa"
    print "Ingresar opcion: "

    menuOption = gets

    if Integer(menuOption) == 1
      #Llamar al Analizador Sintáctico Descendente
      ASD()
    elsif Integer(menuOption) == 2
      #Convertir la bandera de salida a verdadero, de esta forma, saliendo del
      #programa
      exitFlag = true
    end

  end #while(!exitFlag)

end

def ASD()
  #Función que tomará el papel y comportamiento del Analizador sintáctico
  #Descendente

  print "Ingresa una cadena => "
  cadena = gets

  if cadena = "" or cadena " "
    puts "Cadena aceptada"
    gets
  else
    expr()
  end
end

def expr()

end

#El programa empezará aqui
menu()
