#!/usr/bin/python3
from sys import argv
from Harness import Harness


def main():

    if len(argv) != 3:
        print("Usage: %s <binary> <binaryinput.txt>" % argv[0])
        exit(1)

    target = argv[1]
    binary_input_path = argv[2]

    # Create instance of harness
    Harness.create_instance(target)

    # Sets the strategy to use
    Harness.get_instance().set_fuzzer_strategy(binary_input_path)
    
    # Use the input file as the default, initial payload
    payload = b""
    with open(binary_input_path, "rb") as f:
        payload = f.read()

    # Execute the fuzzer
    Harness.get_instance().fuzz(payload)


if __name__ == "__main__":
    main()
