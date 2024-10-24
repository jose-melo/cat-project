from abc import abstractmethod
from tkinter import Canvas

from src.cat import Cat
from src.health_checker import Healthcheck


class BaseGUI:

    def __init__(self, pet, health_checker) -> None:
        pass

    @abstractmethod
    def show_welcome(self):
        pass

    @abstractmethod
    def show_pet_info(self):
        pass

    @abstractmethod
    def show_pet_health_status(self):
        pass


class GUITkinter(BaseGUI):

    def __init__(self, pet: Cat, health_checker: Healthcheck) -> None:
        super().__init__()
        self.pet = pet
        self.health_checker = health_checker

        self.canvas = Canvas(width=800, height=600, bg="white")
        self.buttons = []

    def show_welcome(self):
        self.canvas.create_text(
            400,
            50,
            text="Welcome to the pet health checker!",
            font=("Helvetica", 24, "bold"),
        )


class GUITerminal(BaseGUI):

    def __init__(self, pet: Cat, health_checker: Healthcheck) -> None:
        super().__init__()
        self.pet = pet
        self.hc = health_checker

    def show_welcome(self):
        print("Welcome to the pet health checker!")

    def show_pet_info(self):
        print(
            f"Your pet is {self.pet.age} years old, weighs {self.pet.weight} kg, and has a body temperature of {self.pet.body_temp}"
        )

    def show_pet_health_status(self):
        print(self.hc.health_status())


if __name__ == "__main__":
    my_cat = Cat("Killua", 3.5, 7.7, 38)
    health_checker = Healthcheck(my_cat)
    gui = GUITerminal(my_cat, health_checker)
    gui.show_welcome()
    gui.show_pet_info()
    gui.show_pet_health_status()
