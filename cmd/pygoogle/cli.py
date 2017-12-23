#!/usr/bin/env python
# coding: utf-8

from argparse import ArgumentParser

parser = ArgumentParser(
    prog="pygoogle",
    description="pygoogle is google drive upload tool")

parser.add_argument(
    "file_name",
    action="store",
    help="The file name")
