# Hunter Schafer, hschafer
# This file defines some classes about dogs


class Dog:
    """
    A simple class that represents a dog with a name.
    """

    def __init__(self, name):
        """
        Constructs a Dog with the given name
        """
        self.name = name

    def bark(self):
        """
        Prints the dog's name and "Woof"
        """
        print(self.name + ': Woof')

    def __eq__(self, other):
        if type(other) == Dog:
            return self.name == other.name
        else:
            return False

    def __repr__(self):
        return 'Dog(' + self.name + ')'


class DogPack:
    """
    A class that represents a group of dogs.
    Dogs can be added to the pack.
    """

    def __init__(self, pack=None):
        """
        Constructs a DogPack with no dogs.
        """
        self._my_dogs = pack if pack is not None else []

    def add_dog(self, dog):
        """
        Adds the given dog to this DogPack
        """
        self._my_dogs.append(dog)

    def all_bark(self):
        """
        Makes each dog in the DogPack bark.
        """
        for dog in self._my_dogs:
            dog.bark()


def main():
    print('Humans suck')


if __name__ == '__main__':
    main()
