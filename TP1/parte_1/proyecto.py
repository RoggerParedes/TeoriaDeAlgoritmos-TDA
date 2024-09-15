import sys
from parsers import parse_tasks_file, parse_earnings_file

BEST_RESULT = []
MAX_EARNINGS = 0
TASK_NUMBER = 0


def calculate_earnings(tasks, earnings):
    """Calcula ganancias para todas las tareas hasta el momento."""
    total = 0
    for i, task in enumerate(tasks):
        total += earnings[task][i]
    return total


def all_tasks_done(tasks, required_tasks):
    """Devuelve true si todas las tareas estan hechas, false si no."""
    return len(tasks) != len(required_tasks)


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
    if week_number > max_weeks or not all_tasks_done(tasks, required_tasks):
        if earnings_so_far > MAX_EARNINGS:
            MAX_EARNINGS = earnings_so_far
            BEST_RESULT = tasks.copy()
    else:
        for task in required_tasks:
            if task[TASK_NUMBER] not in tasks and required_tasks_done(tasks, task, required_tasks):
                tasks.append(task[TASK_NUMBER])
                task_earnings = calculate_earnings_for_task(task, earnings, week_number)
                # La funcion de costo asume que todas las tareas de las semanas restantes otorgan
                # el mismo beneficio que el maximo de esa semana.
                try:
                    max_earning = max_earning_per_week[week_number+1]
                except KeyError:
                    max_earning = max_earning_per_week[week_number]
                # La ganancia estimada se define como la ganancia hasta ahora + la ganancia potencial
                # si cada semana se ganase el maximo posible.
                max_possible_earning = (earnings_so_far + task_earnings +
                                        max_earning * (max_weeks - week_number))
                # Solo se evaluan los estados posteriores si el beneficio estimado es mayor que el actual.
                if max_possible_earning > MAX_EARNINGS:
                    backtrack(tasks, earnings, required_tasks, max_weeks, max_earning_per_week)
                tasks.pop()


def exercise_1():
    if len(sys.argv) < 3:
        print("Required files missing in parameters.")
        return
    tasks = []
    required_tasks = parse_tasks_file(sys.argv[1])
    earnings, max_earning_per_week = parse_earnings_file(sys.argv[2])
    MAX_WEEKS = len(earnings[1])
    backtrack(tasks, earnings, required_tasks, MAX_WEEKS, max_earning_per_week)
    print(MAX_EARNINGS)
    print(BEST_RESULT)


exercise_1()
