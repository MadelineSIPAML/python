# AUTO SERVICIO
#  adeline Toledo
def obtener_Articulo( valor):
    if valor == 1:
        return "🍔 Hamburguesa con queso"
    elif valor == 2:
        return "papa fritas🍟"
    elif valor == 3:
        return "Refresco🥤"
    elif valor == 4:
        return "Helado🍦"
    elif valor == 5:
        return "galleta🍪"
    else:
        return "Articulo no disponible"

    """
    Descripcion  de la (F) :
    
  Esta función  Hace que el Articulo Se devuelva depende del numero que elege el Usuario.
    
    """
print(obtener_Articulo(int(input("Elige You PEDIDO"))))  # 🍔 Hamburguesa con queso