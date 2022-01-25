# File dog.py
class Dog:
    name = ""
    breed = ""

    def bark(self):
        print(f"{self.name}: Woof woof!")

    def sleep(self):
        print("Zzzzz...")

# File main.py
my_dog = Dog()
my_dog.name = "Fido"
my_dog.breed = "Pit bull"

print(f"My dog, {my_dog.name}, is a {my_dog.breed}")
my_dog.bark()
my_dog.sleep()
print()

other_dog = Dog()
other_dog.name = input("What is your dog's name? ")
other_dog.breed = input("What breed is it? ")

print(f"So, you have a {other_dog.breed} named {my_dog.name}.")
other_dog.bark()
other_dog.sleep()