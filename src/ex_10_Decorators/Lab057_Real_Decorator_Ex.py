import time

def print_logs(func):

    def wrapper():
        print("Starting to capture the logs")
        func()
        print("End of the logs")
    return wrapper

def time_decorator(func):

    def wrapper():
        start_time = time.time()
        print("Start the timer", start_time)
        func()
        end_time = time.time()
        print("End the timer", end_time)
        print(f"Total time taken is, {end_time-start_time}")
    return wrapper

@time_decorator
@print_logs

def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)

@time_decorator
@print_logs

def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)

test_ui_1()
test_ui_2()