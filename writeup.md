# Fully Sick Fuzzer
# COMP6447 Major Project
# by Cameron Huang, Cyrus Wilkie, Hashimi Chau, Jayden Leung

## Design & Functionality - How the fuzzer works
### Fuzzing Strategy
Our program begins by using the from_file module from the magic library to detect the file type of the input, it then loads the appropriate mutator for that file type. The current file types that our fuzzer supports are
- CSV
- JSON
The file type mutator engages in fuzzing strategies specific to the relevant file format and then calls specific data type mutators to deal with the fuzzing of data types stored within that file format.

### Type Mutations & Strategies
Our program currently supports four different data type mutations:
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

Our boolean, float and integer mutations ensure that the program being tested properly validates these data types by converting input to other arbitrary data types. These mutations also test for basic logic issues and the validation of values by setting these data types to extremely large values or positive/negative values where a negative/positive value is expected.

Our string mutations test for similar issues, but also tests for issues unique to string inputs, including buffer overflows and format string vulnerabilities. It does this by extending the input string to large, arbitrary lengths and also randomly adding in format string characters.



### Priority Queue
A priority queue is used to maintain a list of inputs to run on the provided binary. - priority based on distance (number of mutations from original input).

## What kinds of bugs your fuzzer can find?



## What improvements can be made to your fuzzer for next iteration
The improvements we want to make include:
- Increasing functionality 
    - Fuzzing 64 bit binaries
    - Increasing mutation strategies to target Plaintext, XML, JPEG, ELF, and PDF
    - Progress loggin
    - Hang detection
    - 

- Increasing speed
    -  We plan to optimise our fuzzer by improving our algorithms runtime and also to utilise multithreading for executing our payloads on the binaries


- Priority queue huristic
    - Currently our priority is based off only one factor, that is distance away from the original mutation. One of our ideas is to integrate some type of genetic algorithm into our huristic. Mutations that trigger a new code path will have a higher priority compared with one that doesn't. Inorder to do this, we will need a way to measure code coverage.

- Fault detection


## Something Awesome Ideas
Currently our something awesome ideas include
- Hosting our fuzzer online
-  

