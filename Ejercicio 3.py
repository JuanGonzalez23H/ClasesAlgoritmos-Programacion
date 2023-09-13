#Hagamos una variable en donde el usaurio ingresa una variable numerica y por medio de una secuecnia logica me permita validar un resultado correcto

num = input ("Por favor digite un numero que sea menor a 50 ")
num = (int(num))

#Uso de Boleano

x = True
y = False 

print (bool(num<50))

#Uso de If & Else

if num<50:

    print ("proceso exitoso")
else:
    print ("El numero ingresado es incorrecto, por favor reiniciar el sistema e intentar de nuevo")