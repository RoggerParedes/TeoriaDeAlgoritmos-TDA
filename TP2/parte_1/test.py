import copy
def max_suma_rec(matriz, n, m):
    # Si ya hemos calculado la solución para esta celda, la devolvemos
    if memo[n][m] != 0:
        return memo[n][m]
    
    # Si llegamos al inicio (0, 0), devolvemos su valor
    if n == 0 and m == 0:
        memo[n][m] = matriz[0][0]
        paths[n][m].append((n, m))
        print(paths)
        return matriz[0][0]
    value_to_compare = matriz[n][m]
    
    # Llamadas recursivas para moverse hacia arriba y hacia la izquierda
    left = -1
    top = -1
    vec_max = []
    max = 0
    
    if(m - 1 >= 0):
        left = max_suma_rec(matriz, n, m - 1)
    if(n - 1 >= 0):
        top = max_suma_rec(matriz, n - 1, m)
    print("******")
    print(vec_max)
    print(n,"-",m)
    for i in range(n + 1):
        for j in range(m + 1):
            print("viendo punto", i,'-',j)
            if (matriz[i][j]> value_to_compare):
                print("Parte 1")
                max_aux = memo[i][j] + value_to_compare
                if(max < max_aux):
                    if (i+1,j+1) not in vec_max:
                        print("la paths[i][j]: ", paths[i][j])
                        vec_max = []
                        vec_max = copy.deepcopy(paths[i][j])
                        vec_max.append((n+1, m+1))
                        print(i,"-",j)
                        print("la vec_max resul: ", vec_max)
                    max = max_aux
            if(max < value_to_compare):
                if (i,j) not in vec_max:
                    print("Parte 2")
                    vec_max = []
                    vec_max.append((n+1, m+1))
                    print(n,"-",m)
                max = value_to_compare
    memo[n][m] = max
    print(paths)
    print(vec_max)
    paths[n][m] = vec_max
    print(paths)
    return memo[n][m]

# Matriz de ejemplo
matriz = [
    [100, 150, 300, 100, 50],
    [80,  100, 80,  120, 100],
    [200, 100, 90,  120, 100],
    [140, 60,  80,  90,  50]
]

matriz3 = [
    [100, 150, 300],
    [80,  100, 80],
    [200, 100, 90],
    [140, 60,  80]
]


matriz4 = [
    [100, 150, 300],
    [80,  100, 80],
    [200, 100, 90],
    [140, 60,  80]
]

matriz1 = [
    [100, 150, 300],
    [80,  100, 80],
    [140, 60,  80],
]

# Ejecutar el algoritmo
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

# Imprimir la tabla de memorización (memo) y los caminos (paths)
print("Memo:")
for fila in memo:
    print(fila)

print("Camino Max:")
# for fila in memo:
#     print(fila)

print(paths[n-1][m-1])