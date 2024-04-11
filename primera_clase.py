# Variables: tipos

'''

Tipos de variables:
1. Enteros: Los numeros que estan en el conjunto de los numeros reales.
2. Flotantes: Son los numeros decimales
3. Booleanos: 1 / 0. True or False
4. Strings (Cadenas de textos): Son oraciones o palabras
5. Char (Caracteres): una sola letra 
6. Double: son deciamles con dos o mas cifras significativas

'''

variable_entero = 16

print (type(variable_entero))
print(variable_entero)

variable_flotante = 12.5

print (type(variable_flotante))
print(variable_flotante)

variable_string = "Hola Mundo"

print (type(variable_string))
print(variable_string)

variable_booleano = True

print (type(variable_booleano))
print(variable_booleano)

variable_double = 12.3564456

print (type(variable_double))
print(variable_double)

# Operadores 

"""
Tipos de operadores:
-Suma
-Resta
-Division
-Multiplicacion
-Radicacion
-Potenciacion 
-Modulos

 * ESPECIALES 
    - and
    - or
    - !
    - ==
    - !=
    
"""

suma = variable_entero + 1 # Es 17
resta = variable_double - 36
division = variable_flotante / 2

modulo = variable_entero % 2

#entrada = int(input())

multiplicacion = variable_entero * 3 # Es 48
#print(type (entrada))
print (suma)

# Condicionales 

if ( suma == 17 and multiplicacion == 16 ):
    print ("Ambos son verdaderos")
elif (suma != 17):
    print ("Suma no es 17")
elif (multiplicacion != 16):
    print ("Multiplicacion no es 16")