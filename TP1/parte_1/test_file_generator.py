import random

def int_to_label(n):
    label = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        label = chr(65 + remainder) + label
    return label

def generate_tareas(num_tareas):
    tareas = []
    for i in range(1, num_tareas + 1):
        precedencias = random.sample(range(1, i), random.randint(0, min(3, i - 1)))
        tarea_line = f"{i},Tarea {int_to_label(i)}" + ("," + ",".join(map(str, precedencias)) if precedencias else "")
        tareas.append(tarea_line)
    return tareas

def generate_ganancias(num_tareas):
    ganancias = []
    for i in range(1, num_tareas + 1):
        ganancia_por_semana = [str(random.randint(5, 50)) for _ in range(num_tareas)]
        ganancias.append(f"{i}," + ",".join(ganancia_por_semana))
    return ganancias

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + "\n")

def generate_files(num_tareas):

    tareas = generate_tareas(num_tareas)
    save_to_file("tareas.txt", tareas)
    print(f"Generated 'tareas.txt' with {num_tareas} tasks.")

    ganancias = generate_ganancias(num_tareas)
    save_to_file("ganancias.txt", ganancias)
    print(f"Generated 'ganancias.txt' with {num_tareas} tasks.")
