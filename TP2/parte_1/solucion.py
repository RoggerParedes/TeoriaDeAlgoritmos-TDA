import copy

def max_suma_rec(matriz, n, m):
    # Si ya hemos calculado la solución para esta celda, la devolvemos
    if memo[n][m] != 0:
        return memo[n][m]
    
    # Si llegamos al inicio (0, 0), devolvemos su valor
    if n == 0 and m == 0:
        memo[n][m] = matriz[0][0]
        paths[n][m].append([(n, m)])  # Almacena el camino inicial
        return matriz[0][0]
    
    value_to_compare = matriz[n][m]
    
    # Llamadas recursivas para moverse hacia arriba y hacia la izquierda
    left = -1
    top = -1
    vec_max = []
    max_value = 0  # Para almacenar la ganancia máxima en esta celda
    
    # Si se puede mover a la izquierda
    if m - 1 >= 0:
        left = max_suma_rec(matriz, n, m - 1)
    
    # Si se puede mover hacia arriba
    if n - 1 >= 0:
        top = max_suma_rec(matriz, n - 1, m)
    
    # Recorrer todas las celdas anteriores para encontrar el máximo
    for i in range(n + 1):
        for j in range(m + 1):
            if matriz[i][j] > value_to_compare:
                max_aux = memo[i][j] + value_to_compare
                if max_value < max_aux:
                    # Nuevo máximo encontrado, reiniciar lista de caminos
                    vec_max = [copy.deepcopy(p) for p in paths[i][j]]
                    for v in vec_max:
                        v.append((n+ 1, m+ 1))  # Agrega la posición actual al camino
                    max_value = max_aux
                elif max_value == max_aux:
                    # Si el nuevo valor es igual al máximo, agregarlo a los caminos
                    new_paths = [copy.deepcopy(p) for p in paths[i][j]]
                    for v in new_paths:
                        v.append((n+ 1, m+ 1))
                    vec_max.extend(new_paths)  # Agregar nuevos caminos a la lista

    # Si no se encontró ningún camino mayor, usar el valor de la celda actual
    if max_value < value_to_compare:
        vec_max = [[(n+ 1, m+ 1)]]
        max_value = value_to_compare
    
    # Guardar el resultado en la tabla de memoización
    memo[n][m] = max_value
    
    # Almacenar todos los caminos posibles en la tabla de caminos
    paths[n][m] = vec_max
    return memo[n][m]

# Matriz de ejemplo
matriz = [
    [100, 150, 300, 100, 50],
    [80,  100, 80,  120, 100],
    [200, 100, 90,  120, 100],
    [140, 60,  80,  90,  50]
]

# Dimensiones de la matriz
n = len(matriz)
m = len(matriz[0])

# Tabla de memorización para almacenar las ganancias máximas calculadas
memo = [[0 for _ in range(m)] for _ in range(n)]

# Tabla para almacenar los caminos
paths = [[[] for _ in range(m)] for _ in range(n)]

# Llamada a la función recursiva
ganancia = max_suma_rec(matriz, n-1, m-1)

# Imprimir la ganancia máxima
print(f"Ganancia máxima: {ganancia}")

# Imprimir la tabla de memorización (memo)
print("Memo:")
for fila in memo:
    print(fila)

# Imprimir los caminos máximos
print("Caminos máximos:")
for camino in paths[n-1][m-1]:
    print(camino)
