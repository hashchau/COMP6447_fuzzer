import signal
import os
import subprocess
import re
import string
import random
import signal

class QEMUHelper:
    I386 = "qemu-i386"
    AMD64 = "qemu-x86_64"
    
    @staticmethod
    def execute_payload(target, arch, visited_addresses, node):
        random_str = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        trace_file_location = f"/tmp/trace-{random_str}"
        curr_arch = QEMUHelper.AMD64 if arch == "amd64" else QEMUHelper.I386

        try:
            if (arch == "amd64"):
                process = subprocess.Popen([curr_arch, f"{target}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                process = subprocess.Popen([curr_arch, "-d", "exec", "-D", f"{trace_file_location}", f"{target}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            if (arch == "amd64"):
                process = subprocess.Popen([curr_arch, f"./{target}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                process = subprocess.Popen([curr_arch, "-d", "exec", "-D", f"{trace_file_location}", f"./{target}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            out, err = process.communicate(node.payload.encode()) 
        except subprocess.TimeoutExpired:
            process.terminate()

        # Crashed    
        if process.returncode == -(signal.SIGSEGV):
            if os.path.isfile(trace_file_location):
                os.remove(trace_file_location)
            return (True, set(), node, process)

        # Abort
        if process.returncode == -(signal.SIGABRT):
            if os.path.isfile(trace_file_location):
                os.remove(trace_file_location)
            # We skip this, don't mutate if not segfault
            return (False, set(), node, process)

        unique_addresses = set()
        base_address = None

        if arch != "amd64":
            with open(trace_file_location, "r") as f:
                for line in f:
                    address = int(re.findall(r"0x[0-9A-F]+", str(line), re.I)[0],16)
                    if not base_address:
                        base_address = address
                    
                    relative_address = address - base_address

                    if relative_address not in visited_addresses:
                        unique_addresses.add(relative_address)
                f.close()
        
        # Delete trace file
        if os.path.isfile(trace_file_location):
            os.remove(trace_file_location)
        
        return (False, unique_addresses, node, process)

