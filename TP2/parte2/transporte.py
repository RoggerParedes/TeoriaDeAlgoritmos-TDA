from collections import defaultdict, deque
from itertools import combinations

def construir_grafo(archivo):
    grafo = defaultdict(dict)
    with open(archivo, 'r') as f:
        for linea in f:
            origen, destino = linea.strip().split(',')
            grafo[origen][destino] = 1  # Capacidad de cada ruta es 1.
            grafo[destino][origen] = 1  # Ejes bidireccionales, ya que las rutas son doble mano.
    return grafo

# Implementación del algoritmo de Ford-Fulkerson
def bfs_ford_fulkerson(grafo, source, sink, parent):
    visitados = set()
    queue = deque([source])
    visitados.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v, capacidad in grafo[u].items():
            if v not in visitados and capacidad > 0:
                queue.append(v)
                visitados.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(grafo, source, sink):
    parent = {}
    flujo_maximo = 0
    grafo_residual = defaultdict(dict)
    
    # Inicializamos el grafo residual
    for u in grafo:
        for v in grafo[u]:
            grafo_residual[u][v] = grafo[u][v]
    
    # Mientras encontremos un camino aumentante
    while bfs_ford_fulkerson(grafo_residual, source, sink, parent):
        # Determinamos la capacidad mínima en el camino aumentante
        flujo_camino = float('Inf')
        v = sink
        while v != source:
            u = parent[v]
            flujo_camino = min(flujo_camino, grafo_residual[u][v])
            v = u
        
        # Actualizamos las capacidades en el grafo residual
        v = sink
        while v != source:
            u = parent[v]
            grafo_residual[u][v] -= flujo_camino
            grafo_residual[v][u] += flujo_camino
            v = u
        
        # Sumar el flujo de este camino al flujo máximo
        flujo_maximo += flujo_camino
    
    return flujo_maximo, grafo_residual

# Función para encontrar el corte mínimo
def encontrar_corte_minimo(grafo, source, sink, grafo_residual):
    visitados = set()
    queue = deque([source])
    visitados.add(source)
    
    while queue:
        u = queue.popleft()
        for v, capacidad in grafo_residual[u].items():
            if capacidad > 0 and v not in visitados:
                queue.append(v)
                visitados.add(v)
    
    # Aristas que forman el corte mínimo
    corte_minimo = []
    for u in visitados:
        for v in grafo[u]:
            if v not in visitados and grafo[u][v] > 0:
                corte_minimo.append((u, v))
    
    return corte_minimo

def encontrar_corte_minimo_global(grafo):
    ciudades = list(grafo.keys())
    corte_minimo_global = []
    min_rutas = float('Inf')

    # Probar cada par de ciudades como source y sink
    for source, sink in combinations(ciudades, 2):
        flujo_maximo, grafo_residual = ford_fulkerson(grafo, source, sink)
        corte_minimo = encontrar_corte_minimo(grafo, source, sink, grafo_residual)

        # Verificar si encontramos un corte más pequeño
        if len(corte_minimo) < min_rutas:
            min_rutas = len(corte_minimo)
            corte_minimo_global = corte_minimo

    return corte_minimo_global, min_rutas

def main():
    archivo = 'rutas.txt'  # Archivo de entrada
    grafo = construir_grafo(archivo)
    
    # Buscamos el corte mínimo global
    corte_minimo, cantidad_rutas = encontrar_corte_minimo_global(grafo)
    
    print(f'Cantidad mínima de rutas: {cantidad_rutas}')
    print('Rutas:', ' '.join([f'{u},{v}' for u, v in corte_minimo]))

if __name__ == '__main__':
    main()
