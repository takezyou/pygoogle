#!/usr/bin/env python
# coding: utf-8

import sys
import traceback
from cli import parser
from core import upload
import datetime

def time_add(args):
    time = datetime.datetime.now().strftime("%Y/%m/%d %H-%M-%S")
    file_name = time + args.file_name

    upload(file_name)

    return 0

def main(argv=sys.argv):

    argv = argv[1:]

    if len(argv) == 0:
        parser.parse_args(["-h"])
        sys.exit(0)
    
    args = parser.parse_args(argv)
    
    try:
        exit_code = time_add(args)
        sys.exit(exit_code)
    
    except Exception as e:
        error_type = type(e).__name__ 
        sys.stderr.write("{0}: {1}\n".format(error_type, e.message))
        sys.exit(1)

if __name__ == "__main__":

    main()