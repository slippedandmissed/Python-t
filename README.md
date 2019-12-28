# Python't
An esoteric programming language based on Python

Start with normal Python code. Each letter then gets replaced with its inverse (e.g. "a" is replaced with "z", "C" is replaced with "X", "8" is replaced with "1"). Any character which is not alphanumeric stays unchanged. Then the order of the lines is reversed.

## Usage
usage: pythont.py [-h] [--output OUTPUT] [--bin BIN] [--noexec] [--nocleanup] src [args [args ...]]

positional arguments:<br />&nbsp;&nbsp;src&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path to the script you want to transpile.<br />&nbsp;&nbsp;args&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; arguments to pass to the transpiled script upon execution

optional arguments:<br />&nbsp;&nbsp;-h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; show this help message and exit<br />&nbsp;&nbsp;--output OUTPUT&nbsp;&nbsp;path to store the transpiled code (default is the same name<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; as the src file with a '.py' extension)<br />&nbsp;&nbsp;--bin BIN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path to the Python binary to execute the script (default is<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'python3')<br />&nbsp;&nbsp;--noexec&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; only transpile the code, do not execute it<br />&nbsp;&nbsp;--nocleanup&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;do not delete transpiled code after execution
