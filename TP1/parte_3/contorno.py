import sys

piece_global_counter = 0

def get_max(array):
    max_value = 0
    for value in array:
        if value > max_value:
            max_value = value
    return max_value

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
    global piece_global_counter
    piece_global_counter += 1
    return [(piece[0], piece[1], piece_global_counter), (piece[2], 0, piece_global_counter)]

def calculate_contour(coordinates):
    contour = []

    coordinates.sort(key=lambda x: x[0])
    active_pieces = []
    active_heights = []
    current_height = 0
    current_piece = 0

    for coordinate in coordinates:
        print("\n")
        print("Coordinate: ", coordinate)
        print("Current piece: ", current_piece)
        print("Current height: ", current_height)
        print("Active pieces: ", active_pieces)
        print("Active heights: ", active_heights)
        if len(contour) == 0:
            contour.append(coordinate)
            active_heights.append(coordinate[1])
            active_pieces.append(coordinate[2])
            current_height = coordinate[1]
            current_piece = coordinate[2]
        else:
            if coordinate[1] > current_height:
                contour.append(coordinate)
                active_heights.append(coordinate[1])
                active_pieces.append(coordinate[2])
                current_height = coordinate[1]
                current_piece = coordinate[2]
            
            elif coordinate[1] == 0:
                if coordinate[2] == current_piece:
                    if len(active_pieces) == 1:
                        contour.append(coordinate)
                        current_height = 0
                        current_piece = 0
                    else:
                        active_heights.remove(current_height)
                        active_pieces.remove(current_piece)
                        current_height = get_max(active_heights)
                        current_piece = active_pieces[active_heights.index(current_height)]
                        contour.append((coordinate[0], current_height, coordinate[2]))
                else:
                    if coordinate[2] in active_pieces:
                        del active_heights[active_pieces.index(coordinate[2])]
                        active_pieces.remove(current_piece)
            
            elif coordinate[1] < current_height:
                if coordinate[2] in active_pieces:
                    del active_heights[active_pieces.index(coordinate[2])]
                    active_pieces.remove(coordinate[2])
                else:
                    active_pieces.append(coordinate[2])
                    active_heights.append(coordinate[1])
    
    print("Contour: ", contour)

    return contour

def get_contour(pieces):
    if len(pieces) == 1:
        #print("Base case 1", pieces)
        return calculate_coordinates(pieces[0])
    if len(pieces) == 2:
        #print("Base case 2", pieces)
        coordinates = []
        coordinates.extend(calculate_coordinates(pieces[0]))
        coordinates.extend(calculate_coordinates(pieces[1]))
        return calculate_contour(coordinates)
    else:
        first_half, second_half = split_pieces(pieces)
        #print("Recursive case ", first_half, second_half)
        coordinates = []
        coordinates.extend(get_contour(first_half))
        coordinates.extend(get_contour(second_half))
        return calculate_contour(coordinates)

def main():
    if len(sys.argv) != 2:
        print("Error: Cantidad de argumentos invalida")
        return
    
    file_path = sys.argv[1]
    pieces = read_file(file_path)
    contour = get_contour(pieces)
    print(contour)
    


main()