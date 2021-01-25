
# lISTA 
# 1ra parte (CONCEPTOS BASICOS)
# -EXPLICACION
# - iNDICE ,VALOR  + EJEMPLO
# - CREAR LSTAS VACIAS
# - LISTAS CON DIFERENTES OBJETOS

# 2da parte (OPERADORES QUE NOS PERMITEN MANIPULAR LOS DATOS DE UN ALISTA)
# - get , editar ,elimira,anadir 
# - Coger un valor 
# - OPERACIONES MATEMATICAS SOBRE LA LISTA
# - OPERAR EN YA VISTOS (BUCLES FOR)

# -EXPLICACION
#se pueden guardar diferentes tipos de datos, se puede hacer uso de cada indice de la lista 

# - iNDICE ,VALOR  + EJEMPLO
# indice: los numeros que marcan cada casilla de 0 a infinito, le podemos dar cualquier valor
# valor:  lo que le asignamos a la casilla 

# ejemplo lista con valores definidos: 
      #           0         1       2       3  4     5    6     7        8 
listaCompras =['manzana','peras','platanos',1,False,1.0 True,'lejia,', 'pipas']

#- Ejemplo CREAR LSTAS VACIAS
empty_list = []
print(empty_list) # muesta lo que contiene la lista , en este caso vacia!

#Lista con diferentes objetos
listaConOtraLista = ["string",0,[listaCompras]

# get , editar ,elimira,anadir 

# - Coger (get) un valor de la lista
    print(listaCompras[3]) #indico que quiero el objeto con el indice 3

#importante! como coger un objeto de una lista que se encuentra dentro de otra lista?
        print(listaConOtraLista[2][2])
        # ingreso a la primera lista, indico el indice al que quiero ingresar, en este caso es 2.
        # luego ingreso a la lista del item selecionado e indico que indice quiero coger , en este caso tambien es dos, por lo cual me devolvera en "platano"

 #EDITAR UN VALOR(MODIFICARLO)
 #cambiare lejia por  lava vajillas
 listaCompras[[7]] = 'Lavavajillas'
 #creo un print y llamo la lista  y al objeto que queria cambiar en este caso lejia
 print(listaCompras[7])# muestra lavavajillas

 #COMO BORRAR DE LA LISTA
 #VOY A BORRAR PLATANOS ENTONCES DEBO DE usar .remove
 listaCompras.remove('platano')
 #PARA ANADIR DE NUEVO PLATANO debo de usar .append
 listaCompras.append('platanosnuevos') #Lo agraga al ultimo item de la lista!
# En caso de que lo quiera agregar a un item en especial dedo de usar .insert
listaCompras.insert(2 'platanosnuevos')
     
#COMO CONSULTAR EL TAMANIO DE LA LISTA usamos (len(lista a consultar))
print(len(listaCompras))

#COMO CONSULTAR UN INDICE (EN QUE POSICION DE ENCUENTRA UN VALOR) USAMOS .INDEX
print(listaCompras.index('platanosnuevos'))#nos regresa un dos 

# EL MAX  Y EL MIN PARA INDICAR EL MAXIMO DE LA LISTA O EL MENOR EN ESTE CASO 
#EN ESTE CASO MAX = PIPAS , MIN = MANZANAS
# se creo una nueva lista, porque no se puede usar una lista de enteros y string juntos

list2[1,2,3,1,1,1]# creo lista

print(max(list2))
print(min(list2))

# Count es para indicar el numero de veces que se repite un item en una lista
print(list2.count*(1))

# reverse invertir una lista(intercambio de valores)
print(listaCompras.revese*())

#operaciones matematicas sobre la lista # suma los valores indicados (hace la lista mas grande) es decir anade una matriz a la otra
# concatena listas
print(list2 + [1,2,3,1,1,1])
#tambien podria multiplicarlo IMPORTANTE asi mismo puedo - y + 
print(listaCompras *3) anade la cantidad que se quiera

#OPERADOR in YA VISTO EN BUCLES FOR

print('pipas' in listaCompras) #compara si ese elemnto esta dentro de la lista


