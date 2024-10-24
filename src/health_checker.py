from src.cat import Cat


class Healthcheck:
    def __init__(self, pet: Cat):
        self.pet = pet

    def check_weight(self):

        if 4 <= self.pet.weight <= 6:
            return "Weight is healthy."
        elif self.pet.weight < 4:
            return "Pet is underweight."
        else:
            return "Pet is overweight."

    def check_temperature(self):
        if 38 <= self.pet.temperature <= 39:
            return "Temperature is normal."
        else:
            return "Abnormal temperature! Consider visiting a vet."

    def health_status(self):
        weight_status = self.check_weight()
        temp_status = self.check_temperature()
        return f"{weight_status}\n{temp_status}"


if __name__ == "__main__":
    dataloader = Dataloader()
    my_cat = Cat(dataloader)
    health_checker = Healthcheck(my_cat)
    print(health_checker.health_status())
    print(my_cat.check_health_status())
