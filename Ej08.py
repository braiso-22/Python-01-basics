
if __name__ == "__main__":

    # version 1

    ''' edad1 = int(input("Introduce la edad de la persona: "))
     edad2 = int(input("Introduce la edad de la persona: "))
     edad3 = int(input("Introduce la edad de la persona: "))
     edad4 = int(input("Introduce la edad de la persona: "))

     media = round(((edad1+edad2+edad3+edad4)/4), 2)
     print(f"La edad media es {media} años")'''

    # version 2
    suma_edades = int(input("Introduce la edad de la persona: ")) + \
        int(input("Introduce la edad de la persona: ")) + \
        int(input("Introduce la edad de la persona: ")) + \
        int(input("Introduce la edad de la persona: "))

    media = round((suma_edades/4), 2)
    print(f"La edad media es {media} años")

    # se puede hacer lo mismo pero sin la variable media teniendo solo una variable
    
    pass
