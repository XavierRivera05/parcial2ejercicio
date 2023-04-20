#Bienvenida
print("Hola ing bienvenido a nuestro programa,parte dos del parcial")

#Suma de numeros positivos 
n = int(input("Ingrese un número entero positivo: "))
if n <= 0:
    print("El número ingresado no es válido.")
else:
    sum = 0.0
    for i in range(1, n+1):
        sum += 1.0 / i
    print("La suma de la serie es:", sum)
    
print("Fin del programa")