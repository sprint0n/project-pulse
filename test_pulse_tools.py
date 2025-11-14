#!#!/usr/bin/python3
from pulse_tools import read_pulse_file

def test_read_pulse_file():
    assert read_pulse_file("pulse.txt") >= 7