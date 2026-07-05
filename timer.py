import time
import json
from datetime import datetime

def start_timer(duration, task_name):
    print(f'Starting task: {task_name}')
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\r{timer}', end='')
        time.sleep(1)
        duration -= 1
    print('\r00:00')


def save_session(task_name, duration):
    session = {
        'task_name': task_name,
        'start_time': datetime.now().isoformat(),
        'duration': duration
    }
    try:
        with open('sessions.json', 'r') as f:
            sessions = json.load(f)
    except FileNotFoundError:
        sessions = []
    sessions.append(session)
    with open('sessions.json', 'w') as f:
        json.dump(sessions, f, indent=4)


def pomodoro_cycle():
    task_name = input('Enter the task name: ')
    for i in range(4):
        start_time = time.time()
        start_timer(25 * 60, task_name)
        duration = time.time() - start_time
        save_session(task_name, duration)
        if i < 3:
            print('Time for a 5-minute break!')
            start_timer(5 * 60, 'Break')
        else:
            print('Time for a 15-minute break!')
            start_timer(15 * 60, 'Break')