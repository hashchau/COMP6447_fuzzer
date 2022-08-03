import signal
import os
import subprocess
import re
import string
import random
class QEMUHelper:

    @staticmethod
    def execute_payload(target, payload_data):
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        trace_file_location = f"/tmp/trace-{random_str}"
        
        try:
            process = subprocess.Popen(['qemu-i386', '-d', 'exec', '-D', f'{trace_file_location}', f'{target}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        except:
            process = subprocess.Popen(['qemu-i386', '-d', 'exec', '-D', f'{trace_file_location}', f'./{target}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            out, err = process.communicate(payload_data.encode()) 
        except subprocess.TimeoutExpired:
            process.terminate()

        if process.returncode != 0:
            if os.path.isfile(trace_file_location):
                os.remove(trace_file_location)
            return

        unique_addresses = set()
        base_address = None

        with open(trace_file_location, "r") as f:
            for line in f:
                address = int(re.findall(r'0x[0-9A-F]+', str(line), re.I)[0],16)

                if not base_address:
                    base_address = address
                
                relative_address = address - base_address

                if relative_address not in unique_addresses:
                    unique_addresses.add(relative_address)
            
            f.close()
        
        # Delete file
        if os.path.isfile(trace_file_location):
            os.remove(trace_file_location)
        
        return hash(str(unique_addresses))

# echo "a" | qemu-i386 -d exec -D trace2 ./binaries/plaintext1 
