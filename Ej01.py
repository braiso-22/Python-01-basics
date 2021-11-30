
if __name__ == "__main__":
    valor = input("Introduce una cantidad de dinero en dolares:")
    tasa = 1.14
    tasa = round(float(valor)*tasa, 2)
    print(f"El valor en euros es {tasa}€ ")
    pass
