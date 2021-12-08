
if __name__ == "__main__":
    celsius = float(input("Introduce una temperatura den Celsius: "))
    fahrenheit = round(((celsius * 9 / 5) + 32),2)
    print(f"{fahrenheit} ºF")

    pulgadas = float(input("Introduce una cantidad de agua en pulgadas: "))
    centimetros = round((pulgadas *25.5/10),1)
    print(f"{centimetros} cm")
    pass
