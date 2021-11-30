
if __name__ == "__main__":
    valor1 = input("Introduce un numero sin decimales\n")
    valor2 = input("Introduce otro numero sin decimales\n")

    suma = int(valor1)+int(valor2)
    resta = int(valor1)-int(valor2)
    multiplicacion = int(valor1)*int(valor2)
    division = round(int(valor1)/int(valor2),2)

    print(f"La suma es: {suma}\nLa resta es: {resta}\nLa Multiplicación es: {multiplicacion}\nLa División es: {division}")
