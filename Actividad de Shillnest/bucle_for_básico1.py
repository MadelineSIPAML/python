# madeline Toledo fecha: 15 DE Abril 2024
# Bucles for: Básico 1 
#Ejercicios de bucles for básicos.

#Básico: imprime todos los números enteros del 0 al 100.
print("Básico: imprime todos los números enteros del 0 al 100.")
for i in range(101):
    print(i)
    #Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print("Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500")
for i in range(2, 501, 2):
    print(i)
    #Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
print("Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
 #Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total.
print("Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante)")
suma = 0
for i in range(0, 500001, 2):
    suma += i   
print(suma)  


#Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
print("Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.")
for i in range(2024, 0, -3):
    print(i)        
#los números positivos comenzando desde 0, en cuenta regresiva de 3 en 3.
print(" los números positivos comenzando desde 0, en cuenta regresiva de 3 en 3.")
for i in range(0, 1000, 3):
    print(i)


#Comenzado como Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, 
#el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
print("Contador dinámico 3 variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo.")
numInicial = 3
numFinal = 10
multiplo = 2
#numInicial (3), numFinal (10), multiplo (2)
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
