import time, os, re
from datetime import datetime


def parse():
    pass

str1 =  "date: 2022-12-09"

def main():
    f = open('files/timetable')
    for line in f:
        if line == str1:
            print(str1)
    
main()