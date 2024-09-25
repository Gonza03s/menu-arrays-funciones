from Package_input.input import *

def crear_lista(valor_inicial:any,limite:int) -> list:

    lista = [valor_inicial] * limite

    return lista

def ingresar_numeros(lista:list) -> list:

    indice = 0

    print("\n--- Ingreso de numeros ---")
    print("Ingrese 10 numeros entre entre -1000 y 1000:")

    while indice < 10:
        numeros_ingresados = get_int(f"Ingrese Numero {indice+1}: ",-1000,1000,3)
        lista[indice] = numeros_ingresados
        indice += 1

    return lista

def mostrar_lista(lista:list) -> int:

    print("Numeros Ingresados: ")

    retorno = None
    if type(lista) == list:
        retorno = -1
        if len(lista) > 0:
            for i in range(len(lista)):
                if lista[i] != None:
                    print(lista[i])
        retorno = 1

    return retorno

def mostrar_positivos_y_negativos(lista:list) -> int:

    cantidad_positivos = 0
    cantidad_negativos = 0
    
    print("\n--- Mostrar positivos y negativos ingresados ---")
    
    retorno = None
    if type(lista) == list:
        retorno = -1
        if len(lista) > 0:
            for i in range(len(lista)):
                
                if lista[i] > 0:
                    cantidad_positivos += 1
                elif lista[i] < 0:
                    cantidad_negativos += 1
        retorno = 1

    if cantidad_positivos > 0:
        print(f"Se ingresaron -> {cantidad_positivos} numeros positivos")
    else:
        print("No se ingresaron numeros positivos") 
    
    if cantidad_negativos > 0:
        print(f"Se ingresaron -> {cantidad_negativos} numeros negativos")
    else:
        print("No se ingresaron numeros negativos") 

    return retorno

def mostrar_sumatoria_numeros_pares(lista:list) -> int:

    numeros_acumulados = 0
    retorno = None
    print("\n--- Sumatoria de numeros pares ---")

    if type(lista) == list:
        retorno = -1
        if len(lista) > 0:
            for i in range(len(lista)):

                if lista[i] % 2 == 0:
                    numeros_acumulados += lista[i]
        retorno = 1
                
    if numeros_acumulados > 0:
        print(f"La sumatoria de los numeros pares ingresados es -> {numeros_acumulados}")
    else:
        print("No se ingresaron numeros pares")
    
    return retorno

def informar_mayor_impar(lista:list) -> int:

    bandera_impar = 0
    mayor_impar = 0
    retorno = None

    print("\n--- El mayor numeros de los impares ---")
    if type(lista) == list:
        retorno = -1
        if len(lista) > 0:
            for i in range(len(lista)):

                if lista[i] % 2 != 0:
                    if lista [i] > mayor_impar or bandera_impar == 0:
                        mayor_impar = lista[i]
                        bandera_impar = 1
        retorno = 1

    if bandera_impar == 1:
        print(f"El mayor numero impar es: {mayor_impar}")
    else:
        print(f"No se encontraron mayores impares")
    
    return retorno

def listar_numeros_pares(lista:list) -> int:

    bandera = 0
    retorno = None
    print("\n--- Numeros pares ingresados ---")

    if type(lista) == list:
        retorno = -1
        if len(lista) > 0:
            for i in range(len(lista)):

                if lista[i] % 2 == 0:
                    print(lista[i])
                    bandera = 1
        retorno = 1

    if bandera == 0:
        print("No se ingresaron numeros pares")

    return retorno

def listar_numeros_posiciones_impares(lista:list) -> int:

    retorno = None
    if type(lista) == list:
        retorno = -1
        if len(lista) > 0:
            print("\n--- Listar numeros en posiciones impares ---")

            for i in range(len(lista)):
                if (i % 2) != 0:
                    print(lista[i])

        retorno = 1

    return retorno



























