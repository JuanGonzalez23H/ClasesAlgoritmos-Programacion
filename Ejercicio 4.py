#vamos a crear un codigo que realice por pantalla un calculo de variables, que permita sumar, restar y hacer operaciones para mostrar al final un resultado de cada operacion y a su vez crear una tabla de la verdad y cada una de las operaciones usando "bool o usando and y or"

num1 = float (input ("Por favor digite un numero entero "))
num2 = float (input ("Por favor digite un numero entero mayor al anterior "))

print ( num1 + num2 )
print ( num1 - num2 )
print ( num1 * num2 )
print ( num1 / num2 )
print ( num1 % num2 )
print ( " " )

X = True
Y = False

print ("Tabla de verdad con conjuncion: ")

print ( " " )
print ("El numero 1 y el numero 1 son:")
print (bool( num1 == num1 ))

print ( " " )
print ("El numero 1 y el numero 2 son:")
print (bool( num1 == num2 ))
print ( " " )

print ("Tabla de la verdad con disyuncion: ")

print ( " " )
print ("El numero 1 y el numero 1 son: ")

if num1==num1:

    print ("True")

else:

    print ("False")

print ( " " )
print ("El numero 1 y el numero 2 son: ")

if num1>num2:

    print ("False")

else:

    print ("True")

print ( " " )