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

#libs
require 'io/console'

$CADENA = String.new #Valor que recibirá el programa para validar, se ingresará al ASD
$GLOBFLAG = false #Variable de control para el programa

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
      print "Saliendo del programa..."
      gets
      exitFlag = true
    else
      puts "Esa opcion no esta disponible en el menu"
      gets
    end

  end #while(!exitFlag)

end

def ASD()
  #Función que tomará el papel y comportamiento del Analizador sintáctico
  #Descendente

  print "Ingresa una cadena => "
  $CADENA = gets

  if $CADENA.length == 1
    print "Cadena aceptada"
    gets
  else
    expr()
  end
end

def expr()
  contador = $CADENA.length
  c = 0
  $GLOBFLAG = true

  #Recorrer cada caracter de la cadena

  while < contador
    c = term()
    c = resto()

    unless c.nil?
      if c >= contador or c.nil?
        break
      end
    else
      break
    end
  end

  if $GLOBFLAG
    puts "Cadena aceptada"
  end
end

#El programa empezará aqui
menu()
