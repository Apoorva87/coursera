#!/usr/local/bin/python3
'''
A simple python template
'''
import os
import sys
import argparse

def main(args):
    parser = argparse.ArgumentParser(description="Generic template")
    parser.add_argument("-v","--verbose",
                        help="Increase verbosity of the script",
                        action="store_true")
    args = parser.parse_args()
    # call_function(args)
    print ("Template script works fine")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
