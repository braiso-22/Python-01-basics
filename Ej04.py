
if __name__ == "__main__":
    suspensos = int(input("Introduce los suspensos: "))
    suficientes = int(input("Introduce los suficientes: "))
    notables = int(input("Introduce los notables: "))
    sobresalientes = int(input("Introduce los sobresalientes: "))

    total = suficientes+notables+sobresalientes+suspensos
    aprobados = total - suspensos

    porcentaje_aprobados = round(aprobados * 100/total)
    porcentaje_notables = round(notables * 100/total)
    porcentaje_sobresalientes = round(sobresalientes * 100/total)
    print(f"Han aprobado el {porcentaje_aprobados} %")
    print(f"Han sacado notable el {porcentaje_notables}%")
    print(f"Han sacado sobresaliente el {porcentaje_sobresalientes}%")
    pass
