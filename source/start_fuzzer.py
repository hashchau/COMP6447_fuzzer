#!/usr/bin/env python3

import os
import sys

binary_list = ["plaintext1", "plaintext2", "plaintext3", "xml1", "xml2", "xml3", "csv1", "csv2", "json1", "json2"]
if __name__ == "__main__":
    if len(sys.argv) == 2:
        os.system(f"./run.py ../binaries/{sys.argv[1]} ../binaries/{sys.argv[1]}.txt")
    else:
        for binary in binary_list:
            os.system(f"./run.py ../binaries/{binary} ../binaries/{binary}.txt")

