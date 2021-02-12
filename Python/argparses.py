#!/bin/python
# coding: utf8
# lang: python 3

import argparse

from body import Body
from cell import Cell
from seed import Seed
from seedlist import SeedList

FILES = True

def argvparses():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=int, dest='x', help='x size', default='10')
    parser.add_argument('-y', type=int, dest='y', help='y size', default='10')
    parser.add_argument('--random', '-R', type=bool, dest="random" ,help="to start with random spwan life", default=True)
    parser.add_argument('--maxcycle', type=int, dest='maxcycle', default='10000')
    parser.add_argument('--maxtry', type=int, dest='maxtry', default=1)
    parser.add_argument('--seed', '-s', type=str, dest='seedname', default='spaceships')
    parser.add_argument('--movespeed', type=float, dest='movespeed', default=0.20)
    argv = parser.parse_args()
    return argv

def getseed(name):
    for s in SeedList:
        if s['name'] == name:
            out = Seed(s['x'], s['y'], s['name'], s['seed'])
            return out

def main():
    argv = argvparses()
    if FILES == True:
        mybody = getseed(argv.seedname)
    else:
        mybody = Body(argv.x, argv.y)
    print(mybody)
    for i in range(argv.maxtry):
        mybody.MoveBody(maxcycle=argv.maxcycle,movespeed=argv.movespeed)

if __name__ == "__main__":
    main()
