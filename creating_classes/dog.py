class Dog:
    """ A simple to model a DOG """
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now Sitting.")

    def rolling(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} Rolled over!.")


''' Making an Instance from a Class '''

print("\nLet’s make an instance representing a specific dog:")
my_dog = Dog('Ruby', 7)

''' Creating Multiple Instances '''

your_dog = Dog('Lucky', 3)

print(f"My Dog name is : {my_dog.name}")
print(f"Also My Dog age is : {my_dog.age}")
''' Calling Methods '''
my_dog.sit()

print(f"\nMy Dog name is : {your_dog.name}")
print(f"Also My Dog age is : {your_dog.age}")
''' Calling Methods '''
your_dog.rolling()
