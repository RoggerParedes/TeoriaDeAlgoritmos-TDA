import copy
import sys

def leer_matriz_archivo(nombre_archivo):
    matriz = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split(',')))
            matriz.append(fila)
    return matriz

def actualizar_opt_obtener_ganancia_camino_maximo(n, m, ganacia_maxima_actual, maximo_ganancia_este_oeste, maximo_ganancia_norte_sur, \
                                    camino_maximo_este_oeste, camino_maximo_norte_sur, camino_maximo, opt, manzanas):
    if ganacia_maxima_actual > maximo_ganancia_norte_sur and ganacia_maxima_actual > maximo_ganancia_este_oeste:
        opt[n][m] = ganacia_maxima_actual
        manzanas[n][m] = copy.deepcopy(camino_maximo)
        #print(f"n: {n}, m: {m}, opt: {opt[n][m]}, manzanas: {manzanas[n][m]}")
        return ganacia_maxima_actual, manzanas[n][m]
    elif ganacia_maxima_actual < maximo_ganancia_norte_sur and maximo_ganancia_este_oeste <= maximo_ganancia_norte_sur:
        opt[n][m] = maximo_ganancia_norte_sur
        manzanas[n][m] = copy.deepcopy(camino_maximo_norte_sur)
        #print(f"n: {n}, m: {m}, opt: {opt[n][m]}, manzanas: {manzanas[n][m]}")
        return maximo_ganancia_norte_sur, camino_maximo_norte_sur
    else:
        opt[n][m] = maximo_ganancia_este_oeste
        manzanas[n][m] = copy.deepcopy(camino_maximo_este_oeste)
        #print(f"n: {n}, m: {m}, opt: {opt[n][m]}, manzanas: {manzanas[n][m]}")
        return maximo_ganancia_este_oeste, camino_maximo_este_oeste

def obtener_ganancia_caso_base(matriz, opt, manzanas):
    opt[0][0] = matriz[0][0]
    manzanas[0][0] = [(1, 1)]
    #rint("n: 0, m: 0,", "opt:", matriz[0][0], "manzanas:", manzanas[0][0])
    return matriz[0][0], manzanas[0][0]

def obtener_maximo_ganancia_y_camino(matriz, n, m, maximo_ganancia_este_oeste, maximo_ganancia_norte_sur, \
                                  camino_maximo_este_oeste, camino_maximo_norte_sur, ganancia_posicion_actual, opt, manzanas):
    camino_maximo = []
    ganacia_maxima_actual = ganancia_posicion_actual
    #print(f"n: {n}, m: {m}, ganacia_maxima_actual: {ganacia_maxima_actual}, ganancia_posicion_actual: {ganancia_posicion_actual}")
    for i in range(n + 1):
        for j in range(m + 1):
            if matriz[i][j] > ganancia_posicion_actual:
                ganacia_acumulada = opt[i][j] + ganancia_posicion_actual
                if ganacia_acumulada  > ganacia_maxima_actual:
                    ganacia_maxima_actual = ganacia_acumulada 
                    camino_maximo = copy.deepcopy(manzanas[i][j])
        
    camino_maximo.append((n, m))
    return actualizar_opt_obtener_ganancia_camino_maximo(n, m, ganacia_maxima_actual, maximo_ganancia_este_oeste, maximo_ganancia_norte_sur,\
                                            camino_maximo_este_oeste, camino_maximo_norte_sur, camino_maximo, opt, manzanas)

def obtener_ganancia_y_camino_maximo_posicion_actual(ganancia, n, m, opt, manzanas):
    opt[n][m] = ganancia
    manzanas[n][m] = [(n, m)]
    #print(f"n: {n}, m: {m}, opt: {opt[n][m]}, manzanas: {manzanas[n][m]}")
    return ganancia, manzanas[n][m]

def ganancia_esta_en_opt(opt, n, m):
    return opt[n][m] != 0

def es_posicion_inicial(n, m):
    return n == 0 and m == 0

def tenemos_manzanas_este(m):
    return m - 1 >= 0

def tenemos_manzanas_norte(n):
    return n - 1 >= 0

def max_ganancia(matriz, n, m, opt, manzanas):
    #print(f"PRIMERA n: {n}, m: {m}")
    if ganancia_esta_en_opt(opt, n, m):
        return opt[n][m], manzanas[n][m]
    
    if es_posicion_inicial(n, m):
        return obtener_ganancia_caso_base(matriz, opt, manzanas)
    
    ganancia_posicion_actual = matriz[n][m]
    maximo_ganancia_este_oeste= -1
    maximo_ganancia_norte_sur = -1
    camino_maximo_este_oeste = []
    camino_maximo_norte_sur = []

    if tenemos_manzanas_este(m):
        maximo_ganancia_este_oeste, camino_maximo_este_oeste = max_ganancia(matriz, n, m - 1, opt, manzanas)
    if tenemos_manzanas_norte(n):
        maximo_ganancia_norte_sur, camino_maximo_norte_sur = max_ganancia(matriz, n - 1, m, opt, manzanas)
    

    if maximo_ganancia_este_oeste < ganancia_posicion_actual and maximo_ganancia_norte_sur <= ganancia_posicion_actual:
        return obtener_ganancia_y_camino_maximo_posicion_actual(ganancia_posicion_actual, n, m, opt, manzanas)
    else:
        return obtener_maximo_ganancia_y_camino(matriz, n, m, maximo_ganancia_este_oeste, maximo_ganancia_norte_sur, \
                                             camino_maximo_este_oeste, camino_maximo_norte_sur, ganancia_posicion_actual, opt, manzanas)

def main():
    if len(sys.argv) < 4:
        print("Uso: python tareas.py filas columnas archivo.txt")
        return
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    nombre_archivo = sys.argv[3]
    ganancia_total, manzanas_seleccionadas = 0, []
    if(filas == 0 and columnas == 0):
        print("Manzanas: ", [])
        print("Ganancia total: ", 0)
    else:
        matriz = leer_matriz_archivo(nombre_archivo)
        opt = [[0 for _ in range(columnas)] for _ in range(filas)]
        manzanas = [[[] for _ in range(columnas)] for _ in range(filas)]
        ganancia_total, manzanas_seleccionadas = max_ganancia(matriz, filas-1, columnas-1, opt, manzanas)
        print("Manzanas: ", end="")
        print(" ".join(f"({fila+1},{columna+1})" for fila, columna in manzanas_seleccionadas))
        print("Ganancia: ", end="")
        print(" + ".join(f"{matriz[fila-1][columna-1]}" for fila, columna in manzanas_seleccionadas)+ f" = {ganancia_total}")

if __name__ == "__main__":
    main()