import time
def countdown(func):
    def some_time():
        for i in range(1, 4):
            time.sleep(1)
            print(i)
        func()
    return some_time()
@countdown
def what_time_is_it_now():
    print(time.strftime('%H:%M'))