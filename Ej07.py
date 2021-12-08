
if __name__ == "__main__":
    km_inicial = float(input("Kilometraje inicial: "))
    km_actual = float(input("Kilometraje actual: "))
    litros_inicio = float(input("Litros después de repostar: "))
    litros_actuales = float(input("Litros actuales: "))

    consumo_medio = round(((litros_inicio-litros_actuales)
                          * 100/(km_actual-km_inicial)), 2)
    print(f"El consumo medio de combustible ha sido de {consumo_medio}L/100km")
    pass
