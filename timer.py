import time

def start_timer(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\r{timer}', end='')
        time.sleep(1)
        duration -= 1
    print('\r00:00')

if __name__ == '__main__':
    start_timer(25 * 60)