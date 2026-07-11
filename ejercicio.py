diccionario_arreglos={
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}
diccionario_bodega={
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
}

def menu():
    print(f"##MENU PRINCIAL##\n1.Unidades por tiempo de arreglo\n2.Busqueda de arreglos por rango de precio")
    print(f"\n3.Actualizar precio de arreglo\n4.Agregar arreglo\n5.Eliminar arreglo\n6.Salir")

def leer_opcion():
    seguir=True
    while seguir:
        try:
            opcion=int(input("Ingrese una opcion: "))
            seguir=False
        except:
            print("Ingresa opcion valida.")
    return opcion

def unidades_tipo():
    total=0
    seguir=True
    while seguir:
        tipo=input("Ingresa tipo de arreglo (ramo,caja,centro): ").lower()
        if tipo=="ramo":
            for i in diccionario_arreglos:
                if diccionario_arreglos[i][1]=="ramo":
                    total=diccionario_bodega[i][1]+total
            print(f"El total de los arreglos de ramo son: {total}")
            seguir=False
        elif tipo=="caja":
            for i in diccionario_arreglos:
                if diccionario_arreglos[i][1]=="caja":
                    total=diccionario_bodega[i][1]+total
            print(f"El total de los arreglos de caja son: {total}")
            seguir=False
        elif tipo=="centro":
            for i in diccionario_arreglos:
                if diccionario_arreglos[i][1]=="centro":
                    total=diccionario_bodega[i][1]+total
            print(f"El total de los arreglos de centro son: {total}")
            seguir=False
        else:
            print("ERROR, parametro invalido.")

def busqueda_precio():
    seguir = True
    while seguir:
        try:
            precio_min=int(input("Ingresa el precio minimo: "))
            if precio_min>0:
                seguir =False
        except:
            print("ERROR, precio invalido.")
    seguir = True
    while seguir:
        try:  
            precio_max=int(input("Ingresa el precio maximo: "))
            seguir=False
        except:
            print("ERROR, precio invalido.")
    if precio_max<9990:
        print("No hay arreglos de ese precio.")
    elif precio_min>29990:
        print("No hay arreglos de ese precio.")
    else:    
        for i in diccionario_bodega:
            if precio_min<int(diccionario_bodega[i][0])<precio_max:
                print(f"El arreglo {diccionario_arreglos[i][0]} cuesta {diccionario_bodega[i][0]}.")

def actualizar_precio():
    seguir =True
    while seguir:
        try:
            actualizar = input("Ingresa el cOdigo del arreglo FLO (FLO1-6): ").strip().upper()
            if actualizar in diccionario_bodega:
                nuevo_precio = int(input("Ingresa nuevo precio: "))
                if nuevo_precio > 0:
                    diccionario_bodega[actualizar][0] = nuevo_precio
                    print(f"Precio actualizado para {actualizar}: {nuevo_precio}")
                    seguir=False
                else:
                    print("El precio debe ser mayor que 0.")
            else:
                print("Codigo invAlido. Usa FLO1, FLO2, FLO3, FLO4, FLO5, FLO6.")
        except:
            print("ERROR, Ingresa un numero valido para el precio.")

def agregar_arreglo(codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades):
    if codigo in diccionario_bodega or codigo in diccionario_arreglos:
        return False
    
    diccionario_bodega[codigo] = [precio, unidades]
    diccionario_arreglos[codigo] = [nombre, tipo, color_principal, tamano.upper(),True if incluye_tarjeta.lower() =="s" else False,temporada]
    return True
def validar_codigo(codigo):
    return bool(codigo.strip()) and codigo not in diccionario_bodega and codigo not in diccionario_arreglos

def validar_nombre(nombre):
    return bool(nombre.strip())

def validar_tipo(tipo):
    return tipo.strip().lower() in ["ramo", "caja", "centro"]

def validar_color(color_principal):
    return bool(color_principal.strip())

def validar_tamano(tamano):
    return tamano.upper() in ["S", "M", "L"]

def validar_incluye_tarjeta(valor):
    return valor.lower() in ["s", "n"]

def validar_temporada(temporada):
    return bool(temporada.strip())

def validar_precio(precio):
    return isinstance(precio, int) and precio > 0

def validar_unidades(unidades):
    return isinstance(unidades, int) and unidades >= 0

def opcion_agregar_arreglo():
    codigo = input("Codigo del arreglo (FLOx): ").strip().upper()
    nombre = input("Nombre: ").strip()
    tipo = input("Tipo (ramo/caja/centro): ").strip().lower()
    color_principal = input("Color principal: ").strip()
    tamano = input("Tamaño (S/M/L): ").strip().upper()
    incluye_tarjeta = input("¿Incluye tarjeta? (s/n): ").strip().lower()
    temporada = input("Temporada: ").strip()
    try:
        precio = int(input("Precio: "))
        unidades = int(input("Unidades: "))
    except ValueError:
        print("Error: precio y unidades deben ser números enteros.")
        return
    if not validar_codigo(codigo):
        print("Error: codigo invalido o ya existente.")
        return
    if not validar_nombre(nombre):
        print("Error: nombre invalido.")
        return
    if not validar_tipo(tipo):
        print("Error: tipo invalido (ramo/caja/centro).")
        return
    if not validar_color(color_principal):
        print("Error: color invalido.")
        return
    if not validar_tamano(tamano):
        print("Error: tamaño debe ser S, M o L.")
        return
    if not validar_incluye_tarjeta(incluye_tarjeta):
        print("Error: incluye tarjeta debe ser 's' o 'n'.")
        return
    if not validar_temporada(temporada):
        print("Error: temporada invalida.")
        return
    if not validar_precio(precio):
        print("Error: precio debe ser mayor que 0.")
        return
    if not validar_unidades(unidades):
        print("Error: unidades debe ser mayor o igual a 0.")
        return
    if agregar_arreglo(codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades):
        print(f"Arreglo {nombre} agregado exitosamente con codigo {codigo}.")
    else:
        print("Error: el codigo ya existe.")


def buscar_codigo(codigo):
    codigo = codigo.strip().upper()
    return codigo in diccionario_bodega and codigo in diccionario_arreglos

def eliminar_arreglo(codigo):
    codigo = codigo.strip().upper()
    if buscar_codigo(codigo):
        del diccionario_bodega[codigo]
        del diccionario_arreglos[codigo]
        return True
    else:
        return False

def opcion_eliminar_arreglo():
    codigo = input("Ingrese el codigo del arreglo a eliminar (FLOx): ").strip().upper()
    if eliminar_arreglo(codigo):
        print("Arreglo eliminado.")
    else:
        print("El codigo no existe.")

def ejecutar_menu():
    salir = False
    while not salir:
        menu()
        opcion = leer_opcion()
        if opcion == 1:
            unidades_tipo()
        elif opcion == 2:
            busqueda_precio()
        elif opcion == 3:
            actualizar_precio()
        elif opcion == 4:
            opcion_agregar_arreglo()
        elif opcion == 5:
            opcion_eliminar_arreglo()
        elif opcion == 6:
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            salir = True
        else:
            print("Opcion invalida.")
ejecutar_menu()