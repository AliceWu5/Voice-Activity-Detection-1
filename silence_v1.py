#!/usr/bin/python


import os, sys

def convert(folder):
    print folder
    os.chdir(folder)
    files = os.listdir('.')
    for file in files:
         print file
         f = open(file)
         for line in f:
              if line.split('\n')[0] == '0':
                    #print line
                    line == 'SIL'
                    print line

if __name__ == '__main__':
    folder = '../energy'
    convert(folder)






