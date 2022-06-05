#!/usr/bin/env python
# coding: utf-8

from lib import lib01
from lib import lib02

def main():
    
    lib01_action = lib01.lib01()
    name = "Steev"
    greeding = lib01_action.hello(name)
    print(greeding)
    
    lib02_action = lib02.lib02()
    dt_now = lib02_action.print_now()
    print(dt_now)


if __name__ == '__main__': 
    main()