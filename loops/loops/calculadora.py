# UNA CALCULADORA SUMA RESTA
def sumar(a, b):
    resultado = a + b
    return resultado
total =  sumar(2, 3)
print("La suma es:", total)



# resta
def restar(a, b):
    resultado = a - b
    return resultado
# multiplicar
def multiplicar(a, b):
    resultado = a * b
    return resultado
# dividir
def dividir(a, b):  
    if b == 0:
        return "Error: Division by zero"
    resultado = a / b
    return resultado
# potencia
def potencia(a, b):
    resultado = a ** b
    return resultado    
# EXPOTENCIAL
def exponencial(a):
    resultado = 2 ** a
    return resultado
# los numeros imprir en la consola
print("Calculadora")        

print("Suma:", sumar(2, 3))
print("Resta:", restar(5, 2))
print("Multiplicación:", multiplicar(4, 3))
print("División:", dividir(10, 2))
print("Potencia:", potencia(2, 3))
print ("Exponencial:", exponencial(3))

