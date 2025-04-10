import logging
logger = logging.getLogger(__name__)

class Dog:
    dog_count = 0

    def __init__(self, id: int, race: str, age: int) -> None:
        self.id = id
        self.race = race
        self.age = age
        Dog.dog_count += 1

    @staticmethod
    def foo():
        print("asdasd")

    def bark(self) -> None:
        if self.race == "Jezevcik":
            logger.info("Jezevcik steka")
        elif self.race == "Retriever":
            logger.info("Retriever steka")
        else:
            logger.info("Haf")
