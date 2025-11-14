#!#!/usr/bin/python3

def read_pulse_file(path="pulse.txt"):
    lines = open(path).read().splitlines()
    return len(lines)