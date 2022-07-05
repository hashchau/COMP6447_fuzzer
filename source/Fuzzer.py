from source.PDFFuzzer import PDFFuzzer
from sys import argv

def main():
    # Read input
    if len(argv) != 2:
        print("Usage: %s <pdf_file>" % argv[0])
        exit(1)

    fuzzer = PDFFuzzer()
    result = fuzzer.fuzz()
    print(result)




if __name__ == "__main__":
    main()
