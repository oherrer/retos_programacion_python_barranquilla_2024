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



        

if __name__ = "__main__":
    # Ejemplo de uso
    resultado = multiplicacion(9, 9)
    print(f"9 multiplicado por 9 usando la función suma es: {resultado}") 
