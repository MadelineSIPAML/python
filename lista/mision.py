#ma#madeline  17/03/2025#
tareas=["🏦Sacar dinero del banco",
        "🗑️   hacer la colada",
        "🌳 dar un páseo",
        "✂️ cortarme el cabello",
        "🍵 preparar un té",
        "💻 Termina el capitulo de la Lista",
        "💖 LLamar a mamá",
        "📺 ver Mi Héroe Academia."]

print(tareas[0])
print(tareas[1])
print( tareas[0:3])

# tareas.append("Error ⚠️ ")
# print( tareas)
# indice=tareas.index(" Error   ⚠️")
# print(indice)


try:
    print(tareas[8])
except IndexError as e:
    print(f"¡Error de índice!: ⚠️⚠️⚠️⚠️⚠️   {e}")


tareas[-1]="💅Pintarse las uñas "
 #tareas.insert(3,"💅Pintarse las uñas")
print(tareas)