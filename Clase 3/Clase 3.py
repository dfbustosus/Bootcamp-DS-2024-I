"""
skmdkdm
smdkmddl
dmndkmdkmdd
djndkdfnkfnfkrnfkr
"""
print("#####################################")
# 1. Numeros
# 1.1 Enteros
print(type(2))
# 1.2 Decimales
print(type(1.322))
# 1.3 Complejos
print(type(2 +4j))
c= 3-7j
print(type(c))
print(c.real)
print(c.imag)

print("################ NUMEROS #####################")
# 2. Operaciones numericas
# 2.1 Suma
print(2.5+2.1)
# 2.2 Resta
print(4-3.5)
# 2.3 Multiplicacion
print(5*4)
# 2.4 Potencia
print(2**3)
# 2.5 Division
print(5/6)
# 2.6 division (resto)
print(4%3) 
# 2.7 Floor division (division parte entera)
print(5//2) 
print("############### STRINGS ####################")
a = "+5634566677 David"
#a = "5634566677"
print(a.isnumeric()) # Fijense que el print no esta pegado al parentesis 
print(a.isalpha()) # Si solo son letras o texto
print(a)

variable = "David"
numero_float= 32.2
numero_int= 3
print(f"El valor es: {variable}")
print("El valor es: %s con un entero %i y un flotante de: %f" % ("David", numero_int, numero_float))

print("################INDEXACION Y SLICING DE STRINGS###################")
variable = "Juan"
print(variable[0])
print(variable[-1])
print(variable[0:3:2])
print(variable[0:4])
print(variable[-3:-1:1])
print(variable[-3::1])

print("################ ASIGNACION VARIABLES ###################")
# Formas correctas 
entero = 2
_entero =5
entero_=4
entero_a_probar= 5
david_123= 100
_ = 7