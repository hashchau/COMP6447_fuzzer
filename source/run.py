#!/usr/bin/python3
import sys
import os
from strategies.JSONFuzzer import JSONFuzzer
from strategies.CSVFuzzer import CSVFuzzer
from sys import argv
from magic import from_file
from strategies.Harness import Harness
    
def get_strategy(binary_input_path):
    file_type = from_file(binary_input_path)
    if "CSV" in file_type:
        print("Selecting CSV Fuzzer")
        return CSVFuzzer
    elif "JPEG" in file_type:
        print("Selecting JPEG Fuzzer")
    elif "JSON" in file_type:
        print("Selecting JSON Fuzzer")
        return JSONFuzzer
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

    target = argv[1]
    binary_input_path = argv[2]



    # Create instance of harness
    Harness.create_instance(target)
    # Harness.get_instance().queue_payload(b'{"len": 1000012, "input": "AAAABBBBCCCC", "more_data": ["a", "bb"]}')
    # Harness.get_instance().run()

    print("Fuzzing this thing...")
    fuzzer_strat = get_strategy(binary_input_path)
    fuzzer = fuzzer_strat(target, binary_input_path)

    result = 0
    result = fuzzer.fuzz()
    print("Found bad input, writing to bad.txt")
    with open("bad.txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
