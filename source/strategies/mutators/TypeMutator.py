from abc import ABC, abstractmethod
# Abstract class for Fuzzer
class TypeMutator(ABC):
    def __init__(self):
        raise RuntimeError('Cannot create an instance of this class')
        
    @abstractmethod
    def mutate(input_string):
        pass

