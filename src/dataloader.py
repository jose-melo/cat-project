from abc import abstractmethod
import json
import numpy as np
import random


class CatDataclass:
    name: str
    age: int
    vomit: bool


class BaseDataloader:

    def __init__(self) -> None:
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def preprocess_data(self):
        pass

    @abstractmethod
    def get_data(self) -> CatDataclass:
        pass


class RandomDataloader(BaseDataloader):

    def __init__(self) -> None:
        super().__init__()

    def get_data(self):
        return CatDataclass(
            age=random.randint(1, 10), vomit=random.choice([True, False])
        )

        # return {
        # "vomit": np.random.choice([True, False]),
        # "weight": np.random.uniform(2, 10),
        # "age": np.random.uniform(0.5, 10),
        # "temperature": np.random.uniform(37, 40),
        # }


class JSONDataloader(BaseDataloader):

    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.data = None

    def load_data(self):
        with open(self.file_path, "r") as f:
            self.data = json.load(f)

    def preprocess_data(self):
        pass

    def get_data(self):
        return self.data


class APIDataloader(BaseDataloader):

    def __init__(self, url) -> None:
        self.url = url
        self.data = None

    def load_data(self):
        pass

    def preprocess_data(self):
        pass

    def get_data(self):
        return self.data
