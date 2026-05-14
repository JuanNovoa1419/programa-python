# Nombre del estudiante: Juan Camilo Novoa Zapata 
# Grupo 213022_33
# Problema 2 menu de restaurante
# Autoria propia 


# MATRIZ DEL MENÚ
# [Nombre del Producto, Categoría, Precio Base]

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



# FUNCIÓN PARA CALCULAR PRECIO FINAL

def calcular_precio_final(categoria, precio_base):

    # Aplicar descuento del 15%
    if categoria == categoria_objetivo and precio_base > umbral_precio:

        descuento = precio_base * 0.15
        precio_final = precio_base - descuento

    # Mantener precio original
    else:

        precio_final = precio_base

    return precio_final



# MOSTRAR MENÚ

print("========== MENÚ DEL RESTAURANTE ==========\n")

for i in range(len(menu)):

    nombre = menu[i][0]
    precio_base = menu[i][2]

    print(i + 1, "-", nombre, "- Precio: $", precio_base)

print("-----------------------------------")



# ELEGIR PRODUCTO

print("\nSeleccione el número del producto que desea comprar:")
opcion = int(input("Opción: "))



# VALIDAR OPCIÓN

if opcion >= 1 and opcion <= len(menu):

    producto = menu[opcion - 1]

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Calcular precio final
    precio_final = calcular_precio_final(categoria, precio_base)

   
    # FACTURA FINAL
    
    print("\n========== FACTURA ==========")
    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)

    # Mostrar si aplica promoción
    if precio_final < precio_base:
        print("Promoción aplicada: 15% de descuento")
    else:
        print("Promoción aplicada: No aplica")

    print("Precio Final: $", round(precio_final))
    print("=============================")

else:

    print("\nOpción no válida.")
