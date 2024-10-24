from src.dataloader import BaseDataloader, CatDataclass


class Cat:
    def __init__(
        self,
        name,
        age,
        weight,
        body_temp,
        vomit=False,
        dataloader: BaseDataloader = None,
    ):
        """
        vomit is a boolean, name is string, and the rest are numeric
        age should be in years, weight in kg, body_temp in celcius
        """
        if dataloader is None:
            self.name = name
            self.age = age
            self.weight = weight
            self.body_temp = body_temp
            self.vomit = vomit
        else:
            data: CatDataclass = dataloader.get_data()
            self.name = data.name
            self.age = data.age

    def update_stats(self, age, weight, body_temp, vomit):
        """
        Update the cat's basic information
        """
        self.age = age
        self.weight = weight
        self.body_temp = body_temp
        self.vomit = vomit

    def get_stats(self):
        """
        Get the basic stats of a cat
        """
        return f"Cat is {self.age} years old, weighs {self.weight} kg, has a body temperature of {self.body_temp}"

    # def check_health_status(self):
    # """
    # Initially check if cat shows sign of FIP by considering the occurrence of vomit and unusual body temperature
    # """
    # if self.vomit and self.body_temp > 39.5:
    # return f"You cat checks 2 signs of FIP. "
    # elif self.vomit or self.body_temp > 39.5:
    # return f"You cat requires close monitoring. "
    # else:
    # return f"No worries of FIP."


if __name__ == "__main__":
    my_cat = Cat("Killua", 3.5, 7.7, 38)
    print(my_cat.get_stats())
    print(my_cat.check_health_status())
