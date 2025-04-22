# AUTO SERVICIO
# Madeline Toledo

def obtener_Articulo(valor):
    """
    Descripción de la función:
    Esta función devuelve el artículo correspondiente según el número elegido por el usuario.
    """
    if valor == 1:
        return "Hamburguesa con queso 🍔"
    elif valor == 2:
        return "Papas fritas 🍟"
    elif valor == 3:
        return "Refresco 🥤"
    elif valor == 4:
        return "Helado 🍦"
    elif valor == 5:
        return "Galleta 🍪"
    else:
        return "Artículo no disponible ❌"

print("🍽️ Menú de Auto Servicio:")
print("1. Hamburguesa con queso 🍔")
print("2. Papas fritas 🍟")
print("3. Refresco 🥤")
print("4. Helado 🍦")
print("5. Galleta 🍪")
print("\nElige tu pedido (1-5): ", end="")
pedido = int(input())
print("\n" + obtener_Articulo(pedido))