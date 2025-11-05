def add_security(func):

    def wrapper():
        print("1.Before the function is called")
        print("2. Add Helmet, Dashcash, Gloves, Knee Guards")
        func()
        print("3.After the function is called")
        print("4. Secure Driving, leave all the items")

    return wrapper


@add_security
def drive_ola_scooter():
    print("Test driving a ola scooter")


drive_ola_scooter()

