from abc import ABC, abstractmethod
# Abstract class for Fuzzer
class TypeMutator(ABC):
    @abstractmethod
    def mutate(input_string):
        pass

