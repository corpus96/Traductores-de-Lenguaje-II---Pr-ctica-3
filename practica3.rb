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
$C = Integer.new #Variable que contará caracter por caracter

def menu()
  exitFlag = false

  while(!exitFlag)
    #Limpiar pantalla y reinicio de variables
    system "cls"
    finalString = ""
    turns = 0
    $C = 0

    #Menú del programa
    puts "\t ------------------------------------"
    puts "\t|             PRACTICA 3             |"
    puts "\t ------------------------------------"
    puts "(1) Ingresar cadena"
    puts "(2) Salir del programa"
    print "Ingresar opcion: "
    STDOUT.flush

    menuOption = gets

    if Integer(menuOption) == 1
      #Llamar al Analizador Sintáctico Descendente
      ASD()
    elsif Integer(menuOption) == 2
      #Convertir la bandera de salida a verdadero, de esta forma, saliendo del
      #programa
      print "Saliendo del programa..."
      STDOUT.flush
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
  STDOUT.flush
  $CADENA = gets

  if $CADENA.length == 1 or $CADENA.length == 0
    print "Cadena aceptada"
    STDOUT.flush
    gets
  else
    expr()
  end
end

def expr()
  contador = $CADENA.length
  $GLOBFLAG = true

  #Recorrer cada caracter de la cadena

  while < contador
    $C = term()
    $C = resto()

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

def term()
  arrPos = $C

  if $CADENA.index(arrPos) =~ /\d/
    t = $CADENA.index(arrPos)
    arrPos = coincidir()
    print t
    STDOUT.flush
end


#El programa empezará aqui
menu()
