import math

if __name__ == "__main__":
    cateto1 = float(input("Introduce el primer cateto: "))
    cateto2 = float(input("Introduce el segundo cateto: "))

    hipotenusa = round((math.sqrt((cateto1**2 + cateto2**2))), 2)

    print(f"la hipotenusa es {hipotenusa}")

    pass
