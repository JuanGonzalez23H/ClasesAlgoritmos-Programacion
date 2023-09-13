#listas

#x = "L"
#y = "M"
#z = "N"
#l_list = ["10", "L", "perro", "casa", x, y, z]

#print(l_list)

color = str (input("Cual es su color favorito? "))
materia = str (input("Cual es su materia favorita? "))
NFav = int (input("Cual es su numero favorito? "))
marca = str (input("Cual es su marca de ropa favorita? "))
cel = str (input("Que marca de celular tienes? "))
m = 5+2
l = 9*8
p = 8/2
q = 4-7
r = 0*4+8

Y_list = [ color , materia , NFav , marca , cel , m , l , p , q , r]

Y_list.append ("EAN") #Agregar solo una variable
Y_list.index (7)      #Buscar posicion
Y_list.remove (color) #Quitar variable
Y_list.reverse ()     #Reversar la lista
Y_list.extend ([8, 203, (8*9), 40, "perro", "casa", "pesa"]) #Agregar mas de una variable
Y_list.clear ()       #Eliminar todos los elementos dentro de la lista
contar = Y_list.count (8)
copia = Y_list.copy()
copia [0] = 300

print (copia)
print (contar)
print (Y_list)
