#!/usr/bin/python3

import argparse
import subprocess
import os

reverse = {"a": "z",
           "A": "Z",
           "0": "9"}

def transpile(src):
    newSrc = [""]
    for i in src:
        if i == "\n":
            newSrc.append("")
        else:
            for a, b in reverse.items():
                if a <= i <= b:
                    newSrc[-1] += chr(ord(a)+ord(b)-ord(i))
                    break
            else:
                newSrc[-1] += i
    return "\n".join(newSrc[::-1])

parser = argparse.ArgumentParser()
parser.add_argument("src", help="path to the script you want to transpile.")
parser.add_argument("--output", help="path to store the transpiled code (default is the same name as the src file with a '.py' extension)")
parser.add_argument("--bin", help="path to the Python binary to execute the script (default is 'python3')", default="python3")
parser.add_argument("--noexec", help="only transpile the code, do not execute it", action="store_true")
parser.add_argument("--nocleanup", help="do not delete transpiled code after execution", action="store_true")
parser.add_argument("args", help="arguments to pass to the transpiled script upon execution", nargs="*")
args = parser.parse_args()

with open(args.src) as file:
    src = file.read()
transpiled = transpile(src)

output = args.src
if args.output is None:
    if "." in output:
        output = ".".join(output.split(".")[:-1])
    output += ".py"
else:
    output = args.output

with open(output, "w") as file:
    file.write(transpiled)

if not args.noexec:
    subprocess.run([args.bin, output]+args.args)
if not args.nocleanup:
    os.remove(output)
