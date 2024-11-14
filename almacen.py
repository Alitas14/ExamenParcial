
productos_almacen = {"Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5}, {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}], "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5}, {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}], "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0}, {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],"Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8}, {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}] }

def agregar_producto(almacen, estanteria, nombre, cantidad, precio):
    #Crea un diccionario con el nombre, cantidad y precio del producto, y lo añade a la lista de productos de la estantería.
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    almacen[estanteria].append(producto)
    print(f"Producto {nombre} agregado correctamente a {estanteria}.")

def retirar_producto(almacen, nombre, cantidad):
    for estanteria, productos in almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre:
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f"Producto {nombre} retirado correctamente.")
                    return
                else:
                    print("Error: Cantidad insuficiente.")
                    return
    print("Error: Producto no encontrado.")

def verificar_disponibilidad(almacen, nombre):
    for estanteria, productos in almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre:
                print(f"{nombre} - Cantidad: {producto['cantidad']} en {estanteria}")
                return
    print(f"{nombre} no está disponible.")

def estado_almacen(almacen):
    for estanteria, productos in almacen.items():
        print(f"Estado de {estanteria}:")
        for producto in productos:
            print(f" - {producto['nombre']}: {producto['cantidad']} unidades, Precio: {producto['precio']}")

def transferir_producto(almacen, nombre, cantidad, origen, destino):
    for producto_origen in almacen[origen]:
        if producto_origen["nombre"] == nombre and producto_origen["cantidad"] >= cantidad:
            producto_origen["cantidad"] -= cantidad
            for producto_destino in almacen[destino]:
                if producto_destino["nombre"] == nombre:
                    producto_destino["cantidad"] += cantidad
                    print(f"Producto {nombre} transferido de {origen} a {destino}.")
                    return
            almacen[destino].append({"nombre": nombre, "cantidad": cantidad, "precio": producto_origen["precio"]})
            print(f"Producto {nombre} transferido de {origen} a {destino}.")
            return
    print("Error en la transferencia de producto.")

def optimizar_inventario(almacen):
    max_valor, min_productos = None, None
    for estanteria, productos in almacen.items():
        valor_total = sum(p["cantidad"] * p["precio"] for p in productos)
        cantidad_productos = sum(p["cantidad"] for p in productos)
        if max_valor is None or valor_total > max_valor[1]:
            max_valor = (estanteria, valor_total)
        if min_productos is None or cantidad_productos < min_productos[1]:
            min_productos = (estanteria, cantidad_productos)
    print(f"Estantería con mayor valor: {max_valor[0]}, valor total: {max_valor[1]}")
    print(f"Estantería con menos productos: {min_productos[0]}, total productos: {min_productos[1]}")

def main():
    while True:
        print("\nMenú de Gestión de Almacén")
        print("1. Agregar producto")
        print("2. Retirar producto")
        print("3. Verificar disponibilidad de un producto")
        print("4. Ver estado del almacén")
        print("5. Transferir producto entre estanterías")
        print("6. Optimizar inventario")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            estanteria = input("Ingrese la estantería (A, B, C, D): ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            agregar_producto(productos_almacen, f"Estantería {estanteria.upper()}", nombre, cantidad, precio)
        
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a retirar: ")
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            retirar_producto(productos_almacen, nombre, cantidad)
        
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a verificar: ")
            verificar_disponibilidad(productos_almacen, nombre)
        
        elif opcion == "4":
            estado_almacen(productos_almacen)
        
        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto a transferir: ")
            cantidad = int(input("Ingrese la cantidad a transferir: "))
            origen = input("Ingrese la estantería de origen (A, B, C, D): ")
            destino = input("Ingrese la estantería de destino (A, B, C, D): ")
            transferir_producto(productos_almacen, nombre, cantidad, f"Estantería {origen.upper()}", f"Estantería {destino.upper()}")
        
        elif opcion == "6":
            optimizar_inventario(productos_almacen)
        
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, por favor elige una opción del menú.")

if __name__ == "__main__":
    main()