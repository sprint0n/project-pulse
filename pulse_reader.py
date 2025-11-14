#!#!/usr/bin/python3

from rich import print

lines = open("pulse.txt").read().splitlines()
print(f"[cyan]Commits:[/cyan] {lines[0]}")
print(f"[cyan]Timestamp:[/cyan] {lines[1]}")
print(f"[cyan]Files Tracked:[/cyan] {lines[2]}")