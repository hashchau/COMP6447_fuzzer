from abc import ABC, abstractmethod
# Abstract class for Fuzzer
class FormatMutator(ABC):
    @abstractmethod
    def mutate_once(payload):
        """_summary_
        Mutates the payload once

        _returns_
        Returns the mutated payload
        """
        pass

    @abstractmethod
    def mutate_all(payload):
        """_summary_
        Mutates the payload with all mutations strategies 

        _returns_
        Returns a list of the mutated payloads
        """
        pass