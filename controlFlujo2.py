#COMO SE ESTRUCTURAN LAS SENTENCIAS EN PYTHON 

# .-sentencias if
# .-sentencias else
# .-Ejemplo donde se muestra (combinacion con operadores)
# .-for loops
# .-while loops
# . switch


# sentencias if
#if condicionante:
#   sentencias
# .-Ejemplo donde se muestra (combinacion con operadores)
inputUser = input() 
print( 'con la palabra no y ok en caso de que sea no (cancela lanzamiento) y en caso de que sea ok lanzara el misil')
if (inputUser == 'ok'):# (tengo que quitar los puntos y ponerlos al final tambien puedo hacer mas validaciones, tipo or inputUser == 'y'
    print(' lanzando  misil....')
elif (inputUser == 'no'):
    print('No lo vas a lanzar..')


# for loops: poner una condicion y mientras dure esa condicion se ejecuta el codigo
# en el for normalmente se pone un limite para que se repita

listaCompras = ['manzana', ' peras', 'bananas']
# vamos a recorrer la lista y lo vamos a mostrar en la terminal con un salto de linea
for frutaDeLaLista in listaCompras:
    print(frutaDeLaLista + '\n')


# while loops
# vamos a hacer un contador 
count = 1
while count <=5:
    print(count)
    count +=1

print("termino de conteo") #mostrara hasta 5

#switch:  en python no exite com tal la terminologia switch pero si se puede hacer con otros controladores

diaElegido = int(input()) #ingresa un numero de la semana

if diaElegido == 1:
    print('Lunes')
elif diaElegido == 2:
    print('Martes')
elif diaElegido == 3:
    print('Miercoles')
elif diaElegido == 4:
    print('Jueves')
elif diaElegido == 5:
    print('Viernes')
elif diaElegido == 6:
    print('Sabado')
elif diaElegido == 7:
    print('Domingo')
else:
    print('No existe')
    #me motrara que dia de la semana segun se indique en la entrada





