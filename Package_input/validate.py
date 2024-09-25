
def validate_number(numero:int,minimo:int,maximo:int,reintentos:int) -> int | None:

    while numero < minimo or numero > maximo:

        reintentos -= 1
        print(f"te quedan {reintentos} reintentos")
        numero = input(f"Error ingresar entre {minimo} - {maximo}: ")
        numero = int(numero)

        if reintentos == 0:
            print("Reitentos agotados")
            numero = None
            break

    return numero



def validate_length_two(longitud,minimo,maximo,mensaje_error,reintentos):

    while len(longitud) < minimo or len(longitud) > maximo:
        
        reintentos -= 1
        print(f"Reintentos restantes -> {reintentos}")
        longitud = input(mensaje_error)

        if reintentos == 0:
            print("Reintentos agotados")
            longitud =  None
            break

    return longitud




def validate_length(mensaje:str,longitud:int,mensaje_error:str, reintentos:int) -> str | None:

    while len(mensaje) != longitud:
        reintentos -= 1
        print(f"Intentos restantes: {reintentos} ")

        mensaje = input(mensaje_error)

        if reintentos == 0:
            mensaje = None
            break

    return mensaje















