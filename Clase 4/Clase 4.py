# Bool
a= True
print(type(a))
a+1
b= False
b+1

# Listas
# 1.1 Homegeneas
lista = [1,2,3,3,4]
type(lista)
# 1.2 Heterogenas
lista_1=[1,2.3, True,'David']
print(lista_1)
lista_de_otra_forma= list((1,2,3,True,1+2j))
print(lista_de_otra_forma)

# Tuplas
tupla_1 = (1,2,True, False, 1+3j)
print(type(tupla_1))
tupla_2= tuple((1,3,False))
print(tupla_2)
# tupla_2[0]=10 # Inmutabilidad (No se puede)
tupla_3= list(tupla_1) # Casting !!

#Sets
#help(set())
set_1= {1,2,3,4}
set_2=set((1,2,3))
type(set_2)
set_A= {123, 456, 567, 764}
set_B= {123, 456, 563, 761}
print(set_A.intersection(set_B))
print(set_A.union(set_B))
print(set_A.difference(set_B)) # ESTO NO ES SIMETRICO
print(set_B.difference(set_A)) # ESTO NO ES SIMETRICO
set_A.symmetric_difference(set_B) # EXCLUSIVE OR 
#set_A.issubset(set_B)
set_A.discard(123)
set_A.update({5,6,7})
set_A

# Dicts
diccionario_1 ={
    "123445555" : "Sociedad Pepito",
    "123445768" : "Sociedad Juan",
    1234555 : "David",
    True:  1234.45,
    23.4: "Pedro",
    (1,2): "Pedro",
    #4: 2,
    4: 1
}
type(diccionario_1)
#diccionario_1.clear()
diccionario_2= diccionario_1.copy()
diccionario_2.get("123445555","David")
diccionario_2.items()
diccionario_2.keys()
diccionario_2.values()
#diccionario_2[12345551112]= 10
diccionario_2