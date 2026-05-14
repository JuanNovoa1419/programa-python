# Nombre del estudiante: Juan Camilo Novoa Zapata 
# Grupo 213022_33
# Problema 2 menu de restaurante
# Autoria propia 

menu = [
    ["Hamburguesa", "Comida Rápida", 18000],
    ["Pizza", "Comida Rápida", 32000],
    ["Ensalada César", "Saludable", 15000],
    ["Jugo Natural", "Bebidas", 8000],
    ["Pasta Alfredo", "Italiana", 28000],
    ["Perro Caliente", "Comida Rápida", 25000]
]

# Categoría específica para aplicar descuento
categoria_objetivo = "Comida Rápida"

# Umbral mínimo del precio
umbral_precio = 20000


# ==========================================
# FUNCIÓN PARA CALCULAR PRECIO FINAL
# ==========================================
def calcular_precio_final(categoria, precio_base):

    # CONDICIÓN:
    # Aplicar 15% de descuento si:
    # 1. La categoría es igual a la categoría objetivo
    # 2. El precio base es mayor al umbral definido

    if categoria == categoria_objetivo and precio_base > umbral_precio:

        descuento = precio_base * 0.15
        precio_final = precio_base - descuento

    # Mantener el precio original
    # si no se cumplen las condiciones

    else:

        precio_final = precio_base

    return precio_final


# ==========================================
# MOSTRAR MENÚ
# ==========================================
print("========== MENÚ DEL RESTAURANTE ==========\n")

for i in range(len(menu)):

    print(i + 1, "-", menu[i][0])

# ==========================================
# ELEGIR PRODUCTO
# ==========================================
print("\nSeleccione el número del producto que desea comprar:")
opcion = int(input("Opción: "))


# ==========================================
# VALIDAR OPCIÓN
# ==========================================
if opcion >= 1 and opcion <= len(menu):

    producto = menu[opcion - 1]

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Llamar función
    precio_final = calcular_precio_final(categoria, precio_base)

    # ==========================================
    # MOSTRAR RESULTADO
    # ==========================================
    print("\n========== FACTURA ==========")
    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)

    # Mostrar si hubo descuento
    if precio_final < precio_base:
        print("Promoción aplicada: 15% de descuento")
    else:
        print("Promoción aplicada: No aplica")

    print("Precio Final: $", round(precio_final))
    print("=============================")

else:

    print("\nOpción no válida.")