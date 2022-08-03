import signal
import os
import subprocess
import re

class QEMUHelper:

    @staticmethod
    def execute_payload(target, payload_data):
        trace_file_location = "/tmp/trace"
        cmd = f'qemu-i386 -d exec -D {trace_file_location} {target}'
        # os.system(f'qemu-i386 -d exec -D {trace_file_location} {target}')
        
        try:
            process = subprocess.Popen(['qemu-i386', '-d', 'exec', '-D', f'{trace_file_location}', f'{target}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        except:
            process = subprocess.Popen(['qemu-i386', '-d', 'exec', '-D', f'{trace_file_location}', f'./{target}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            out, err = process.communicate(payload_data.encode()) 
        except subprocess.TimeoutExpired:
            process.terminate()

        if process.returncode != 0:
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

        return hash(str(unique_addresses))

# echo "a" | qemu-i386 -d exec -D trace2 ./binaries/plaintext1 
