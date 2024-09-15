def parse_tasks_file(filename):
    required_tasks = {}
    with open(filename, "r") as file:
        for line in file:
            split_line = line.split(',')
            required_tasks[(int(split_line[0]), split_line[1])] = list(map(int, split_line[2::]))
    return required_tasks


def parse_earnings_file(filename):
    potential_earnings = {}
    max_earning_per_week = {}
    with open(filename, "r") as earnings_file:
        for line in earnings_file:
            split_line = line.split(',')
            task_number = int(split_line[0])
            earnings = list(map(int, split_line[1::]))
            potential_earnings[task_number] = earnings
            # Se construye un diccionario con las maximas ganancias potenciales
            # para cada semana. La ganancia no necesariamente decrece a medida que pasan las semanas, y
            # siempre se toma la maxima ganancia de las semanas restantes para todas las tareas.
            for index, earning in reversed(list(enumerate(earnings))):
                try:
                    if index < len(earnings) - 1:
                            if max_earning_per_week[index+2] > earning:
                                if max_earning_per_week[index+2] > max_earning_per_week[index+1]:
                                    max_earning_per_week[index+1] = max_earning_per_week[index+2]
                                    continue
                    if max_earning_per_week[index + 1] < earning:
                        max_earning_per_week[index + 1] = earning
                except KeyError:
                    max_earning_per_week[index+1] = earning
    return potential_earnings, max_earning_per_week
