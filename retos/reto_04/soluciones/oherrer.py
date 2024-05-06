def incremento(n):
    return n+1

def decremento(n):
    return n-1


def suma (n , m):
    for i in range (m):
        n = incremento(n)
    return n 
def resta (n , m):
    for i in range (m):
        n= decremento(n)
    return -n    


def multiplicacion(n, m):
    """
    Esta función calcula la multiplicación de un número 'n' por otro número 'm'
    utilizando la función 'suma' repetidamente.

    Parámetros:
        n (int): El número que se va a multiplicar.
        m (int): El número de veces que se va a sumar 'n' a sí mismo.

    Retorno:
        int: El resultado de la multiplicación 'n * m'.
    """

        if m == 0:  # Caso base: si m es 0, la multiplicación es 0.
            return 0

        else: 
            # Caso recursivo: si m es mayor que 0, se suma 'n' a sí mismo 
            # 'm' veces y se devuelve el resultado.
            return n + multiplicacion(n, m - 1)


def division_entera(n, m):
  """
    Esta función calcula la división entera de dos números 'n' y 'm' utilizando la
    función 'resta' repetidamente.

    Parámetros:
        n (int): El dividendo (el número que se va a dividir).
        m (int): El divisor (el número por el que se va a dividir).

    Retorno:
        tuple: Una tupla que contiene dos valores:
        cociente (int): El cociente de la división entera (número de veces que se resta 'm' a 'n').
        residuo (int): El residuo de la división entera (lo que queda después de restar 'm' a 'n' todas las veces posibles).
    """

    if m == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")

    cociente = 0
    while n >= m:
        n -= m
        cociente += 1

    residuo = n

    return cociente, residuo



   

if __name__ = "__main__":
    # Ejemplo de uso
    resultado = multiplicacion(9, 9)
    print(f"9 multiplicado por 9 usando la función suma es: {resultado}") 


    # Ejemplo de uso
    cociente, residuo = division_entera(50, 7)
    print(f"División entera de 50 por 7:")
    print(f"Cociente: {cociente}")  # Resultado: 7
    print(f"Residuo: {residuo}")    # Resultado: 1