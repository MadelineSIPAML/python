# Madeline toledo
# ALCANCE GLOBAL

def sumar (a, b):
    respuesta = a + b
    return respuesta
print( sumar(4, 2))
# GLOBAL
respuesta = 0
def sumar (a, b):
    global respuesta
    respuesta = a + b
    return respuesta
print(sumar(4, 2))
