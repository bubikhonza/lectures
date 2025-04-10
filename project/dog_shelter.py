from dog import Dog
from custom_exceptions import DogNotFoundException


class DogShelter:
    def __init__(self, dogs: list[Dog]) -> None:
        self.dogs = dogs

    def all_animals_bark(self) -> None:
        for dog in self.dogs:
            dog.bark()

    def remove_dogs_by_id(self, dog_id: int) -> None:
        self.dogs = [d for d in self.dogs if d.id != dog_id]

    def get_dog_by_id(self, dog_id: int) -> Dog:
        for d in self.dogs:
            if d.id == dog_id:
                return d
        raise DogNotFoundException(f"Dog was not found while searching for its id!!! searched for: {dog_id}")
