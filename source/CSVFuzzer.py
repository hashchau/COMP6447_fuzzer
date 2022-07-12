from Fuzzer import Fuzzer
class CSVFuzzer(Fuzzer):
    def __init__(self, binary_path, binary_input_path):
        super().__init__(binary_path, binary_input_path)
        print("Running CSV Fuzzer")
        print(f"binary_path: {self.binary_path}")
        print(f"binary_input_path: {self.binary_input_path}")
        pass

    def fuzz(self):
        return "blah"

    def get_coverage():
        return 0.0
    
    def get_type_of_crash():
        return "e.g. buffer overflow"

    