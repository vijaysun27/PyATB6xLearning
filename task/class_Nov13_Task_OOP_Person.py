'''Create a Person class where we will have five attributes and five behaviors.
Make sure that each type of function is used,
and I want you to also create the print function, which will print all the instance variable values. '''


class Person:
    def __init__(self,name,age,occupation,city,marital_status):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.city = city
        self.marital_status = marital_status

    def display_info(self):
        return f"Hello! I am {self.name}, I am {self.age}, I am working as a {self.occupation}, I live in {self.city} and I am {self.marital_status}"

    def talk(self):
        return f"I can talk n talk n talk n talk n talk...."

    def jump(self):
        return f"I am a high jumper"

    def sing(self):
        return f"I can sing all day"

    def dance(self):
        return f"I love to dance"

    def play(self):
        return f"I love to play cricket, I am a fast bowler"

p1 = Person("Vijay",39,"QA","Chennai","Married")
p2 = Person("Guru",39,"SDET","Chennai","Married")

# Person1_info = p1.display_info()
# Person2_info = p2.display_info()
# Person1_tal = p1.dance()
# Person2_tal = p1.play()
# print(f"{Person1_info} and {Person1_tal}")
# print(f"{Person2_info} and {Person2_tal}")

# Person1 = p1.display_info(),p1.dance()
# Person2 = p2.display_info(),p1.play()
# print(Person1)
# print(Person2)

Person1_info,Person1_tal=p1.display_info(),p1.dance()
print(Person1_info,Person1_tal)
Person2_info,Person2_tal=p2.display_info(),p2.play()
print(Person2_info,Person2_tal)
