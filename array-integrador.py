from os import system
from Package_Arrays.array_generales import *
from Package_Arrays.especificas import verificar_retorno


def menu_principal():

    lista = crear_lista(valor_inicial = None, limite = 10)
    datos_ingresados = False

    while True:
        print("\n---- Menu Principal ----")

        opcion_usuario = input("1. Ingresar Numeros\n2. Mostrar la cantidad de numeros positivos y negativos\n3. Mostrar la sumatoria de numeros pares\n4. Informar el mayor de los numeros impares\n5. Listar todos los numeros ingresados\n6. Listar todos los numeros pares\n7. Listar los numeros de las posiciones impares\n8. Salir\n------------------------------------------------------------\nSeleccione una opcion: ")

        if opcion_usuario == "1":
            lista = ingresar_numeros(lista)
            datos_ingresados = True
            print("Numeros ingresados correctamente")
        elif opcion_usuario == "8":
            print("Cerrando programa...")
            break
        elif datos_ingresados:

            match opcion_usuario:
                case "2":
                    retorno = mostrar_positivos_y_negativos(lista)
                    verificar_retorno(retorno)
                    system("pause")
                    system("cls")
                case "3":
                    retorno = mostrar_sumatoria_numeros_pares(lista)
                    verificar_retorno(retorno)
                    system("pause")
                    system("cls")
                case "4":
                    retorno = informar_mayor_impar(lista)
                    verificar_retorno(retorno)
                    system("pause")
                    system("cls")
                case "5":
                    retorno = mostrar_lista(lista)
                    verificar_retorno(retorno)
                    system("pause")
                    system("cls")
                case "6":
                    retorno = listar_numeros_pares(lista)
                    verificar_retorno(retorno)
                    system("pause")
                    system("cls")
                case "7":
                    retorno = listar_numeros_posiciones_impares(lista)
                    verificar_retorno(retorno)
                    system("pause")
                    system("cls")
                case _:
                    print("\nOpcion incorrecta, reintente")
        else:
            print("Error, debe ingresador datos primero (opcion 1)")


menu_principal()