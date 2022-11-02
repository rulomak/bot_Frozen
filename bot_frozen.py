import requests
import pandas as pd

""" he intentado hacer este codigo escalable, de manera que se puedan agragar, quitar productos o codigos de descuento
    sin tener que tocar nada"""

#//////////////#
_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
                                             "Limon", "Dulce de Leche"], "quantity": [3, 10, 0, 5]})

_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
                             "heladoFrozen"]

# funciones #


class GeoApi:
    """ defino las variables y una funcion la cual intenta consumir la URL dentro del 'timeout' determinado, si lo logra
        se gestiona para optener la tempetatura en celsius y se muestra el saludo segun temperatura en pehuajo.
        si la coneccion falla se retorna false y por lo tanto el saludo de clima fresco """

    api_key = "67d0d3dd004d4a379d174e9ef046cae5"
    lat = "-35.836948753554054"
    lon = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        while True:
            try:
                url = f"https://api.openweathermap.org/data/2.5/weather?lat={GeoApi.lat}&lon={GeoApi.lon}&appid={GeoApi.api_key}&units=metric"
                res = requests.get(url, timeout=8.05)
                data = res.json()
                temp = data["main"]["temp"]

                if temp > 8:
                    print("************************************************")
                    print("Clima calido un helado Frozen es la mejor opcion")
                    return True
                else:
                    print("********************************************")
                    print("Clima fresco, ideal para comer helado Frozen")
                    return False
            except:
                print("********************************************")
                print("Clima fresco, ideal para comer helado Frozen")
                return False


available = False


def menu():
    """ menu basico, para comprobar funcionamiento """
    while available is False:
        print("*********** MENU ***********")
        print("****************************")
        indice = 1
        for p, c in zip(_PRODUCT_DF.product_name, _PRODUCT_DF.quantity):
            print(f"{indice} {p} - stock {c}")
            indice += 1
        """creo una iteracion por ambas y muestro una cadena literal,   
           se podria haber mostrado simplemente con print(_PRODUCT_DF),  pero no me gusto como quedaba"""

        option = int(input("elije el producto: -> "))
        if option in range(len(_PRODUCT_DF) +1):
            print(f"seleccionaste '{_PRODUCT_DF.product_name[option -1]}' Stock disponible: '{_PRODUCT_DF.quantity[option -1]}'")
            order = int(input("elige la cantidad: "))
            """paso a la funcion (option -1), la cual hace referencia al id del producto 
               y order que contiene la cantidad ordenada"""
            is_product_available(option -1, order)
        else:
            print(f"** Elija una opcion valida entre 1 y {len(_PRODUCT_DF)} **")


def is_product_available(product, order):
    """ recibo el id del producto y la cantidad ordenada
       compruebo si la cantidad ordenada es inferior o igual al stock del producto y asigno True en la variable
       para que salga del while y no vuelva a mostrar el menu."""
    if order <= _PRODUCT_DF.quantity[product]:
        print("gracias")
        global available
        available = True

    else:
        print(" ## no hay stock suficiente ##")
        print(f"cantidad disponible {_PRODUCT_DF.quantity[product]}")
        print()


def validate_discount_code(discount_code, available_code):
    """ en esta funcion se itera por cada letra del str introducido y se verifica si se encuentra en el code valido
        las que no se encuantran se agregan a una variable 'uniques' de tipo set,
        luego se hace lo mismo pero se itera por el code valido y se verifica en el str introducido,
        de igual manera las que no estan se agregan al set 'uniques' luego se verifica que la variable sea menor a 3"""
    uniques = set()
    for i in discount_code:
        if i not in available_code:
            uniques.add(i)

    for i in available_code:
        if i not in discount_code:
            uniques.add(i)

    if len(uniques) < 3:
        return True


def validate_codes_1():
    """ Funcion 3 - creo un while el cual pide al usuario el codigo, luego entra en un for que itera por cada
    palabra dentro de _AVAILABLE_DISCOUNT_CODES,  y le aplica la funcion 'validate_discount_code' a cada una de ellas,
    si retorna True, pone el contador en 11 para salir del while y sale del for con break"""

    counter = 0
    while counter < 10:
        discount_code = input("ingrese su codigo de descuento: ")
        counter += 1
        for code in _AVAILABLE_DISCOUNT_CODES:
            validate_discount_code(discount_code, code)
            if validate_discount_code(discount_code, code):
                print("codigo valido, Pedido confirmado")
                print("**gracias**")
                counter = 11
                break
        if counter < 10:
            print("lamentablemente el codigo no es valido o ya no esta vigente")
            print("vuelve a intentarlo con un nuevo codigo")
        elif counter == 10:
            print("ya has intentado muchas veces, verifica tu codigo y vuelve a intentar mas adelante ")


GeoApi.is_hot_in_pehuajo()
menu()
validate_codes_1()



























