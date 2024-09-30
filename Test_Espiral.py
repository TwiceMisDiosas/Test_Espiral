def final_direction(T, cases):
    results = []
    for n, m in cases:
        if n == 1 and m == 1:
            results.append("R")
        elif n == 1:
            results.append("R")
        elif m == 1:
            results.append("D")
        elif n % 2 == 0 and m % 2 == 0 and n % 3 == 0 and m % 3 == 0:  # condición para "U" manteniendo paridad
            results.append("U")
        elif n % 2 == 1 and m % 2 == 1:
            results.append("R")
        elif n % 2 == 0 and m % 2 == 0:
            results.append("D")
        elif n % 2 == 0:
            results.append("L")
        else:  # m % 2 == 0
            results.append("D")
    return results

# Pedir el número de casos de prueba
T = int(input("Ingrese el número de casos de prueba: "))
cases = []

for i in range(T):
    n, m = map(int, input(f"Ingrese N y M para el caso {i + 1} (separados por espacio): ").split())
    cases.append((n, m))

# Obtener y mostrar los resultados
results = final_direction(T, cases)

for result in results:
    print(result)
