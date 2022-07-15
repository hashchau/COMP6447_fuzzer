import signal
import subprocess

# Singleton class
class Harness():
    _instance = None
    _target = None
    _queue = None
    
    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def create_instance(cls, target):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._target = target
            cls._queue = []
        
    @classmethod
    def get_instance(cls):
        return cls._instance
    
    # 0 is first priority
    @classmethod
    def queue_payload(cls, payload, priority=0):
        cls._queue.append((priority,payload))
    
    # Runs the stuff in the payload
    @classmethod
    def run(cls):
        # run the queue
        # Run in sub process
        while len(cls._queue) > 0:
            print("running payload")
            # get the highest priority payload
            payload = cls._queue.pop(0)[1]
            print(payload)
            # run the payload
            cls.try_payload(payload)
        
    @classmethod
    def try_payload(cls, payload):
        process, out, err = cls.send_data(payload)
        
        # print(f"signal.SIGSEGV == {signal.SIGSEGV}")
        if process.returncode == -(signal.SIGABRT) or process.returncode != -(signal.SIGSEGV):
            # Successful
            print("no error")
            return 0
    
        print("it crashed :)")    
        return process.returncode

    @classmethod
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
    