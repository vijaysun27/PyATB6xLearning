def before_after_ui_test(func):

    def wrapper():
        print("Before running the test")
        func()
        print("After running the test")
    return wrapper

@before_after_ui_test
def test_ui():
    print("Hi, I am testing a UI")

test_ui()