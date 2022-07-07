from abc import ABC, abstractmethod
# Abstract class for Fuzzer
class Fuzzer(ABC):
    def __init__(self, binary_path, binary_input_path):
        self.binary_path = binary_path
        self.binary_input_path = binary_input_path
        pass

    @abstractmethod
    def is_type(binary_path):
        pass
    
    @abstractmethod
    def fuzz(self):
        """_summary_
        Fuzz the PDF file

        _returns_
        Returns the input that crashed the binary
        """
        pass

    @abstractmethod
    def get_coverage():
        """_summary_
        Get the current coverage of fuzzer on the binary file
        
        _returns_
        Returns the coverage as a percentage
        """
        pass


    @abstractmethod
    def get_type_of_crash():
        """_summary_
        Get the type of crash that was found

        This is only run after fuzz()

        _returns_
        Returns the type of crash
        """
        pass
