import time
import os


# Función para limpiar la pantalla
def limpiar_pantalla():
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')  # Comando para borrar pantalla


# Función de mostrar mensaje con animación
def mostrar_mensaje(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.01)
    print()

# Función para obtener un valor numérico del usuario
def obtener_valor_numerico(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar un número válido.")


# Función para obtener el presupuesto del usuario
def obtener_presupuesto():
    presupuesto = obtener_valor_numerico("¿Cuánto dinero tienes para salir? ")
    mostrar_mensaje("Cuentas con un presupuesto de " + str(presupuesto) + " pesos.")
    return presupuesto


# Función para obtener el nombre del boliche
def obtener_nombre_boliche():
    while True:
        boliche = input("¿A qué boliche te gustaría salir? ")
        if not boliche.isnumeric():  # Verifica que sea texto y no un número
            mostrar_mensaje("Has elegido salir a " + str(boliche.capitalize()) + ".")
            return boliche
        else:
            print("Respuesta inválida. Debes ingresar el nombre del boliche, no un número.")


def precio_entrada():
    precio = obtener_valor_numerico("¿Cuál es el precio de la entrada? ")
    return precio


# Función para obtener la bebida del usuario
def obtener_bebida():
    while True:
        bebida = input("¿Qué bebidas vas a comprar? ")
        if not bebida.isnumeric():  # Verifica que sea texto y no un número
            return bebida
        else:
            print("Respuesta inválida. Debes ingresar el nombre de la bebida que quieras, no un número.")


# Función para obtener el precio de la bebida
def obtener_precio():
    precio = obtener_valor_numerico("¿Cuál es el precio? ")
    return precio


# Función para preguntar si desea tomar otra bebida
def preguntar_tomar_otra_bebida(dinero_restante, bebidas):
    while True:
        respuesta = input("¿Deseas tomar otra bebida? (Sí/No): ").lower()
        if respuesta == "s":
            return elegir_otra_bebida(dinero_restante, bebidas)
        elif respuesta == "n":
            mostrar_mensaje("Has elegido no comprar más bebida!")
            lista_compra(bebidas)
            exit()
        else:
            print("Respuesta inválida. Por favor, ingresa 'S' o 'N'.")
            
        return bebidas

# Funcion para elegir bebida (Lo más importante)
def elegir_bebida():
    bebidas=[]
    while True:
        presupuesto = precio_total()
        bebida = obtener_bebida()
        precio_bebida = obtener_precio()
        dinero_restante = presupuesto - precio_bebida
        if dinero_restante > 0:  # Se seguirá ejecutando el programa si le queda saldo.
            mostrar_mensaje(
                "Has elegido comprar " + str(bebida).lower() + " que cuesta " + str(precio_bebida) + " pesos.")
            mostrar_mensaje("Te quedan " + str(dinero_restante) + " pesos.")
            bebidas.append(bebida) #se utiliza para agregar un elemento (en este caso, una bebida) a una lista
            presupuesto = dinero_restante
            return preguntar_tomar_otra_bebida(dinero_restante, bebidas)
        else:  # Se finaliza el programa debido a que no tienes suficiente saldo.
            mostrar_mensaje("¡No te queda más dinero para comprar bebidas!")
            lista_compra(bebidas)
            exit()


# Función para calcular el presupuesto restante después de restar el precio de la entrada
def precio_total():
    presupuesto = obtener_presupuesto()
    entrada = precio_entrada()
    precioTotal = presupuesto - entrada
    if precioTotal > 0:  # Si la entrada vale menos que el presupuesto que tienes, se seguirá ejecutando el programa.
        mostrar_mensaje("Tu presupuesto es de " + str(precioTotal) + ".")
        return precioTotal
    else:  # Si la entrada vale más de lo que tienes de presupuesto, el programa va a finalizar.
        mostrar_mensaje("¡No tienes dinero para salir!")
        mostrar_mensaje("Programa finalizado.")
        exit()


# Función para elegir otra bebida
def elegir_otra_bebida(dinero_restante, bebidas):
    presupuesto = dinero_restante
    bebida = obtener_bebida()
    precio_bebida = obtener_precio()
    dinero_restante = presupuesto - precio_bebida
    if dinero_restante > 0:
        mostrar_mensaje(
            "Has elegido comprar " + str(bebida).lower() + " que cuesta " + str(precio_bebida) + " pesos.")
        mostrar_mensaje("Te quedan " + str(dinero_restante) + " pesos.")
        bebidas.append(bebida)
        return preguntar_tomar_otra_bebida(dinero_restante, bebidas)
    else:
        mostrar_mensaje("¡No te queda más dinero para comprar bebidas!")
        exit()


# Lista de compra de bebidas
def lista_compra(bebidas):
    mostrar_mensaje("Tu lista de compra:")
    for bebida in bebidas:
        mostrar_mensaje("- " + str(bebida).capitalize())


# Estructura del programa
def ejecucion_programa():
    limpiar_pantalla()
    obtener_nombre_boliche()
    elegir_bebida()
    lista_compra()


# Llamada a la función principal
ejecucion_programa()
