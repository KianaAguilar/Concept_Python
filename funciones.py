#Funciones 
#que es una funcion y para que sirve? 
#normas de un codigo limpio 
#estructura de una funcion
#ES: def nombre_funcion(parametros de entrada1 parametro 2 ):
#parametros de entrada y salida
#ejemplo de la diferentes combinaciones

#ejemplo de las diferentes combinaciones
itemsAvailableList= ["sarten", "hacha","ruedas","te"]

#No parametros  de entrar  y no devuelve nada
def welcomeMessage():
    print("Bienvenido a shoping market, cargando datos..")
    print("por favor , introduzca su nombre de usuario")

#SI HAY PARAMETROS DE ENTRADA , NO DEVULVE NADA
def requestUsername(username):
  print ("Nombre de usuario disponible," + username)

#si hay parametros de entrada , si devuelve un valor
def isAvaliable (item):
  return item in itemsAvailableList
    

#main
welcomeMessage()
username = input()
requestUsername(username)
print("Por favor introduzca el producto que desea comprobar")
userBuy = input()
print(isAvaliable(userBuy))


