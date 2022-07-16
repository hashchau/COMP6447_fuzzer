# Fully Sick Fuzzer
# COMP6447 Major Project
# by Cameron Huang, Cyrus Wilkie, Hashimi Chau, Jayden Leung

## Design & Functionality
### Fuzzing Strategy
Our program begins by using the from_file module from the magic library o detect whatto detect the file type oite input, this thappropriate mutator for that file type. The current file types that our fuzzer supports are
- CSV
- JSON
The file type mutator then calls corresponding type mutators to fuzz the input.
ds the corres
### T & Strategies
Our program currently supports four different type mutations:y- pe Muta
    - negate boolean
    - convert boolean to string
    - convert boolean to int
    - convert boolean to floati- ons
B
    - flip all bits
    - add or subtract a random integer
    - make negative
    - make huge
    - convert float to int
    - convert float to bool
    - convert float to nullo- lean

F
    - same as aboveo- at

In
    - delete random char
    - insert random char
    - flip random bit
    - insert new line in random location
    - insert new line in random location with delimiter
    - insert format string in random location
    - extend string
    - extend string by repeating itselfteger

String

### P
A priority queue is used to SON

### CSV
