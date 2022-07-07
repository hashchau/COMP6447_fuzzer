from PDFFuzzer import PDFFuzzer
from sys import argv

def main():

    if len(argv) != 3:
        print("Usage: %s <binary> <binaryinput.txt>" % argv[0])
        exit(1)

    binary_path = argv[1]
    binary_input_path = argv[2]

    print("Fuzzing this thing...")

    if PDFFuzzer.is_type(binary_input_path):
        fuzzer = PDFFuzzer(binary_path, binary_input_path)
    
    
    result = fuzzer.fuzz()
    print("Found bad input, writing to bad.txt")
    with open("bad.txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
