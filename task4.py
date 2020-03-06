#!/usr/bin/env python

import requests
import getpass
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", nargs=1,
                    help="Enter repo owner", required=True)
parser.add_argument("-r", "--repo", nargs=1,
                    help="Enter repo name", required=True)
parser.add_argument("-n", "--number", nargs="?",
                    help="Number of pullrequest", const=1, default='33')
parser.add_argument("-s", "--status", action="store_true",
                    help="Pull request status")
parser.add_argument("-c", "--created", action="store_true",
                    help="Date of creating")
parser.add_argument("-ct", "--commits", action="store_true",
                    help="Count of commits")
parser.add_argument("-cm", "--comments", action="store_true",
                    help="Number of comments")
parser.add_argument("-ch", "--change", action="store_true",
                    help="Shows number of changed files")
parser.add_argument("-p", "--puller", action="store_true",
                    help="Who open request")
parser.add_argument("-V", "--version", action="version",
                    version="version 1.0, created by Andrei Leanovich")

args = parser.parse_args()

user = input("Enter Github login: ")

try:
    passw = getpass.getpass()
except Exception as err:
    print("Wrong Github password", err)

url = 'https://api.github.com/repos' + '/' + args.user + '/' + args.repo + '/pulls/' + args.number

rec = requests.get(url=url, auth=(user, passw))

file = rec.json()
output = "Current pull request" + file["title"]

if args.created:
    output += " Creation date: " + file['created_at'][:10]
if args.status:
    output += " Request status: " + file['labels'][0]['name']
if args.change:
    output += "Number of changed files = ", str(file['changed_files'])
if args.puller:
    output += " Request open : " + file['user']['login']
if args.commits:
    output += " Count of commits: " + str(file['commits'])
if args.comments:
    output += " Number of comments: " + str(file['comments'])

print(output)
