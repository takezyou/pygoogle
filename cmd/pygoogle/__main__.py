#!/usr/bin/env python
# coding: utf-8

import sys
from cli import parser
from core import upload

def main(argv=sys.argv):
    
    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(0)
    
    args = parser.parse_args(argv)
    
    try:
        if args.file_name:
            upload(file_name)
    
    except Exception as e:
        error_type = type(e).__name__ 
        sys.stderr.write("{0}: {1}\n".format(e_type, e.message))
        sys.exit(1)

if __name__ == "__main__":

    main()