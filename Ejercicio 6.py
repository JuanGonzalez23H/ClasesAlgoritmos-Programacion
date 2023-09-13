#Este programa va a tener como finalidad mezclar varios elementos que pueda solicitar el usuario 
#Vamos a colocar diferentes metodos para realizar activades simples o secuenciales. Del mismo modo permitira realizar salidad de informacion
#sujetas a condiciones logicas

print ("____________Inicio del programa____________")
print ("")
print ("____________Primer modulo de seguridad____________")

Edad = int ( input ("Ingresa tu edad: "))

print ("")

if Edad < 18 :
    print ("Eres menor de edad")
else:
    print ("Eres mayor de edad")

print ("")
print ("____________Segundo modulo de seguridad____________")
print ("")

print ("Su contraseña fue enviada exitosamente al correo")

Clave_Mayor_Edad = float (input ("Ingresa la contraseña enviada a su correo: "))
password = float (input ("Ingrese la contraseña que fue enviada a su correo: "))


if Clave_Mayor_Edad == password:
    print ("Contraseña correcta")
else:
    print ("Contraseña incorrecta")

print ("")
print ("____________Tercer modulo de seguridad____________")
print ("")

print ("Escriba una frase o palabra para segir adelante en la autenticacion")
print ("")

frase = str ( input ("Introduce un frase: "))

print ("")

vocal = str (input ("Introduce una vocal en minuscula: "))
frase1 = frase.replace (vocal, vocal.upper)

print (frase1)

print ("Usted ha completado los tres modulos de autenticacion...")
print ("...Puede seguir con el pago...")