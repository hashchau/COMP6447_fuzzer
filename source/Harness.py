import signal
import subprocess
from queue import PriorityQueue
from strategies.JSONMutator import JSONMutator
from strategies.CSVMutator import CSVMutator

from magic import from_file
import copy

# Singleton class
class Harness():
    _instance = None
    _target = None
    _mutations = None
    _strategy = None
    _successful_payload = None
    
    
    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def create_instance(cls, target):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._target = target
            cls._mutations = PriorityQueue()
        
    @classmethod
    def get_instance(cls):
        return cls._instance
    
    # Does not modify original queue
    def execute_mutations(cls):
        good_mutations = PriorityQueue()
        
        # Create a copy of the queue so we dont modify the original
        queue_copy = PriorityQueue()
        for i in cls._mutations.queue:
            queue_copy.put(i)
        print(f"queue_copy == {queue_copy.queue}")

        # run the queue
        while not queue_copy.empty():
            print("running payload")
            # get the highest priority payload
            priority, payload = queue_copy.get()
            # run the payload
            cls.try_payload(payload)
            
            # Todo determine if this mutation was good, if so add it to good mutation
            # good_mutations.put((0,payload))
            
        return good_mutations
    
    # Entry point
    def fuzz(cls, default_payload):
        # _mutations: a
        # a -> aa
        # a -> ab
        # a -> a%x
        # a -> aaaaaa
        
        # next_mutations: aaa aax a%x%x a%x%d
        round = 1
        # Add the default payload to the mutation queue
        cls._mutations.put((0,default_payload))
        
        while True:
            if round == 5:
                break
                
            print(f"Fuzzing round {round}")                
            # Run the fuzzer on current mutations
            next_mutations = cls.execute_mutations()
            
            # Check if crash
            if not cls._successful_payload is None:
                break
            
            # Generate new mutations
            while not cls._mutations.empty():
                priority, payload = cls._mutations.get()
                
                
                # Strategy 1
                # # Mutate twice
                # for i in range(2):
                #     mutated_payload = cls._strategy.mutate(payload)
                #     next_mutations.put((priority + 1, mutated_payload))
                
                
                # Strategy 2
                mutated_payloads = cls._strategy.mutate_all(payload)
                for mutated_payload in mutated_payloads:
                    next_mutations.put((priority + 1, mutated_payload))
                
                
            # Replace queue with new mutations
            cls._mutations = next_mutations
            round += 1

        print("Finished fuzzing, writing payload to bad.txt")
        print(f"payload written to bad.txt == {cls._successful_payload}")
        with open("bad.txt", "wb") as f:
            f.write(cls._successful_payload)
        
    
    def try_payload(cls, payload):
        process, out, err = cls.send_data(payload)
        
        # print(f"signal.SIGSEGV == {signal.SIGSEGV}")
        if process.returncode == -(signal.SIGABRT) or process.returncode != -(signal.SIGSEGV):
            # Successful
            print("no error")
            return 0
    
        print("it crashed :)")
        cls._successful_payload = payload
        return process.returncode

    def send_data(cls, payload_data):
        try:
            process = subprocess.Popen([f'{cls._target}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            process = subprocess.Popen([f'./{cls._target}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        try:
            out, err = process.communicate(payload_data) 
        except subprocess.TimeoutExpired:
            print("Process exceeded given timeout value")
            process.terminate()

        return (process, out, err) 

    def set_fuzzer_strategy(cls, default_input):
        file_type = from_file(default_input)
        if "CSV" in file_type:
            print("Selecting CSV Fuzzer")
            cls._strategy = CSVMutator
            return
        elif "JPEG" in file_type:
            print("Selecting JPEG Fuzzer")
        elif "JSON" in file_type:
            print("Selecting JSON Fuzzer")
            cls._strategy = JSONMutator
            return
        elif "ASCII text" == file_type:
            print("Selecting plaintext Fuzzer")
        elif "HTML document, ASCII text" == file_type:
            print("Selecting XML Fuzzer")
        
        print("Unknown file type, using all fuzzers")
        cls._strategy = CSVMutator
        
