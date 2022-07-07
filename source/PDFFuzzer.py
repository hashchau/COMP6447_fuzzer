class PDFFuzzer:
    def __init__(self, binary_path, binary_input_path):
        print("Running PDF Fuzzer")
        self.binary_path = binary_path
        self.binary_input_path = binary_input_path
        print(f"binary_path: {self.binary_path}")
        print(f"binary_input_path: {self.binary_input_path}")
        pass

    @staticmethod
    def isType(binary_path):
        """_summary_
        Check if the type is a pdf
        """

        return True

    def fuzz(self):
        """_summary_
        Fuzz the PDF file

        _returns_
        Returns the input that crashed the binary
        """

        return "blah"