import sys

def split_pieces(pieces):
    mid = (len(pieces) + 1) // 2
    first_half = pieces[:mid]
    second_half = pieces[mid:]
    
    return first_half, second_half

def read_file(file_path):
    pieces = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(",")
            piece = (int(data[0]), int(data[1]), int(data[2]))
            pieces.append(piece)

    return pieces

def calculate_coordinates(piece):
    return [(piece[0], piece[1]), (piece[2], 0)]

def calculate_contour(left_piece, right_piece):
    contour = []
    h1, h2 = 0, 0 # Alturas de los dos piezas
    i, j = 0, 0 # Indice de las piezas
    current_position = 0 # Posicion actual
    max_height = 0 # Altura maxima
    
    while i < len(left_piece) and j < len(right_piece): # While there are pieces to compare

        if left_piece[i][0] < right_piece[j][0]: # Si pieza izquierda viene antes
            current_position, h1 = left_piece[i] # Actualizo la posicion y la altura a la de la pieza izquierda
            max_height = max(h1, h2) # Actualizo la altura maxima
            i += 1 # Avanzo al siguiente indice de la pieza izquierda

        elif left_piece[i][0] > right_piece[j][0]: # Si pieza derecha viene antes
            current_position, h2 = right_piece[j] # Actualizo la posicion y la altura a la de la pieza derecha
            max_height = max(h1, h2) # Actualizo la altura maxima
            j += 1 # Avanzo al siguiente indice de la pieza derecha

        else: # Si las piezas tienen la misma posicion
            current_position, h1, h2 = left_piece[i][0], left_piece[i][1], left_piece[j][1] # Actualizo la posicion y las alturas
            max_height = max(h1, h2) # Actualizo la altura maxima
            i += 1 # Avanzo al siguiente indice de la pieza izquierda
            j += 1 # Avanzo al siguiente indice de la pieza derecha
        
        if not contour or contour[-1][1] != max_height: # Agrego la coordenada si cambio la altura o si es la primera
            contour.append((current_position, max_height))
    
    # Este paso sirve para agregar las piezas restantes si es que quedaron
    contour.extend(left_piece[i:])
    contour.extend(right_piece[j:])
    
    return contour

def get_contour(pieces):
    if len(pieces) == 1:
        # Caso base
        return calculate_coordinates(pieces[0])
    else:
        # Dividir
        first_half, second_half = split_pieces(pieces)
        first_half = get_contour(first_half)
        second_half = get_contour(second_half)

        # Conquistar
        return calculate_contour(first_half, second_half)

def main():
    if len(sys.argv) != 2:
        print("Error: Cantidad de argumentos invalida")
        return
    
    file_path = sys.argv[1]
    pieces = read_file(file_path)
    pieces.sort()
    contour = get_contour(pieces)
    print(contour)

main()