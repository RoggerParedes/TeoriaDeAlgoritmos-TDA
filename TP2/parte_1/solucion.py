import sys

def leer_matriz_ganancias(archivo, n, m):
    with open(archivo, 'r') as f:
        matriz = []
        for index, linea in enumerate(f):
            fila = list(map(int, linea.strip().split(',')))
            if len(fila) != m:
                raise ValueError(f"Error en la fila {index + 1}: El número de columnas no coincide con el valor especificado ({m} columnas esperadas, {len(fila)} encontradas).")
            matriz.append(fila)
        if len(matriz) != n:
            raise ValueError(f"Error: El número de filas no coincide con el valor especificado ({n} filas esperadas, {len(matriz)} encontradas).")
        return matriz

def tareas(n, m, archivo):
    matriz = leer_matriz_ganancias(archivo, n, m)
    dp = [[0] * m for _ in range(n)]
    path = [[None] * m for _ in range(n)]

    # Empezamos en la cuadra más al sureste (n-1, m-1)
    dp[n-1][m-1] = matriz[n-1][m-1]
    path[n-1][m-1] = [(n, m)]

    # Llenamos la tabla DP
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i < n-1 and matriz[i][j] < matriz[i+1][j]:
                if dp[i+1][j] > dp[i][j]:
                    dp[i][j] = dp[i+1][j] + matriz[i][j]
                    path[i][j] = path[i+1][j] + [(i+1, j+1)]
            if j < m-1 and matriz[i][j] < matriz[i][j+1]:
                if dp[i][j+1] > dp[i][j]:
                    dp[i][j] = dp[i][j+1] + matriz[i][j]
                    path[i][j] = path[i][j+1] + [(i+1, j+1)]

    # La mayor ganancia se encuentra en dp[0][0]
    print("Manzanas seleccionadas:", path[0][0])
    print("Ganancia total:", dp[0][0])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python tareas.py <n> <m> <archivo>")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        archivo = sys.argv[3]
        tareas(n, m, archivo)