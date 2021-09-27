#!/usr/bin/python3
from posixpath import expanduser
from subprocess import run, PIPE
import argparse
from yaml import load, CLoader as Loader
from os.path import join

parser = argparse.ArgumentParser(description='Record the rostopics listed in /etc/topics-record.yml')

parser.add_argument('--team', '-t', type=str,
                    help='team name')
parser.add_argument('--location', '-l', type=str,
                    help='recording location: robot | operator')
parser.add_argument('--constraints', '-c', type=str, default='none',
                    help='applied network contraints')

args = parser.parse_args()
print(args)
print(args.team)

teamName = args.team
constraints = args.constraints
location = args.location
topicFile = join(expanduser('~'), 'topic-record.yml')

with open(topicFile, 'r') as file:
    config = load(file, Loader=Loader)
    topics = " ".join(config['topics'])
    print(topics)

topics = ''
run(['rosbag', 'record', '-o', f'{teamName}-{constraints}-{location}', 'topics'], stdout=PIPE)