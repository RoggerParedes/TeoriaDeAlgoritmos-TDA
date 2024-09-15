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
    with open(filename, "r") as file:
        for line in file:
            split_line = line.split(',')
            week_number = int(split_line[0])
            earnings = list(map(int, split_line[1::]))
            potential_earnings[week_number] = earnings
            for index, earning in reversed(list(enumerate(earnings))):
                try:
                    if index < 6:
                            if max_earning_per_week[index+2] > earning and max_earning_per_week[index+2] > max_earning_per_week[index+1]:
                                max_earning_per_week[index+1] = max_earning_per_week[index+2]
                                continue
                    if max_earning_per_week[index + 1] < earning:
                        max_earning_per_week[index + 1] = earning
                except KeyError:
                    max_earning_per_week[index+1] = earning
    return potential_earnings, max_earning_per_week
