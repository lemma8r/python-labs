import json
import sys
import random
from .print_result import print_result
from .cm_timer import cm_timer_1
from .unique import Unique

path = sys.argv[1] if len(sys.argv) > 1 else 'data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

data = data[:10]  # Берем только первые 10 вакансий для красивого вывода

@print_result
def f1(arg):
    return sorted(list(Unique([item['job-name'] for item in arg], ignore_case=True)), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
    salaries = [random.randint(100000, 200000) for _ in arg]
    return [f"{job}, зарплата {sal} руб." for job, sal in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
