import copy
import sys

def leer_matriz_archivo(nombre_archivo):
    matriz = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split(',')))
            matriz.append(fila)
    return matriz

def max_ganancia(matriz, n, m, memo, manzanas):
    if memo[n][m] != 0:
        return memo[n][m], manzanas[n][m]
    if n == 0 and m == 0:
        memo[n][m] = matriz[0][0]
        manzanas[n][m] = [(n + 1, m + 1)]
        return matriz[0][0], manzanas[n][m]
    value_to_compare = matriz[n][m]
    left = -1
    top = -1
    if m - 1 >= 0:
        left, vec_left = max_ganancia(matriz, n, m - 1, memo, manzanas)
    if n - 1 >= 0:
        top, vec_top = max_ganancia(matriz, n - 1, m, memo, manzanas)
    if left < value_to_compare and top < value_to_compare:
        memo[n][m] = value_to_compare
        manzanas[n][m] = [(n+ 1, m+ 1)]
        return value_to_compare, manzanas[n][m]
    else:
        vec_max = []
        max_value = value_to_compare  
        for i in range(n + 1):
            for j in range(m + 1):
                if matriz[i][j] > value_to_compare:
                    aux = memo[i][j] + value_to_compare
                    if(aux > max_value):
                        max_value = aux
                        vec_max = copy.deepcopy(manzanas[i][j])
        vec_max.append((n+ 1, m+ 1))
       
        if(max_value > top and max_value > left):
            memo[n][m] = max_value
            manzanas[n][m] = copy.deepcopy(vec_max)
            return max_value, manzanas[n][m]
        else:
            if(max_value < top and left <= top ):
                memo[n][m] = max_value
                manzanas[n][m] = copy.deepcopy(vec_max)
                return top, vec_top
            else:
                memo[n][m] = max_value
                manzanas[n][m] = copy.deepcopy(vec_max)
                return left, vec_left
            
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
        memo = [[0 for _ in range(columnas)] for _ in range(filas)]
        manzanas = [[[] for _ in range(columnas)] for _ in range(filas)]
        ganancia_total, manzanas_seleccionadas = max_ganancia(matriz, filas-1, columnas-1, memo, manzanas)
        print("Manzanas: ", end="")
        print(" ".join(f"({fila},{columna})" for fila, columna in manzanas_seleccionadas))
        print("Ganancia: ", end="")
        print(" + ".join(f"{matriz[fila-1][columna-1]}" for fila, columna in manzanas_seleccionadas)+ f" = {ganancia_total}")


if __name__ == "__main__":
    main()