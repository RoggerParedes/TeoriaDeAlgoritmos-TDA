def parse_tasks_file(filename):
    required_tasks = {}
    with open(filename, "r") as file:
        for line in file:
            split_line = line.split(',')
            required_tasks[(int(split_line[0]), split_line[1])] = list(map(int, split_line[2::]))
    return required_tasks


def parse_earnings_file(filename):
    potential_earnings = {}
    with open(filename, "r") as file:
        for line in file:
            split_line = line.split(',')
            potential_earnings[int(split_line[0])] = list(map(int, split_line[1::]))
    return potential_earnings
