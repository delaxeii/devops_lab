#!/usr/bin/env python
import os
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="Enter the path", required=True)
parser.add_argument("-d", "--directory", action="store_true", help="Parent directory")
parser.add_argument("-f", "--recursive", action="store_true", help="Files recursively")
parser.add_argument("sn", "-sortname", action="store_true", help="Order by filename")
parser.add_argument("st", "-sorttime", action="store_true", help="Order by date of creation")
parser.add_argument("ext", "--extension", help="Filter by file extension")
parser.add_argument("-v", action="version", version="Version 1.0, by Andrei Leanovich")

args = parser.parse_args()

if args.directory:
    for entry in os.listdir(args.path):
        if os.path.isfile(os.path.join(args.path, entry)):
            print(entry)

if args.recursive:
    list_files(args.path)
else:
    with os.scandir(args.path) as entries:
        for entry in entries:
            if entry.is_file():
                print([entry.name, os.path.getctime(entry)])

if args.extention:
    for root, dirs, files in os.walk(args.path):
        for file in files:
            if file.endswith(args.extention):
                print(os.path.join(root, file))

if args.sortname:
    s = sorted(os.listdir(args.path))
    for i in range(len(s)):
        print(s[i])

def get_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%Y-%m-%d')
    return formated_date
