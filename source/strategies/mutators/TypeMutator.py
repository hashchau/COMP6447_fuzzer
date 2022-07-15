from abc import ABC, abstractmethod
# Abstract class for Fuzzer
class TypeMutator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def mutate(input_string):
        pass
