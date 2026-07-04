import time

def start_timer(duration, task_name):
    print(f'Starting task: {task_name}')
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\r{timer}', end='')
        time.sleep(1)
        duration -= 1
    print('\r00:00')


def pomodoro_cycle():
    task_name = input('Enter the task name: ')
    for i in range(4):
        start_timer(25 * 60, task_name)
        if i < 3:
            print('Time for a 5-minute break!')
            start_timer(5 * 60, 'Break')
        else:
            print('Time for a 15-minute break!')
            start_timer(15 * 60, 'Long Break')

if __name__ == '__main__':
    pomodoro_cycle()