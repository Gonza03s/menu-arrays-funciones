from .validate import *

def get_int(mensaje:str,minimo:int,maximo:int,reintentos:int) -> int | None:

    numero_ingresado = input(mensaje)
    numero_ingresado = int(numero_ingresado)

    numero_validado = validate_number(numero_ingresado,minimo,maximo,reintentos)
    
    return numero_validado


def get_float(mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos:int) -> float | None:

    numero_ingresado = input(mensaje)
    numero_ingresado = float(numero_ingresado)

    while numero_ingresado < minimo or numero_ingresado > maximo:
        numero_ingresado = input(mensaje_error)
        numero_ingresado = float(numero_ingresado)
        reintentos -= 1

        if reintentos == 0:
            print("agotaste los intentos!")
            numero_ingresado = None
            break
    
    return numero_ingresado


def get_string(mensaje:str,longitud:int,mensaje_error:str,reintentos:int) -> str | None:

    respuesta_usuario = input(mensaje)

    respuesta = validate_length(respuesta_usuario,longitud,mensaje_error,reintentos) 

    # respuesta_usuario = validate_length_two(respuesta_usuario,5,10,mensaje_error,reintentos)

    return respuesta

