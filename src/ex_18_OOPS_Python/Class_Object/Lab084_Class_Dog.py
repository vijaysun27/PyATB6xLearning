class Dog:
    name = None
    breed = None
    height = None
    weight = None

    def bark(self):
        print("Barking")
        print(self.name)

    def playful(self, name):
        print(f"{name}, You are very playful! {name}")

rancho = Dog()
rancho.playful("Rancho")