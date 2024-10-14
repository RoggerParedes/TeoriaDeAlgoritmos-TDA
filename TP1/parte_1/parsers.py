def merge_sort(lst):
  if len(lst) <= 1:
    return lst
  middle = len(lst) // 2
  left = lst[:middle]
  right = lst[middle:]
  sleft = merge_sort(left)
  sright = merge_sort(right)
  return merge(sleft, sright)

def merge(left, right):
  result = []
  while left and right:
    if left[0][1] > right[0][1]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  if left:
    result += left
  if right:
    result += right
  return result

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
            max_weeks = len(earnings)
            for week_number in range(1, max_weeks + 1):
                task_earning_tuple = (task_number, earnings[week_number-1])
                try:
                    max_earning_per_week[week_number].append(task_earning_tuple)
                except KeyError:
                    max_earning_per_week[week_number] = []
                    max_earning_per_week[week_number].append(task_earning_tuple)
    for key, value in max_earning_per_week.items():
        max_earning_per_week[key] = merge_sort(value)[0][0]
    return potential_earnings, max_earning_per_week
