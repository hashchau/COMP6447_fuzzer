from abc import ABC, abstractmethod
# Abstract class for Fuzzer
class FormatMutator(ABC):
    @abstractmethod
    def mutate_once(default_payload, payload):
        """_summary_
        Mutates the payload once

        _returns_
        Returns the mutated payloads
        """
        pass