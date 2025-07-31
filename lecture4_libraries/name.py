import cowsay
import sys

if len(sys.argv) == 2:
     cowsay.trex("Hello, my name is " + sys.argv[1])
else:
     print("Usage: python name.py <name>")

    