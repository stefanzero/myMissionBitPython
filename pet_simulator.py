class Pet:
    """
    name (string)
    animal_type (string)
    hunger (integer, starts at 0)
    happiness (integer, starts at 100)

    Define three methods inside the class:

    eat()
        Decrease hunger by 10
        Print a message showing the updated hunger
        Make sure hunger doesn’t go below 0

    play()
        Increase happiness by 10
        Increase hunger by 5
        Make sure happiness doesn’t go above 100
        Print a message showing updated happiness
        play() increases happiness but also increases hunger.

    status()
        Print the pet’s name, type, hunger, and happiness

    """

    def __init__(self, name, animal_type, hunger=0, happiness=100):
        self.hunger = hunger
        self.happiness = happiness
        self.name = name
        self.animal_type = animal_type

    def __str__(self):
        return f"{self.name} is a {self.animal_type}"

    def eat(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} is now {self.hunger} hungry")

    def play(self):
        self.happiness += 10
        self.hunger += 5
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name} is now {self.happiness} happy")

    def status(self):
        print(f"{self.name} is a {self.animal_type}")
        print(f"{self.name} is {self.hunger} hungry")
        print(f"{self.name} is {self.happiness} happy")


def create_pet():
    create_another_pet = input("Would you like to create another pet? (y/n): ")
    if create_another_pet.lower() == "y":
        pet_name = input("Enter pet name: ")
        pet_type = input("Enter pet type: ")
        return Pet(pet_name, pet_type)
    else:
        return


def ask_user():
    """
    Ask how many pets the user wants to create.
    Use input() to ask the user for a number.
    Convert it to an integer using int().
    Use a for loop to gather details about each pet.
    For each pet, ask:
    What’s the pet’s name?
    What type of animal is it?
    Create a Pet object with those values.
    Add each pet to a list (e.g., pets = []).
     Create a loop that keeps running until the user chooses to exit.
    Inside the loop, display a menu like:
    What would you like to do?
    1. Feed a pet
    2. Play with a pet
    3. Check a pet's status
    4. Exit

    If the user enters 1, feed the pet.
    If the user enters 2, play with the pet.
    If the user enters 3, check the pet's status.
    If the user enters 4, exit the loop.
         _summary_
    """
    num_pets = int(input("How many pets would you like to create? "))
    pets = []
    for i in range(num_pets):
        pet_name = input(f"Enter pet name for pet {i + 1}: ")
        pet_type = input(f"Enter pet type for pet {i + 1}: ")
        pets.append(Pet(pet_name, pet_type))

    while True:
        print("What would you like to do?")
        print("1. Feed a pet")
        print("2. Play with a pet")
        print("3. Check a pet's status")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "4"]:
            choice = int(choice)
        if choice in [1, 2, 3]:
            # print pets
            for i, pet in enumerate(pets):
                print(f"{i}. {pet}")

        if choice == 1:
            pet_index = int(input("Enter the index of the pet to feed: "))
            pets[pet_index].eat()
        elif choice == 2:
            pet_index = int(input("Enter the index of the pet to play with: "))
            pets[pet_index].play()
        elif choice == 3:
            pet_index = int(input("Enter the index of the pet to check: "))
            pets[pet_index].status()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")


def exercise_1():
    pet = create_pet()
    print(pet)


def exercise_2():
    my_pet = Pet("Buddy", "Dog")
    my_pet.status()
    my_pet.eat()
    my_pet.play()
    my_pet.status()


def exercise_3():
    ask_user()


def main():
    exercise_1()
    exercise_2()
    exercise_3()


class AdvancedPet(Pet):
    """
        Extensions and Advanced Practice
    Goal: Add new features and explore advanced OOP concepts.
    Try any or all of these ideas:
    Add New Attributes:
    Add attributes like energy, health, or age to your Pet class.
    Create New Methods:
    For example, add a sleep() method that:
    Increases happiness and energy
    Might increase hunger slightly
    Prints the pet’s updated stats
    Implement a Hunger Timer:
    Make hunger increase automatically after every user action or loop iteration to simulate the pet getting hungry over time.
    Subclassing (Inheritance):
    Create subclasses that inherit from Pet, like Dog and Cat.
    Each subclass can have unique methods:
    Dog.bark()
    Cat.meow()
    And override existing methods for special behavior.
    Set Limits and Warnings:
    For example, if hunger goes above a certain level, print a warning message.
    If happiness drops too low, the pet might “run away” (exit the program or remove the pet).
    Multiple Pets Interaction:
    Allow pets to interact with each other through methods like play_with(other_pet).
    """

    def __init__(self, name, species, energy=50, health=50, age=0):
        super().__init__(name, species)
        self.energy = energy
        self.health = health
        self.age = age

    def play(self):
        # call base class method
        super().play()
        # increase hunger
        self.hunger += 5

    def sleep(self):
        self.energy += 10
        self.happiness += 5

    def play_with(self, other_pet):
        print(f"{self.name} and {other_pet.name} are playing together!")


def Dog(AdvancedPet):
    def bark(self):
        print("Woof woof!")


def Cat(AdvancedPet):
    def meow(self):
        print("Meow meow!")


if __name__ == "__main__":
    main()
