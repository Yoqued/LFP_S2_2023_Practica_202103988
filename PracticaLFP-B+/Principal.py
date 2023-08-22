import os
import csv
from colorama import Fore
from DatosProductos import *

produc = []

def limpiadorRuta(file_path):
    encoded_path = file_path.encode('ascii', 'ignore')

    cleaned_path = encoded_path.decode('ascii')
    return cleaned_path

def InventarioInicial():
    global produc
    produc = []
    no_repetidos = []
    print(Fore.RESET + '------------------------------------------------')
    print('Ingrese "RUTA DE ARCHIVO" de "INVENTARIO"')
    print('------------------------------------------------')
    Ruta = input(Fore.MAGENTA + 'Ingrese una opcion: ')

    cleaned_path = limpiadorRuta(Ruta)

    try:
        rutaArch = open(cleaned_path, 'r', encoding="UTF-8")
        leer = csv.reader(rutaArch, delimiter=" ")
        for i in leer:

            nombre,cantidad,precio,ubicacion = i[1].split(';')
            try:
                if int(cantidad):
                    verificador = (nombre, ubicacion)
                    print(verificador)
                    if verificador not in no_repetidos:
                        datos = productos(nombre,cantidad,precio,ubicacion)
                        produc.append(datos)
                        no_repetidos.append(verificador)
            except:
                print(Fore.BLUE + f'El producto de "{nombre}" es una Cantidad con punto decimal no sera valida')

        rutaArch.close()
        print(Fore.GREEN + f'"ARCHIVO LEIDO"')
    except FileNotFoundError:
        os.system('cls')
        print(Fore.RED + 'Archivo no encontrado.')
    except Exception as e:
        os.system('cls')
        print(Fore.RED + f'Hubo un problema al cargar el archivo: {e}')

def Movimientos():
    print(Fore.RESET + '------------------------------------------------')
    print('Ingrese "RUTA DE ARCHIVO" de "MOVIMIENTOS"')
    print('------------------------------------------------')
    Ruta = input(Fore.MAGENTA + 'Ingrese una opcion: ')

    cleaned_path = limpiadorRuta(Ruta)

    try:
        rutaArch = open(cleaned_path, 'r', encoding="UTF-8")
        leer = csv.reader(rutaArch, delimiter=" ")
        for i in leer:
            if i[0] == "agregar_stock":
                nombre,cantidad,ubicacion = i[1].split(';')
                try:
                    if int(cantidad):
                        for j in range(len(produc)):
                            if nombre == produc[j].getNombre(): 
                                if ubicacion == produc[j].getUbicacion():
                                    sumatoria = int(produc[j].getCantidad()) + int(cantidad)
                                    produc[j].setCantidad(sumatoria)
                                else:
                                    print(Fore.RED + f'El producto: "{nombre}"; no se en cuentra en "{ubicacion}"')
                except:
                    print(Fore.BLUE + f'El producto de "{nombre}" es una Cantidad con punto decimal no sera valida')
            elif i[0] == "vender_producto":
                nombre,cantidad,ubicacion = i[1].split(';')
                try:
                    if int(cantidad):
                        for j in range(len(produc)):
                            if nombre == produc[j].getNombre():
                                if ubicacion == produc[j].getUbicacion():
                                    if int(produc[j].getCantidad()) > 0:
                                        if int(cantidad) <= int(produc[j].getCantidad()):
                                            sumatoria = int(produc[j].getCantidad()) - int(cantidad)
                                            produc[j].setCantidad(sumatoria)
                                        else:
                                            print(Fore.RED + f'La cantidad de: "{nombre}" sobre pasa nuestro "Inventario"')
                                    else:
                                        print(Fore.RED + f'No hay en exitencia "{nombre}"')
                except:
                    print(Fore.WHITE + f'El producto de "{nombre}" es una Cantidad con punto decimal no sera valida')
        rutaArch.close()
        print(Fore.GREEN + f'"MOVIMIENTOS EXITOSOS"')
    except FileNotFoundError:
        os.system('cls')
        print(Fore.RED + 'Archivo no encontrado.')
    except Exception as e:
        os.system('cls')
        print(Fore.RED + f'Hubo un problema al cargar el archivo: {e}')

def CrearInforme():
    print(Fore.RESET + '------------------------------------------------')
    print('Generando Informe de Inventario')
    print('------------------------------------------------')

    try:
        nombre_archivo = input(Fore.MAGENTA + 'Ingrese un nombre para el informe: ')
        with open(nombre_archivo + '.txt', 'w', encoding="UTF-8") as archivo:
            archivo.write('Informe de Inventario:\n\n')
            archivo.write('{:<15} {:<10} {:<15} {:<15} {:<15}\n'.format("Producto", "Cantidad", "Precio Unitario", "Valor Total", "Ubicación"))
            archivo.write('-' * 70 + '\n')

            for producto in range(len(produc)):
                valor_total = float(produc[producto].getCantidad()) * float(produc[producto].getPrecio())
                archivo.write('{:<15} {:<10} {:<15} {:<15} {:<15}\n'.format(produc[producto].getNombre(), produc[producto].getCantidad(), f'${produc[producto].getPrecio()}', f'${valor_total:.2f}', produc[producto].getUbicacion()))

        print(Fore.GREEN + f'Informe creado exitosamente en "{nombre_archivo}.txt"')
    except Exception as e:
        print(Fore.RED + f'Hubo un problema al crear el informe: {e}')

def MenuInicial():
    while True:
        print(Fore.YELLOW+'------------------------------------------------')
        print(Fore.BLUE+'# Sistema de inventario\n\n')
        print('1. Cargar Inventario inicial')
        print('2. Cargar Instrucciones de movimientos')
        print('3. Crear Informe de inventario')
        print('4. Salir\n\n')
        opcion = input(Fore.MAGENTA+'Ingrese una opcion: ')

        if opcion == "1":
            os.system('cls')
            InventarioInicial()
        elif opcion == "2":
            if not produc:
                print(Fore.RED+'No se ha ingresado un Archivo')
            else:
                os.system('cls')
                Movimientos()
        elif opcion == "3":
            if not produc:
                print(Fore.RED+'No se ha ingresado un Archivo')
            else:
                os.system('cls')
                CrearInforme()
        elif opcion == "4":
           os.system('cls')
           print(Fore.GREEN+'"HASTA PRONTO"')
           break 
        else:
            os.system('cls')
            print(Fore.RED+'"INGRESE VALORES DENTRO DEL RANGO"')


print(Fore.YELLOW+'------------------------------------------------')
print('Practica 1 - Lenguaje dormales y de programacion')
MenuInicial()