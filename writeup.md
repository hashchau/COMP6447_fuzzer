# Fully Sick Fuzzer
# COMP6447 Major Project
# by Cameron Huang, Cyrus Wilkie, Hashimi Chau, Jayden Leung

## Design & Functionality
### Fuzzing Strategy
Our program begins by using the from_file module from the magic library to detect the file type of the input, it then loads the appropriate mutator for that file type. The current file types that our fuzzer supports are
- CSV
- JSON
The file type mutator then calls corresponding type mutators to fuzz the input.

### Type Mutations & Strategies
Our program currently supports four different type mutations:
- Boolean
    - negate boolean
    - convert boolean to string
    - convert boolean to int
    - convert boolean to float
- Float
    - flip all bits
    - add or subtract a random integer
    - make negative
    - make huge
    - convert float to int
    - convert float to bool
    - convert float to null
- Integer
    - same as above
- String
    - delete random char
    - insert random char
    - flip random bit
    - insert new line in random location
    - insert new line in random location with delimiter
    - insert format string in random location
    - extend string
    - extend string by repeating itself

### Priority Queue
A priority queue is used to maintain a list of inputs to run on the provided binary. - priority based on distance (number of mutations from original input)