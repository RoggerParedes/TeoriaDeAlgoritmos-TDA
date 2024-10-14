import sys
import time
from test_file_generator import generate_files
from parsers import parse_tasks_file, parse_earnings_file

BEST_RESULT = []
MAX_EARNINGS = 0
TASK_NUMBER = 0
NUMBER_OF_TASKS = 15

def max_earning(tasks, ordered_tasks, week_number, max_week, earnings):
    max_earning = 0
    for i in range(max_week-1, week_number, -1):
        for task in ordered_tasks:
            if task not in tasks:
                if earnings[task][i] > max_earning:
                    max_earning = earnings[task][i]
                    break
    return max_earning

def calculate_earnings(tasks, earnings):
    """Calcula ganancias para todas las tareas hasta el momento."""
    total = 0
    for i, task in enumerate(tasks):
        total += earnings[task][i]
    return total


def all_tasks_done(tasks, required_tasks):
    """Devuelve true si todas las tareas estan hechas, false si no."""
    return len(tasks) == len(required_tasks)


def required_tasks_done(tasks, task, required_tasks):
    """Devuelve true si es posible realizar una tarea especifica, false si no."""
    for required_task in required_tasks[task]:
        if required_task not in tasks:
            return False
    return True


def calculate_earnings_for_task(task, earnings, week_number):
    """Devuelve ganancia prevista para una tarea realizada en una semana especifica."""
    return earnings[task[TASK_NUMBER]][week_number-1]


def backtrack(tasks, earnings, required_tasks, max_weeks, max_earning_per_week):
    """Evalua el arbol de estados y poda las ramas segun la ganancia estimada no supere el maximo actual
    o el orden de taras no sea valido.."""
    global MAX_EARNINGS, BEST_RESULT
    week_number = len(tasks)+1
    earnings_so_far = calculate_earnings(tasks, earnings)
    # Se finaliza la recursion cuando se alcanza el maximo de semanas o se agotan las tareas.
    if week_number > max_weeks or all_tasks_done(tasks, required_tasks):
        if earnings_so_far > MAX_EARNINGS:
            MAX_EARNINGS = earnings_so_far
            BEST_RESULT = tasks.copy()
    else:
        for task in required_tasks:
            if task[TASK_NUMBER] not in tasks and required_tasks_done(tasks, task, required_tasks):
                tasks.append(task[TASK_NUMBER])
                task_earnings = calculate_earnings_for_task(task, earnings, week_number)
                max_possible_earning = (earnings_so_far + task_earnings +
                                        max_earning(tasks, max_earning_per_week, week_number, max_weeks, earnings) *
                                        (max_weeks - week_number))
                # Solo se evaluan los estados posteriores si el beneficio estimado es mayor que el actual.
                if max_possible_earning > MAX_EARNINGS:
                    backtrack(tasks, earnings, required_tasks, max_weeks, max_earning_per_week)
                tasks.pop()


def exercise_1():
    if len(sys.argv) < 3:
        print("Required files missing in parameters.")
        return
    generate_files(NUMBER_OF_TASKS)
    tasks = []
    required_tasks = parse_tasks_file(sys.argv[1])
    earnings, max_earning_per_week = parse_earnings_file(sys.argv[2])
    print(max_earning_per_week)
    MAX_WEEKS = len(earnings[1])
    start_time = time.time()
    backtrack(tasks, earnings, required_tasks, MAX_WEEKS, max_earning_per_week)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    print(MAX_EARNINGS)
    print(BEST_RESULT)


exercise_1()
