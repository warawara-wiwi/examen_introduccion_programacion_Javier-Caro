def menu():
    print(f"##MENU PRINCIPAL##\n1.Unidades por tipo de arreglo\n2.Busqueda de arreglos por rango de precio")
    print(f"\n3.Actualizar precio de arreglo\n4.Agregar arreglo\n5.Eliminar arreglo\n6.Salir")

def leer_opcion():
    seguir = True
    while seguir:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if 1 <= opcion <= 6:
                seguir = False
            else:
                print("Ingresa opcion valida.")
        except:
            print("Ingresa opcion valida.")
    return opcion

def unidades_tipo(tipo, arreglos, bodega):
    total = 0
    for i in arreglos:
        if arreglos[i][1].lower() == tipo.lower():
            total = bodega[i][1] + total
    print(f"El total de unidades disponibles de tipo {tipo} son: {total}")

def busqueda_precio(precio_min, precio_max, arreglos, bodega):
    encontrados = False
    resultados = []
    for i in bodega:
        precio = bodega[i][0]
        unidades = bodega[i][1]
        if precio_min <= precio <= precio_max and unidades != 0:
            resultados.append(f"{arreglos[i][0]}--{i}")
            encontrados = True
    resultados.sort()
    if encontrados:
        print(f"Los arreglos encontrados son: {resultados}")
    else:
        print("No hay arreglos en ese rango de precios.")

def buscar_codigo(codigo, arreglos, bodega):
    codigo = codigo.strip().upper()
    return codigo in arreglos and codigo in bodega

def actualizar_precio(codigo, nuevo_precio, bodega, arreglos):
    codigo = codigo.strip().upper()
    if buscar_codigo(codigo, arreglos, bodega):
        bodega[codigo][0] = nuevo_precio
        return True
    else:
        return False

def validar_codigo(codigo, arreglos, bodega):
    codigo = codigo.strip().upper()
    return codigo != "" and codigo not in arreglos and codigo not in bodega

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_tipo(tipo):
    return tipo.strip() != ""

def validar_color(color_principal):
    return color_principal.strip() != ""

def validar_tamano(tamano):
    return tamano.strip().upper() in ["S", "M", "L"]

def validar_incluye_tarjeta(valor):
    return valor.strip().lower() in ["s", "n"]

def validar_temporada(temporada):
    return temporada.strip() != ""

def validar_precio(precio):
    return precio > 0

def validar_unidades(unidades):
    return unidades >= 0

def agregar_arreglo(codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades, arreglos, bodega):
    codigo = codigo.strip().upper()
    if codigo in arreglos or codigo in bodega:
        return False
    else:
        arreglos[codigo] = [nombre, tipo, color_principal, tamano.upper(), incluye_tarjeta, temporada]
        bodega[codigo] = [precio, unidades]
        return True

def eliminar_arreglo(codigo, arreglos, bodega):
    codigo = codigo.strip().upper()
    if buscar_codigo(codigo, arreglos, bodega):
        del arreglos[codigo]
        del bodega[codigo]
        return True
    else:
        return False


arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo ano'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo ano'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otono'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
}

opc = 0
while opc != 6:
    menu()
    opc = leer_opcion()

    if opc == 1:
        tipo = input("Ingrese tipo de arreglo a consultar: ")
        unidades_tipo(tipo, arreglos, bodega)

    elif opc == 2:
        seguir = True
        while seguir:
            try:
                precio_min = int(input("Ingrese precio minimo: "))
                precio_max = int(input("Ingrese precio maximo: "))
                if precio_min < 0 or precio_max < 0 or precio_min > precio_max:
                    print("Debe ingresar valores enteros validos.")
                else:
                    seguir = False
            except:
                print("Debe ingresar valores enteros")
        busqueda_precio(precio_min, precio_max, arreglos, bodega)

    elif opc == 3:
        seguir_actualizando = True
        while seguir_actualizando:
            codigo = input("Ingrese codigo del arreglo: ")
            seguir_precio = True
            while seguir_precio:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        seguir_precio = False
                    else:
                        print("El precio debe ser un entero positivo")
                except:
                    print("El precio debe ser un entero positivo")

            actualizado = actualizar_precio(codigo, nuevo_precio, bodega, arreglos)
            if actualizado:
                print("Precio actualizado")
            else:
                print("El codigo no existe")

            respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
            if respuesta == "n":
                seguir_actualizando = False

    elif opc == 4:
        codigo = input("Ingrese codigo del arreglo: ")
        nombre = input("Ingrese nombre: ")
        tipo = input("Ingrese tipo: ")
        color_principal = input("Ingrese color principal: ")
        tamano = input("Ingrese tamano (S/M/L): ")
        incluye_tarjeta_input = input("Incluye tarjeta? (s/n): ")
        temporada = input("Ingrese temporada: ")

        seguir = True
        while seguir:
            try:
                precio = int(input("Ingrese precio: "))
                seguir = False
            except:
                print("El precio debe ser un numero entero")

        seguir = True
        while seguir:
            try:
                unidades = int(input("Ingrese unidades: "))
                seguir = False
            except:
                print("Las unidades deben ser un numero entero")

        if not validar_codigo(codigo, arreglos, bodega):
            print("El codigo ya existe o es invalido")
        elif not validar_nombre(nombre):
            print("El nombre no puede estar vacio")
        elif not validar_tipo(tipo):
            print("El tipo no puede estar vacio")
        elif not validar_color(color_principal):
            print("El color no puede estar vacio")
        elif not validar_tamano(tamano):
            print("El tamano debe ser 'S', 'M' o 'L'")
        elif not validar_incluye_tarjeta(incluye_tarjeta_input):
            print("Incluye tarjeta debe ser 's' o 'n'")
        elif not validar_temporada(temporada):
            print("La temporada no puede estar vacia")
        elif not validar_precio(precio):
            print("El precio debe ser mayor que 0")
        elif not validar_unidades(unidades):
            print("Las unidades deben ser mayor o igual a 0")
        else:
            incluye_tarjeta = True if incluye_tarjeta_input.lower() == "s" else False
            agregado = agregar_arreglo(codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades, arreglos, bodega)
            if agregado:
                print("Arreglo agregado")
            else:
                print("El codigo ya existe")

    elif opc == 5:
        codigo = input("Ingrese codigo del arreglo a eliminar: ")
        eliminado = eliminar_arreglo(codigo, arreglos, bodega)
        if eliminado:
            print("Arreglo eliminado")
        else:
            print("El codigo no existe")

    elif opc == 6:
        print("Programa finalizado.")
