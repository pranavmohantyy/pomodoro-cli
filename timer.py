import time

def start_timer(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\r{timer}', end='')
        time.sleep(1)
        duration -= 1
    print('\r00:00')


def pomodoro_cycle():
    for i in range(4):
        start_timer(25 * 60)
        if i < 3:
            print('Time for a 5-minute break!')
            start_timer(5 * 60)
        else:
            print('Time for a 15-minute break!')
            start_timer(15 * 60)

if __name__ == '__main__':
    pomodoro_cycle()