import csv

def agregar_producto():
    with open('inventario.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        id_producto = input("Ingrese la ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto (Electrónica, Textil, Calzado): ")
        precio = input("Ingrese el precio del producto: ")

        writer.writerow([id_producto, nombre, categoria, precio])
        print("Producto añadido")

def leer_inventario():
    try:
        with open('inventario.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\nInventario de Productos:")
            for row in reader:
                print(f"ID: {row[0]}, Nombre: {row[1]}, Categoría: {row[2]}, Precio: {row[3]}")
    except FileNotFoundError:
        print("El archivo 'inventario.csv' no existe. Agregue productos primero.")

def clasificar_y_exportar():
    electronica = []
    textil = []
    calzado = []

    try:
        with open('inventario.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2].lower() == "electrónica":
                    electronica.append(row)
                elif row[2].lower() == "textil":
                    textil.append(row)
                elif row[2].lower() == "calzado":
                    calzado.append(row)

        with open('clasificacion_productos.txt', mode='w') as file:
            file.write("Productos Electrónica:\n")
            for producto in electronica:
                file.write(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[3]}\n")

            file.write("\nProductos Textil:\n")
            for producto in textil:
                file.write(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[3]}\n")

            file.write("\nProductos Calzado:\n")
            for producto in calzado:
                file.write(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[3]}\n")

        print("Clasificación exportada a 'clasificacion_productos.txt'.")
    except FileNotFoundError:
        print("El archivo 'inventario.csv' no existe. Agregue productos primero.")

def menu():
    while True:
        print('''  
        1. Agregar producto al inventario
        2. Leer el inventario
        3. Clasificar productos y generar archivo de texto
        4. Salir''')
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            leer_inventario()
        elif opcion == "3":
            clasificar_y_exportar()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo")

menu()