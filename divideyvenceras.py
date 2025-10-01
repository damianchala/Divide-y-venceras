import csv

# -------------------------------
# Merge Sort para TAREAS
# -------------------------------
def merge_sort_tareas(tareas):
    if len(tareas) <= 1:
        return tareas

    mid = len(tareas) // 2
    left = merge_sort_tareas(tareas[:mid])
    right = merge_sort_tareas(tareas[mid:])

    return merge_tareas(left, right)

def merge_tareas(left, right):
    resultado = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Comparar primero por prioridad (menor número = más prioridad)
        if left[i]["prioridad"] < right[j]["prioridad"]:
            resultado.append(left[i])
            i += 1
        elif left[i]["prioridad"] > right[j]["prioridad"]:
            resultado.append(right[j])
            j += 1
        else:
            # Si tienen la misma prioridad, ordenar por tiempo (menor a mayor)
            if left[i]["tiempo"] <= right[j]["tiempo"]:
                resultado.append(left[i])
                i += 1
            else:
                resultado.append(right[j])
                j += 1

    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado


# -------------------------------
# Merge Sort para PRODUCTOS
# -------------------------------
def merge_sort_productos(productos):
    if len(productos) <= 1:
        return productos

    mid = len(productos) // 2
    left = merge_sort_productos(productos[:mid])
    right = merge_sort_productos(productos[mid:])

    return merge_productos(left, right)

def merge_productos(left, right):
    resultado = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Ordenar primero por calificación (mayor mejor)
        if left[i]["calificacion"] > right[j]["calificacion"]:
            resultado.append(left[i])
            i += 1
        elif left[i]["calificacion"] < right[j]["calificacion"]:
            resultado.append(right[j])
            j += 1
        else:
            # Si tienen la misma calificación, ordenar por precio (menor a mayor)
            if left[i]["precio"] <= right[j]["precio"]:
                resultado.append(left[i])
                i += 1
            else:
                resultado.append(right[j])
                j += 1

    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado


# -------------------------------
# Función principal
# -------------------------------
if __name__ == "__main__":
    # Ejemplo con tareas
    tareas = [
        {"nombre": "Tarea A", "prioridad": 2, "tiempo": 4},
        {"nombre": "Tarea B", "prioridad": 1, "tiempo": 6},
        {"nombre": "Tarea C", "prioridad": 1, "tiempo": 2},
        {"nombre": "Tarea D", "prioridad": 3, "tiempo": 5},
    ]

    print(" Tareas originales:")
    for t in tareas:
        print(t)

    tareas_ordenadas = merge_sort_tareas(tareas)

    print("\n Tareas ordenadas (por prioridad y tiempo):")
    for t in tareas_ordenadas:
        print(t)

    #  Leer productos desde CSV
    productos = []
    with open("productos.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            productos.append({
                "id": int(row["id"]),
                "nombre": row["nombre"],
                "precio": float(row["precio"]),
                "calificacion": int(row["calificacion"]),
                "stock": int(row["stock"])
            })

    # Ordenar productos
    productos_ordenados = merge_sort_productos(productos)

    print("\n Mejores productos (top 10):")
    for p in productos_ordenados[:10]:
        print(p)
