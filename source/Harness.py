from asyncio import ALL_COMPLETED
import signal
import subprocess
import time
from pwn import ELF
from queue import PriorityQueue
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from multiprocessing import cpu_count

from QEMUHelper import QEMUHelper
from strategies.JSONMutator import JSONMutator
from strategies.CSVMutator import CSVMutator
from strategies.PlaintextMutator import PlaintextMutator
from strategies.XMLMutator import XMLMutator

from magic import from_file

# Singleton class
class Harness():
    _instance = None
    _target = None
    _mutations = None
    _strategy = None
    _successful_payload = None
    _visited_addresses = set()
    _THREAD_POOL_SIZE = 5 #cpu_count()

    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def create_instance(cls, target):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._target = target
            cls._arch = ELF(target).arch
            cls._mutations = PriorityQueue()
        
    @classmethod
    def get_instance(cls):
        return cls._instance

    def execute_mutations(cls):
        start = time.time()
        good_mutations = PriorityQueue()
        
        # Create a copy of the queue so we dont modify the original
        queue_copy = PriorityQueue()
        for i in cls._mutations.queue:
            queue_copy.put(i)

        with ThreadPoolExecutor(max_workers=cls._THREAD_POOL_SIZE) as executor:
            futures = []
            while not queue_copy.empty():
                node = queue_copy.get()
                futures.append(executor.submit(QEMUHelper.execute_payload, cls._target, cls._arch, cls._visited_addresses, node))

            # futures_tuple_of_sets = wait(futures, return_when=ALL_COMPLETED)
            # done_futures_set = futures_tuple_of_sets.done
             
            for t_count, i in enumerate(as_completed(futures)):
            # for t_count, i in enumerate(done_futures_set):
                
                result = i.result()
                if result is None:
                    continue
                success, unique_addresses, node, process = result

                # Crashed
                if success:
                    end = time.time()
                    runtime = end - start
                    cls._successful_payload = node.payload
                    Harness.log_crash(node.payload, process, runtime)
                    return

                if len(unique_addresses) > 0:
                    for address in unique_addresses:
                        cls._visited_addresses.add(address)
                            
                    good_mutations.put(Node(node.payload, node.distance + 1, True))

                    print(f"Found {len(unique_addresses)} unique addresses")

        return good_mutations
        
        # # run the queue
        # while not queue_copy.empty():
        #     # get the highest priority payload
        #     priority, payload = queue_copy.get()
        #     # run the payload

        #     # Multithreading

        #     success, unique_addresses = QEMUHelper.execute_payload(cls._target, cls._arch, cls._visited_addresses, payload)
        #     if success:
        #         cls._successful_payload = payload
        #         return

        #     if len(unique_addresses) > 0:
        #         for address in unique_addresses:
        #             cls._visited_addresses.add(address)
                        
        #         good_mutations.put((priority, payload))

        #         print(f"Found {len(unique_addresses)} unique addresses")

        # return good_mutations

    def mutate_vertically(cls, payload, num):
        mutated_payloads = [payload]
        for i in range(num):
            mutated_payloads.append(cls._strategy.mutate_once(mutated_payloads[-1])[0])
 
        return mutated_payloads

    # Entry point
    def fuzz(cls, default_payload):
        round = 1
        # Add the default payload to the mutation queue
        cls._mutations.put(Node(default_payload, 0, False))
                
        while True:
            print(f"Fuzzing mutation set {round}")                
            # Run the fuzzer on current mutations
            next_mutations = cls.execute_mutations()
            
            # Check if crash
            if cls._successful_payload:
                break
            
            # Generate new mutations
            if next_mutations.qsize() == 0:
                node = cls._mutations.get()
                mutated_payloads = cls._strategy.mutate_once(default_payload, node.payload)
                    
                for mutated_payload in mutated_payloads:
                    next_mutations.put(Node(mutated_payload, node.distance, False))



            # Replace queue with new mutations
            print(f"Found {next_mutations.qsize()} new mutations, using them as the next mutation set")
            cls._mutations = next_mutations
            round += 1

    


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
            cls._strategy = PlaintextMutator
            return
        elif "XML" in file_type:
            print("Selecting XML Fuzzer")
            cls._strategy = XMLMutator
            return
        elif "HTML document, ASCII text" == file_type:
            print("Selecting XML Fuzzer")
            cls._strategy = XMLMutator
            return
        
        print("Unknown file type, using all fuzzers")
        cls._strategy = PlaintextMutator


    def log_crash(successful_payload, process, runtime):
        if process.returncode == -(signal.SIGSEGV):
            print("The program exited with a segmentation fault")
        elif process.returncode == -(signal.SIGABRT):
            print("The program aborted")
        else:
            print("Other error")
        output = "\n" + "-" * 100 + "\n"
        output += "Fully Sick Fuzzer - by the boyz \n" 
        output += "-" * 100 + "\n"
        output += f"Run time: {round(runtime, 3)}\n"
        # output += "Strategy: \n"
        # output += "Distance from original input: \n"

        output += f"The length of the payload is {len(successful_payload)} bytes\n"
        output += "Finished fuzzing, writing payload to bad.txt"
        print(output)

        with open("bad.txt", "w") as f:
            f.write(successful_payload)

class Node:
    def __init__(self, payload, distance, new_coverge_branches):
        self.payload = payload
        self.distance = distance
        self.new_coverge_branches = new_coverge_branches        

    def __lt__(self, other):
        if self.distance != other.distance:
            return self.distance < other.distance
        return self.new_coverge_branches < other.new_coverge_branches
    
    def __gt__(self, other):
        if self.distance != other.distance:
            return self.distance > other.distance
        return self.new_coverge_branches > other.new_coverge_branches

    def __eq__(self, other):
        return (self.new_coverge_branches == other.new_coverge_branches) and (self.distance == other.distance)
    