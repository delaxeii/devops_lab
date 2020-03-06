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
folder = args.dir
l1 = []


def list_files_rec(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                l1.append([entry.name, entry.stat().st_ctime])
            elif entry.is_dir():
                list_files_rec(entry.path)
    return l1


def list_files_par(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                l1.append([entry.name, entry.stat().st_ctime])
    return l1


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
