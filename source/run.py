from PDFFuzzer import PDFFuzzer
from CSVFuzzer import CSVFuzzer
from sys import argv
from magic import from_file

def get_strategy(binary_input_path):
    file_type = from_file(binary_input_path)
    if "CSV" in file_type:
        print("Selecting CSV Fuzzer")
        return CSVFuzzer
    elif "JPEG" in file_type:
        print("Selecting JPEG Fuzzer")
    elif "JSON" in file_type:
        print("Selecting JSON Fuzzer")
    elif "ASCII text" == file_type:
        print("Selecting plaintext Fuzzer")
    elif "HTML document, ASCII text" == file_type:
        print("Selecting XML Fuzzer")
    
    print("Unknown file type, using all fuzzers")
    return CSVFuzzer # Change later

def main():

    if len(argv) != 3:
        print("Usage: %s <binary> <binaryinput.txt>" % argv[0])
        exit(1)

    binary_path = argv[1]
    binary_input_path = argv[2]

    print("Fuzzing this thing...")
    fuzzer_strat = get_strategy(binary_input_path)
    fuzzer = fuzzer_strat(binary_path, binary_input_path)

    result = fuzzer.fuzz()
    print("Found bad input, writing to bad.txt")
    with open("bad.txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
