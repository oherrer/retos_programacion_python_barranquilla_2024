def celcius_to_fahrenheit(grados_celcius:float):
    fahrenheit = (grados_celcius*1.8) + 32
    return fahrenheit


if __name__ == '__main__':
    print(celcius_to_fahrenheit(16))



def celcius_to_kelvin(celcius:float):
    kelvin = (celcius+273.15)
    return kelvin

if __name__ == '__main__':
    print(celcius_to_kelvin(18)) 


def kelvin_to_fahrenheit(grados_kelvin:float):
    grados_fahrenheit = (grados_kelvin - 273.15)*9/5+32  
    return grados_fahrenheit  

if __name__ == '__main__':
    print(kelvin_to_fahrenheit(15))   


def kelvin_to_celcius(grados_kelvin:float):
    grados_celcius = (grados_kelvin - 273.15)
    return grados_celcius

if __name__ == '__main__':
    print(kelvin_to_celcius(34))

def fahrenheit_to_celcius(grados_fahrenheit:float):
    grados_celcius = (grados_fahrenheit-32)*9/5   
    return grados_celcius

if __name__ == '__main__':
    print(fahrenheit_to_celcius(14))

def fahrenheit_to_kelvin(grados_fahrenheit:float):
    grados_kelvin = (grados_fahrenheit)*9/5 + 273.15      
    return grados_kelvin

if __name__ == '__main__':
    print(fahrenheit_to_kelvin(24))

