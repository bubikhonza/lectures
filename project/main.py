from dog import Dog
from dog_shelter import DogShelter
from custom_exceptions import DogNotFoundException

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='../mylog.log', encoding='utf-8', level=logging.INFO)


dogs = [
    Dog(race="Retriever", age=10, id=0),
    Dog(race="Retriever", age=12, id=1),
    Dog(race="Retriever", age=1, id=2),
    Dog(race="Jezevcik", age=5, id=3),
    Dog(race="Dalmatin", age=11, id=4)
]

shelter = DogShelter(dogs=dogs)

try:
    shelter.all_animals_bark()
    dog = shelter.get_dog_by_id(1)
    dog2 = shelter.get_dog_by_id(100)
    print(dog.race, dog.id)
except DogNotFoundException as e:
    print("DOG MISSING, SEND MAIL URGENTLY!! ERROR: ", e)
except Exception as e:
    print("Some other exception happened, informing employees")
    raise

