import numpy as np


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Para sacar la raíz cuadrada ', accion1),
        '2': ('Creamos lista', accion2),
        '3': ('Transformamos lista a array', accion3),
        '4': ('Salir', salir),
        '5': ('Generamos un Array con un rango de numeros con intervalos establecidos', accion5),
        '6': ('Generamos array de un nº a otro nº', accion6),
        '7': ('Generamos array de un nº de zeros', accion7),
        '8': ('Generamos array de un nº de unos', accion8),
        '9': ('Array 2 Dimensiones', accion9),
        '10': ('Array shape contiene informacion sobre array anterior creado', accion10),
        '11': ('Ver el tamaño de Array con size', accion11),
        '12': ('Ver el nº de dimensiones de un Array', accion12),
        '13': ('Multiplicando Arrays las listas no se pueden', accion13),
        '14': ('Multiplicando Arrays metodo rústico ', accion14)

    }

    generar_menu(opciones, '4')


# a = [0, 1, 2, 3, 4, 5]

# Para sacar la raíz cuadradas
def accion1():
    print(np.sqrt(25))


# Creamos lista
def accion2():

    a = [0, 1, 2, 3, 4, 5]
    print(a)
    print(type(a))


# Transformamos lista a array
def accion3():
    # accion2()

    a = np.array([0, 1, 2, 3, 4, 5])

    print(a)
    print(type(a))


# Generamos un Array con un rango de numeros con intervalos establecidos
def accion5():
    # accion2()

    b = np.arange(4, 24, 2)

    print(b)


# Generamos array de un nº a otro nº
def accion6():
    # accion2()

    d = np.linspace(1, 50)
    c = np.linspace(1, 244, 5)

    print(d)
    print(c)


# Generamos array de un nº de zeros
def accion7():
    # accion2()
    f = np.zeros(13)

    print(f)


# Generamos array de un nº de unos
def accion8():
    # accion2()
    f = np.ones(50)

    print(f)


# Array 2 Dimensiones
def accion9():
    # accion2()
    array_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(array_2d)


# Array shape contiene informacion sobre array anterior creado
def accion10():
    # accion2()
    array_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(array_2d.shape)


# Ver el tamaño de Array con size
def accion11():
    # accion2()
    array_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(array_2d.size)


# Ver el nº de dimensiones de un Array
def accion12():
    # accion2()
    array_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(array_2d.ndim)


# Multiplicando Arrays las listas no se pueden
def accion13():
    # accion2()

    lista_1 = [1, 2, 3]
    lista_2 = [4, 5, 6]

    # Error
    # lista_1 * lista_2

    array_1 = np.array(lista_1)

    array_2 = np.array(lista_2)

    print(array_1 * array_2
          )


# Multiplicando Arrays metodo rústico
def accion14():
    # accion2()

    lista_1 = [1, 2, 3]
    lista_2 = [4, 5, 6]

    # Error
    # lista_1 * lista_2

    print([num1*num2 for num1, num2 in zip(lista_1, lista_2)])


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()
