from abc import ABC, abstractmethod
# Abstract class for Fuzzer
class TypeMutator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    @staticmethod
    def mutate(input_string):
        pass

